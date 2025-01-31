from flask import Flask, request, jsonify
from flasgger import Swagger
import config
from db_model import db, Student, Lecture

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db.init_app(app)
swagger = Swagger(app)
# Swagger URL = http://localhost:8082/apidocs/

@app.route('/students', methods=['POST'])
def create_student():
    """
        Create a new student
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                name:
                  type: string
                email:
                  type: string
                score1:
                  type: number
                score2:
                  type: number
                score3:
                  type: number
                class:
                  type: string
        responses:
          201:
            description: Student created
        """
    data = request.get_json()
    student = Student(name=data['name'], email=data['email'], score1=data['score1'], score2=data['score2'], score3=data['score3'], class_=data['class'])
    db.session.add(student)
    db.session.commit()
    return jsonify({'id': student.id}), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    """
    Update an existing student
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
            score1:
              type: number
            score2:
              type: number
            score3:
              type: number
            class:
              type: string
    responses:
      201:
        description: Student updated
      404:
        description: Student not found
    """
    data = request.get_json()
    student = Student.query.get(id)
    if not student:
        return jsonify({'message': 'Student not found.'}), 404
    student.name = data['name'] if 'name' in data else student.name
    student.email = data['email'] if 'email' in data else student.email
    student.score1 = data['score1'] if 'score1' in data else student.score1
    student.score2 = data['score2'] if 'score2' in data else student.score2
    student.score3 = data['score3'] if 'score3' in data else student.score3
    student.class_ = data['class'] if 'class' in data else student.class_
    db.session.commit()
    return jsonify({'id': student.id}), 201

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """
    Get a student by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      201:
        description: Student found
      404:
        description: Student not found
    """
    student = Student.query.get(id)
    if not student:
        return jsonify({'message': 'Student not found.'}), 404
    student = mapper(student)
    return jsonify(student), 201

@app.route('/students', methods=['GET'])
def get_all_students():
    """
    Get all students
    ---
    responses:
      201:
        description: List of students
    """
    students = Student.query.all()
    students_list = []
    for student in students:
        student_data = mapper(student)
        students_list.append(student_data)
    return jsonify(students_list), 201

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    """
    Delete a student by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      201:
        description: Student deleted
      404:
        description: Student not found
    """
    student = Student.query.get(id)
    if not student:
        return jsonify({'message': 'Student not found.'}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted.'}), 201

def mapper(student):
    student_data = {
        'id': student.id,
        'name': student.name,
        'email': student.email,
        'score1': student.score1,
        'score2': student.score2,
        'score3': student.score3,
        'class': student.class_
    }
    return student_data

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=8082)