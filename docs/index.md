<div style="display: flex; gap: 10px">
<a href="https://github.com/arnabJ/starlette-admin-beanie-backend/actions">
    <img src="https://github.com/arnabJ/starlette-admin-beanie-backend/actions/workflows/publish.yml/badge.svg" alt="Publish">
</a>
<a href="https://pypi.org/project/starlette-admin-beanie-backend/">
    <img src="https://badge.fury.io/py/starlette-admin-beanie-backend.svg" alt="Package version">
</a>
<a href="https://pypi.org/project/starlette-admin-beanie-backend/">
    <img src="https://img.shields.io/pypi/pyversions/starlette-admin-beanie-backend" alt="Supported Python versions">
</a>
<a href="https://pepy.tech/projects/starlette-admin-beanie-backend">
<img src="https://static.pepy.tech/personalized-badge/starlette-admin-beanie-backend?period=total&units=INTERNATIONAL_SYSTEM&left_color=GRAY&right_color=RED&left_text=downloads" alt="PyPI Downloads">
</a>
</div>
A plugin that integrates Beanie ODM with Starlette Admin, allowing you to use Beanie as the backend data layer for your admin interface

### Why a separate plugin?
Although Starlette Admin now offers official support for Beanie ODM, this plugin was being developed as an independent, alternate implementation long before that support existed. The decision to release it as a separate plugin was driven by the need for flexibility and control over the development and release process — allowing for faster updates, bug fixes, and compatibility with new Beanie versions without being tied to Starlette Admin’s release cycle.

Additionally, since the official Beanie integration is also a third-party contribution and has been less stable in my personal experience, continuing this independent development provides an alternative implementation that aims to offer a more reliable and consistent Beanie–Starlette Admin integration.

### Getting started
* Follow the usage guide in the [How to?](how_to.md) page.

### Features
* Supports latest Beanie Version (v2.0.0)
* Search and filtering
* OneToOne (Link) and OneToMany(List[Link]) relations

### To Do
* Support for BackLink (may work, not officially tested)
* More optimized search method
* Optional Fuzzy search

### Credits
- jowilf ([https://github.com/jowilf](https://github.com/jowilf))
- BeanieODM ([https://github.com/BeanieODM](https://github.com/BeanieODM))
- pydantic ([https://github.com/pydantic](https://github.com/pydantic))