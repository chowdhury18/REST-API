From python:3.8.5-alpine3.12

WORKDIR /usr/app

COPY requirement.txt ./

RUN pip install -r ./requirement.txt

COPY . .

EXPOSE 5000

#FLASK_APP=app.py FLASK_ENV=development flask run
CMD [ "flask", "run" ,"--host=0.0.0.0"]