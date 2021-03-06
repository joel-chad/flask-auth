import uuid
import datetime

from app.main import db
from app.main.model.patient import Patient


def save_new_user(data):
    user = Patient.query.filter_by(email=data['email']).first()
    if not user:
        new_user = Patient(
            email = data['email'],
            name = data['name'],
            password = data['password'],
            age = data['age'],
            sex = data['sex'],
            address = data['address'],
            district = data['district'],
            phone_number = data['phone_number'],
            diagnosis = data['diagnosis'],
            plan = data['plan'],
            complaints = data['complaints'],
            allergies = data['allergies'],
            occupation = data['occupation'],
            marital_status = data['marital_status'],
            aid = data['aid'],
            job = data['job'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return data, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return Patient.query.all()


def get_a_user(id):
    return Patient.query.filter_by(id=id).first()

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()