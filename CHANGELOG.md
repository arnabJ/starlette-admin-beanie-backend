# Changelog

---
## 0.0.2beta2 (2025-08-04)

### Updated
- Removed projection from find_all function due to field always required bug

### Todo
- Create a proper README/Documentation

### Compatibility
- Tested with
  - starlette-admin (0.15.1)
  - Beanie-ODM (2.0.0)
  - FastAPI (0.116.1)

---
## 0.0.2beta1 (2025-07-25)

### Added
- Support for Beanie 2.0.0
- Updated CHANGELOG.md

### Todo
- Create a proper README/Documentation

### Compatibility
- Tested with
  - starlette-admin (0.15.1)
  - Beanie-ODM (2.0.0)
  - FastAPI (0.116.1)

---
## 0.0.1beta3 (2025-06-26)

### Added
- Fixed `__admin_select2_repr__` not working
- Fixed List page taking a lot of time for a huge dataset even when the limit is set to very low.
- Updated CHANGELOG.md

### Todo
- Create a proper README/Documentation

### Compatibility
- Tested with
  - starlette-admin (0.15.1)
  - Beanie-ODM (1.30.0)
  - FastAPI (0.115.13)

---
## 0.0.1beta1 (WIP, 2025-06-13) & 0.0.1beta2 (2025-06-23)

### Added
- Add filters and required helper functions
- Add order by (in find_all)
- Add search query builder
- Complete the ModelView class
- Nested Objects are automatically converted to Collection Fields

### Todo
- Create a proper README/Documentation

### Compatibility
- Tested with
  - starlette-admin (0.15.1)
  - Beanie-ODM (1.29.0)
  - FastAPI (0.115.12)

---
## 0.0.1rc1 (WIP, 2025-04-08)

### Added
- Admin class
- ModelView class (WIP)
- ModelConverter class
- normalize_list helper function

### Todo
- Add filters and required helper functions
- Add order by (in find_all)
- Add search query builder
- Complete the ModelView class
- Test create, edit & delete functionalities
- Create a proper README/Documentation

### Compatibility
- Tested with
  - starlette-admin (0.15.0rc9)
  - Beanie-ODM (1.29.0)
  - FastAPI (0.115.12)
