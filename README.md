# Flask Basic CRUD Application

## This application was asked as an assignment on a job interview

## Running with Docker

- A sample Dockerfile is provided that will run the application in an isolated environment
- Make sure you have `docker` installed and that the Docker daemon is running
- Build the image: `docker build -t flask_crud .`
- Run the image: `docker run -it -p 5000:5000 flask_crud`

## Project Structure Notes

- The database models are stored in the `techtest/models` folder
- The routes of the Flask app are in `techtest/routes` folder


In both cases, the modules are loaded by using the `__all__` variable in `__init__.py`, so be sure to update this if you add new files.

- The views of the models are in `techtest/templates` folder
