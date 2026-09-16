from http import HTTPStatus

from flask import Blueprint, request
from src.models import db, User
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.utils import requires_role
from src.app import bcrypt
from src.views.user import CreateUserSchema, DeleteUserParameter, UpdateUserSchema, UserSchema
from marshmallow import ValidationError

app = Blueprint('user', __name__, url_prefix='/users')

def _create_user():
    # Lógica para criar um novo usuário
    user_schema = CreateUserSchema()

    try:
        data = user_schema.load(request.json)
    except ValidationError as err:
        return {'errors': err.messages}, HTTPStatus.UNPROCESSABLE_ENTITY

    user = User(
        username=data['username'], 
        password=bcrypt.generate_password_hash(data['password']), 
        role_id=data['role_id']
    )
    db.session.add(user)
    db.session.commit()
    return {'message': 'Usuário criado com sucesso!'}, HTTPStatus.CREATED


@jwt_required()
@requires_role('admin')
def _list_users():
    # Lógica para listar todos os usuários
    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)
    query = db.select(User)
    users = db.session.execute(query).scalars()
    users_schema = UserSchema(many=True)
    return users_schema.dump(users)


@app.route('/', methods=['GET', 'POST'])
def list_or_create_users():

    if request.method == 'POST':
        # Lógica para criar um novo usuário
       return _create_user()

    # Lógica para listar todos os usuários
    return {'users': _list_users()}, HTTPStatus.OK

@app.route('/<int:user_id>')
def get_user(user_id):
    """"User detail view.    
    ---    
    get:
        tags: 
            - user
        parameters:            
            - in: path            
                name: user_id            
                schema: GetUserParameter        
        responses:            
            200:            
                description: Successful operation
                content:
                    application/json:
                        schema: UserSchema
    """
    # Lógica para obter um usuário específico pelo ID
    user = db.get_or_404(User, user_id)
    user_schema = UserSchema()
    return user_schema.dump(user), HTTPStatus.OK


@app.route('/<int:user_id>', methods=['PATCH'])
@jwt_required()
@requires_role('admin')
def update_user(user_id):
    # Lógica para atualizar um usuário específico pelo ID
    user = db.get_or_404(User, user_id)
    update_user_schema = UpdateUserSchema()
    data = update_user_schema.load(request.json)

    for field, value in data.items():
        setattr(user, field, value)

    db.session.commit()

    return {
        'id': user.id,
        'username': user.username
    }, HTTPStatus.OK

@app.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
@requires_role('admin')
def delete_user(user_id):
    """"User delete view.        
    ---        
    delete:
        tags:
            - user
        parameters:
            - in: path
                name: user_id
                schema: DeleteUserParameter
        responses:
            204:
                description: Successful operation
            404:
                description: Not found user
    """
    # Lógica para deletar um usuário específico pelo ID
    user = db.get_or_404(User, user_id)
    delete_user_schema = DeleteUserParameter()
    data = delete_user_schema.load(request.json)

    db.session.delete(data)
    db.session.commit()
    return {'message': 'Usuário deletado com sucesso!'}, HTTPStatus.NO_CONTENT
