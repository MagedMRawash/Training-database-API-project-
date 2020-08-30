from model import User as UserModel, TimeStamp as TimeStampModel
import graphene
from graphene import relay, ObjectType
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)


class TimeStamp(SQLAlchemyObjectType):
    class Meta:
        model = TimeStampModel
        interfaces = (relay.Node,)


class Query(ObjectType):
    # employees = graphene.list(User)
    # employee_by_id = graphene.Field(User, id=graphene.String())
    node = relay.Node.Field()
    employees = SQLAlchemyConnectionField(User.connection)

    # def resolve_employees(root, info, **args):
    #     return UserModel.objects.all()

    # def resolve_employee_by_id(root, info, id):
    #     return UserModel.objects.get(pk=id)


schema = graphene.Schema(query=Query)
