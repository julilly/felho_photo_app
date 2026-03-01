# Photos App
Photo-viewing app. It allows users to register, log in, upload photos and view them. It is also possible to delete photos but only the ones that were uploaded by the user (and the user needs to be logged in).
Photos can also be ordered by their names and by their upload dates.

---

## Features

- User authentication: register, login, logout
- Upload photos (with name and date)
- List all photos
- View photo details
- Delete photos (only by owner)
- Order photos by name or upload date

---

## Architecture
The application is implemented using the Model–View–Template (MVT) architecture provided by Django:
- Models define the database structure
- Views contain the logic
- Templates describe (and render) user interface
- URLs map browser requests to view functions

## The Model
The `Photo` model defines the database structure. The fields defined in the model are automatically mapped to database columns by Django.
- an image file
- an automatically generated upload date
- a ForeignKey relationship to the User model (because every photo has an "owner": the owner is the user who uploaded it and only the owner can delete it)


## Templates
Templates are HTML files with special Django syntax. Thanks to this syntax it is possible to inject data into the HTML.
The template files:
- `base.html`: base layout
- `photo_list.html`: shows all photos and options for ordering
- `photo_detail.html`: shows a single photo
- `register.html`: shows the registration page with a button
- `upload_photo.html`: for uploading photos

---

## Authentication

Django’s built-in authentication system is used.  
This enables:

- User registration with username and password
- Secure login and logout
- Restricting access to certain features (e.g., uploading or deleting photos)

Authorization rules:

- Only authenticated users can upload photos.
- Only the owner of a photo can delete it.

## Request Flow
When a user clicks a link on the page (or opens the page), the URL dispatcher (in the urls.py file) pas the request to a view. The view can interact with the database and it passes data to the template. The template renders the HTML and thus the page is dispalyed in the browser.

## How to Run

```bash
# build docker image, from root library
docker build -t photo_app .

# run docker 
docker run photo_app
```
## Used sources
- Tutorial: https://www.youtube.com/watch?v=Rp5vd34d-z4&t=1s
- For deployment and docker file: https://www.youtube.com/watch?v=Rp5vd34d-z4&t=1s
- Multiple pages from Django documentation: https://docs.djangoproject.com/en/6.0/
- Tutorial for registration and authentication: https://www.pythontutorial.net/django-tutorial/django-registration/