* ### Document models not appearing / view shows blank
    * Confirm your models inherit from beanie.Document and you included them in init_beanie(..., document_models=[…]).
    * Check for errors during startup/logs.
* ### Search, filter or list_display not working
    * At present some customization features may be limited — verify if those fields exist on your document and are indexable/searchable.
* ### Compatibility issues with newer Beanie or Starlette Admin versions
    * Since this plugin is independently released, check its version and repository for compatibility notes. You may need to pin dependencies or wait for an update.