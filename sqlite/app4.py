from flask import Flask
from flask_restful import Resource,Api
from flask_restful import reqparse

app=Flask(__name__)
api=Api(app)

class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email',type=str,help='Email Addres to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args=parser.parse_args()
            _userEmail=args['email']
            _userPassword=args['password']

            return {'Email ':args['email'],'Password':args['password']}
        except Exception as e:
            return {'error':str(e)}

api.add_resource(CreateUser,'/CreateUser')

if __name__=='__main__':
    app.run(debug=True)



