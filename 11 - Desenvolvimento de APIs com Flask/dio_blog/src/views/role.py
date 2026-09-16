from src.app import ma

class RoleSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")


class CreateRoleSchema(ma.Schema):
    name = ma.String(required=True)


class ListRolesSchema(ma.Schema):
    roles = ma.List(ma.Nested(RoleSchema))
