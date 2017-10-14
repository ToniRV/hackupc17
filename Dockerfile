# our base image
# FROM tensorflow/tensorflow
FROM python:3-onbuild

# specify the port number the container should expose
EXPOSE 5000

COPY flask /flask

WORKDIR /flask

# run the application
CMD ["python", "app.py"]
