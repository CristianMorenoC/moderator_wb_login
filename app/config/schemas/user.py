from tortoise import fields, models


class User(models.Model):
    ID = fields.IntField(pk=True)
    username = fields.CharField(max_length=100)
    full_name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    password = fields.CharField(max_length=128)

    class Meta:
        table = "users"
