# Conding Challenge

#### Dependencies
- Python 3.6
- MongoDB

#### Git Clone
    git clone https://github.com/elinaldosoft/challenge_b2w.git
    cd challenge_b2w/

## [Logic](hell_triangle) Hell Triangle
#### How to run example app
    python hell_triangle/main.py matrix "[[6],[3,5],[9,7,1],[4,6,8,4]]" in format String

    Numbers selected 6 + 5 + 7 + 8 = 26

#### How to run tests
    python -m unittest discover -s hell_triangle -v

#### How to run test performance
    python -m cProfile -s time hell_triangle/main.py matrix "[[6],[3,5],[9,7,1],[4,6,8,4]]"

    Numbers selected [6, 5, 7, 8] = 26
         48467 function calls (47877 primitive calls) in 0.130 seconds


## Resize Photos
#### How to run example app, follow the steps
    python pip install -r requirements.txt
    cd resize_photos
    python manage.py import_images http://54.152.221.29/images.json
    gunicorn -b 127.0.0.1:8000 config.wsgi

#### Consume API
    curl -H "Content-Type: application/json" http://127.0.0.1:8000/images.json
    or
    direct in browser

    Example output:

    {
       "images":[
          [
             "http://127.0.0.1:8000/static/media/2a30975741c39d210b184ccb479c9040.jpg",
             "http://127.0.0.1:8000/static/media/2a30975741c39d210b184ccb479c9040_320_240.jpg",
             "http://127.0.0.1:8000/static/media/2a30975741c39d210b184ccb479c9040_384_288.jpg",
             "http://127.0.0.1:8000/static/media/2a30975741c39d210b184ccb479c9040_640_480.jpg"
          ],
          [
             "http://127.0.0.1:8000/static/media/6e6d76f54fb1cdf6d8a411ef424eb20e.jpg",
             "http://127.0.0.1:8000/static/media/6e6d76f54fb1cdf6d8a411ef424eb20e_320_240.jpg",
             "http://127.0.0.1:8000/static/media/6e6d76f54fb1cdf6d8a411ef424eb20e_384_288.jpg",
             "http://127.0.0.1:8000/static/media/6e6d76f54fb1cdf6d8a411ef424eb20e_640_480.jpg"
          ]
       ]
    }


#### How to run tests
    coverage run resize_photos/manage.py test manage_photos
