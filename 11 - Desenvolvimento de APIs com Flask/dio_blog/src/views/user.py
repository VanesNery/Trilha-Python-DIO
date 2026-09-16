
from src.app import ma
from marshmallow import fields
from src.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
       model = User
       include_fk = True
       exclude = ("password",)


class GetUserParameter(ma.Schema):
    user_id = fields.Int(required=True)


class DeleteUserParameter(ma.Schema):
    user_id = fields.Int(required=True)


class UpdateUserSchema(ma.Schema):
    username = fields.String()
    password = fields.String()
    role_id = fields.Integer(strict=True)
    active = fields.Boolean()


class CreateUserSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    role_id = fields.Integer(required=True, strict=True)
