from flask import Flask,request
from flask_restful import Resource,Api
from sqlalchemy import create_engine
from json import dumps

e=create_engine('sqlite:///salaries.db')
app=Flask(__name__)
api=Api(app)

class testapi(Resource):
    def get(self):
        conn=e.connect()
        query=conn.execute("select distinct DEPARTMENT from salaries")
        return {'departments': [i[0] for i in query.cursor.fetchall()]}

api.add_resource(testapi, '/departments')

if __name__=='__name__':
    app.run(debug=True)



