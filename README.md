# Conding Challenge

## [Logic](hell_triangle) Hell Triangle
#### How to run example app
    python run_helltriangle.py
#### How to run tests
    python -m unittest discover -s hell_triangle -v

#### How to run test performance
    python -m cProfile -s time run_helltriangle.py

    Numbers selected [6, 5, 7, 8] = 26
         564 function calls (553 primitive calls) in 0.005 seconds



## Resize Photos
#### How to run example app, follow the steps
    - python pip install -r requirements.txt
    - cd resize_photos
    - python manage.py import_images http://54.152.221.29/images.json
    - gunicorn -b 127.0.0.1:8000 config.wsgi

#### Consume API
    curl -H "Content-Type: application/json" http://127.0.0.1:8000/images.json
    or
    direct in browser

#### How to run tests
    coverage run resize_photos/manage.py test