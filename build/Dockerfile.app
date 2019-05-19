From app-base:latest

ENV APP_HOME /mysite

RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000