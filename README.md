# Patient Data Management RESTful API

## overview
This REST API prototype provides functionality to engage with a patient database by creating, reading, updating, and deleting patient records. FastAPI was used to create the user-facing API, and SQLAlchemy was used to create a mock SQLite database to enable implementation and testing of CRUD operations. The API server is hosted locally; documentation and user interaction with the API is provided through Swagger UI.

## dependencies
- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn

## building & running
* Ensure that Python 3.8 or newer is installed.
* To install the required packages, run `pip3 install fastapi sqlalchemy uvicorn` in your Python environment.
* Run the application by executing the following command on the command line: `uvicorn main:app`.
  * The API server will be hosted locally at the port number specified in the command output (e.g. `http://127.0.0.1:8000`).
  * To access the Swagger UI used to engage with the API, append `/docs` to the URL, i.e. `http://127.0.0.1:8000/docs`. Swagger UI provides both documentation and interaction functionality for the API, which you can use to test the application.
* To terminate the server, enter `^C` on the command line.
