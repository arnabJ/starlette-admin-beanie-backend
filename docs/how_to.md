## Prerequisites
Before using this plugin, you should have the following set up:

* Python 3.9+ (supported through 3.13)
* A Starlette or FastAPI application (Starlette Admin works on top of Starlette)
* Beanie ODM configured and connected to your MongoDB instance
* Basic familiarity with Starlette Admin’s concept of “views” and admin mounting

## Installation
```bash
pip install starlette-admin-beanie-backend
```

!!! quote "Note"

    While the plugin is installed as `starlette-admin-beanie-backend`, all imports are available from `starlette_admin_beanie_backend`

## Basic Usage
Here’s how you get started with minimal setup:
```python
from starlette_admin_beanie_backend import Admin, ModelView
from your_app.auth import AdminAuthProvider  # your auth provider
from your_app.models import User  # a Beanie document model

def set_db_admin(app):
    admin = Admin(
        title="My Admin Interface",
        base_url="/admin",
        debug=True,
        auth_provider=AdminAuthProvider(),
    )
    admin.add_view(ModelView(User, icon="fa fa-users"))
    admin.mount_to(app)
```
### Explanation

* `Admin(...)`: creates the admin interface object
* `ModelView(User, icon="...")`: registers a view for your User document model
* `admin.mount_to(app)`: mounts the admin interface onto your Starlette (or FastAPI) app

## Example Setup
Below is a more complete example combining FastAPI, Beanie and this plugin.
```python
# main.py
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from beanie import init_beanie
from pymongo import AsyncMongoClient

from starlette_admin_beanie_backend import Admin, ModelView
from your_app.models import User, Item  # your Beanie document classes
from your_app.auth import AdminAuthProvider

@asynccontextmanager
async def lifespan(_app: FastAPI):  # type: ignore
    # Initialize DB
    client = AsyncMongoClient("mongodb://localhost:27017")
    my_db = client["testdb"]
    await init_beanie(database=my_db, document_models=[User, Item])

    # Initialize Starlette Admin
    admin = Admin(
        title="My Admin Interface",
        base_url="/admin",
        debug=True,
        auth_provider=AdminAuthProvider(),
    )

    # Add the Admin Views
    admin.add_view(ModelView(User, icon="fa fa-users"))
    admin.add_view(ModelView(Item, icon="fa fa-box", identity="item"))

    # Mount app
    admin.mount_to(app)

    print("Startup completed")
    yield
    await client.close()
    print("Shutdown completed")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
### Notes

* Ensure `init_beanie(...)` runs before you mount the admin interface so your document models are registered.
* `base_url="/admin"` means the admin will be accessible at `http://localhost:8000/admin`.
* Customize your models and views as needed.

## Customizing Views
With ModelView, you can customize how your Beanie documents are presented in the admin UI.
Example customizations might include:
```python
from enum import Enum

from starlette_admin import EmailField, EnumField
from starlette_admin_beanie_backend import ModelView

from your_app.models import User

class GENDER(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

class UserView(ModelView):
    model = User
    icon = "fa fa-user"
    fields = ["id", "first_name", "last_name", EmailField("email"), EnumField("gender", enum=GENDER)]


# Initialise admin here
...

admin.add_view(UserView(User))
```