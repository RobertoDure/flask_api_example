# Flask Student API

This project is a RESTful API built with Flask for managing student records. It includes endpoints for creating, updating, retrieving, and deleting student records. The project uses SQLAlchemy for database interactions and Flasgger for API documentation.

## Project Structure

- `app.py`: The main application file containing the Flask app and route definitions.
- `config.py`: Configuration file for database settings.
- `db_model.py`: Contains the SQLAlchemy models for the database.
- `swagger_config.py`: Contains the Swagger documentation strings.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/RobertoDure/flask_student_api.git
    cd flask_student_api
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python app.py
    ```

## Endpoints

- `POST /students`: Create a new student.
- `PUT /students/<int:id>`: Update an existing student.
- `GET /students/<int:id>`: Get a student by ID.
- `GET /students`: Get all students.
- `DELETE /students/<int:id>`: Delete a student by ID.

## Configuration

The database configuration is stored in `config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///students.db'