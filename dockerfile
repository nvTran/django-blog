FROM python:3
ADD . /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8000

# CMD ["python3", "manage.py", "runserver"]
CMD exec gunicorn blog_web_app.wsgi:application --bind 0.0.0.0:8000 --workers 3 
