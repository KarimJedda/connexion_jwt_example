# import flask_jwt
from run import jwt_required, current_identity


@jwt_required()
def get_secret():
	print (current_identity)
	return "https://www.youtube.com/watch?v=ZeYVAo8Tw1Y"