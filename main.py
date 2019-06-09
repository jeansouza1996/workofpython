from flask import Flask
from flask_restful import Api, Resource, reqparse

APP = Flask(__name__)
API = Api(APP)
USERS = [
    {
        "name": "Robert",
        "age": 26,
        "occupation": "Estagiario"
    },
    {
        "name": "Jean",
        "age": 23,
        "occupation": "Administrador de Redes"
    },
    {
        "name": "Renan",
        "age": 21,
        "occupation": "Desenvolvedor"
    }
]


class User(Resource):

    def get(self, name):
        if name is None:
            return USERS, 200
        for user in USERS:
            if name == user["name"]:
                return user, 200
        return "Usuário não encontrado", 404

    def post(self, name):

        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in USERS:
            if name == user["name"]:
                return "Usuário com o nome {} já existe".format(name), 400
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }

        USERS.append(user)
        return user, 201

    def put(self, name):

        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in USERS:
            if name == user["name"]:
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        USERS.append(user)
        return user, 201

    def delete(self, name):

        global USERS
        USERS = [user for user in USERS if user["name"] != name]
        return "{} está deletado.".format(name), 200


API.add_resource(User, "/user/<string:name>")
APP.run(debug=True)
