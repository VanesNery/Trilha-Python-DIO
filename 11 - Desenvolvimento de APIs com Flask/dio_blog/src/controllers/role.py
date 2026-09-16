from http import HTTPStatus

from flask import Blueprint, request
from src.models import db, Role
from src.views.role import CreateRoleSchema, ListRolesSchema


app = Blueprint('role', __name__, url_prefix='/roles')

@app.route('/', methods=['POST'])
def create_role():
    # Lógica para criar uma nova role
    role_schema = CreateRoleSchema()
    data = role_schema.load(request.json)

    role = Role(name=data['name'])

    db.session.add(role)
    db.session.commit()
    return {'message': 'Role criada com sucesso!'}, HTTPStatus.CREATED


@app.route('/', methods=['GET'])
def list_roles():
    # Lógica para listar todas as roles
    query = db.select(Role)
    results = db.session.execute(query).scalars().all()
    list_roles_schema = ListRolesSchema()
    return list_roles_schema.dump({'roles': results}), HTTPStatus.OK
