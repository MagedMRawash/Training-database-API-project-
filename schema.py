from model import User as UserModel, TimeStamp as TimeStampModel
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)
        fields = "__all__"


class TimeStamp(SQLAlchemyObjectType):
    class Meta:
        model = TimeStampModel
        interfaces = (relay.Node,)
        fields = "__all__"


class Query (graphene.ObjectType):
    node = relay.Node.Field()
    employees = SQLAlchemyConnectionField(User)
    timestamps = SQLAlchemyConnectionField(TimeStamp)


schema = graphene.Schema(query=Query, types=[User, TimeStamp])
