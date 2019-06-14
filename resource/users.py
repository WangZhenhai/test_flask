#encoding=utf-8


# test API users
from flask_restful import reqparse, Resource

parser_put = reqparse.RequestParser ()
parser_put.add_argument ("user", type=str, required=True, help="need user data")
parser_put.add_argument ("pwd", type=str, required=True, help="need pwd data")
#
def to_do(user, pwd):
	return str (user), str (pwd)


#
class TodoList (Resource):
	def post(self):
		args = parser_put.parse_args ()
		user = args["user"]
		pwd = args["pwd"]
		info = {"info": to_do (user, pwd)}
		return info, 201