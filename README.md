Alhazerd
========

## Purpose

This personal project is an attempt at implementing a media hosting app supporting multiple formats (WebM, WebP,
PNG, JPG, PNG, GIF, BMP, ...), using Python, PyAV and learning AngularJS in the process.

## Installing

Do not install for now, here be dragons.

### Backend

If you really want to (you should use a virtualenv) :

```bash
# installing production dependencies
pip install -r requirements.txt
# installing development dependencies
pip install -r requirements-devel.txt
# running the app (dev mode)
cd backend && python backend
# or (prod mode)
cd backend && ENV=production gunicorn -w 4 -b 127.0.0.1:5555 application:app
```

### Frontend

Run the following to prepare your development (and building) environment :
```bash
npm install
```
