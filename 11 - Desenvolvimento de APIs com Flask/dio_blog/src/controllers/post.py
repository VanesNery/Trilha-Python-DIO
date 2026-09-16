from http import HTTPStatus

from flask import Blueprint, request
from src.models import Post, db, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.views.post import  PostSchema, UpdatePostSchema

app = Blueprint('post', __name__, url_prefix='/posts')


def _create_post():
    # Lógica para criar um novo post
    post_schema = PostSchema()
    data = post_schema.load(request.json)

    post = Post(
        title=data['title'],
        body=data['body'],
        author_id=data['author_id']
    )
    db.session.add(post)
    db.session.commit()
    return {'message': 'Post criado com sucesso!'}, HTTPStatus.CREATED


def _list_posts():
    # Lógica para listar todos os posts
    query = db.select(Post)
    results = db.session.execute(query).scalars().all()
    post_schema = PostSchema(many=True)
    return post_schema.dump(results)


@app.route('/', methods=['GET'])
def list_posts():
    # Lógica para listar todos os posts
    return {'posts': _list_posts()}, HTTPStatus.OK


@app.route('/', methods=['POST'])
@jwt_required()
def handler_posts():
    # Lógica para criar um novo post
    return _create_post()


@app.route('/<int:post_id>')
def get_post(post_id):
    post = db.get_or_404(Post, post_id)
    post_schema = PostSchema()
    return post_schema.dump(post), HTTPStatus.OK


@app.route('/<int:post_id>', methods=['PATCH'])
@jwt_required()
def update_post(post_id):
    post = db.get_or_404(Post, post_id)

    # Verifica se o usuário autenticado é o autor do post
    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)

    if post.author_id != user.id and user.role.name != 'admin':
        return {'message': 'Você não tem permissão para atualizar este post.'}, HTTPStatus.FORBIDDEN

    update_post_schema = UpdatePostSchema()
    data = update_post_schema.load(request.json, partial=True)

    for fields, value in data.items():
        setattr(post, fields, value)

    db.session.commit()
    return update_post_schema.dump(post), HTTPStatus.OK


@app.route('/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    post = db.get_or_404(Post, post_id)

    # Verifica se o usuário autenticado é o autor do post
    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)

    if post.author_id != user.id and user.role.name != 'admin':
        return {'message': 'Você não tem permissão para deletar este post.'}, HTTPStatus.FORBIDDEN

    db.session.delete(post)
    db.session.commit()
    return {'message': 'Post deletado com sucesso!'}, HTTPStatus.OK
