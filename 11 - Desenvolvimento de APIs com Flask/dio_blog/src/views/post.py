from src.app import ma
from marshmallow import fields
from src.models.post import Post

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        include_fk = True


class GetPostParameter(ma.Schema):
    post_id = fields.Int(required=True)


class UpdatePostSchema(ma.Schema):
    title = fields.String()
    body = fields.String()
    author_id = fields.Integer(strict=True)
