from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


e = create_engine('sqlite:///salaries.db')  # loads db into memory

app = Flask(__name__)
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)

class Departments_Meta(Resource):
    def get(self):
        conn = e.connect()  # open connection to memory data
        query = conn.execute("select distinct DEPARTMENT from salaries")  # query
        return {'departments': [i[0] for i in query.cursor.fetchall()]}  # format results in dict format

class Departmental_Salary(Resource):
    def get(self, department_name):
        conn = e.connect()
        query = conn.execute("select * from salaries where Department='%s'" % department_name.upper())
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return result
class multiply(Resource):
    def get(self, number):
        return number * 2

api.add_resource(Departments_Meta, '/departments')
api.add_resource(Departmental_Salary, '/dept/<string:department_name>')
api.add_resource(multiply, '/multiply/<int:number>')

if __name__ == '__main__':
    app.run(debug=True)


