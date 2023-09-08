from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    username = fields.String()
    password = fields.String()
    created_date = fields.DateTime()
    updated_date = fields.DateTime()
