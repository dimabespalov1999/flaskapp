FROM python:3.9

COPY . /flaskapp

WORKDIR /flaskapp

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python" ] 
CMD ["app.py", "5000"]