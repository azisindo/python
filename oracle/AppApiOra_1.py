from flask import Flask,request
from flask_restful import Resource,Api
import cx_Oracle
import json

app=Flask(__name__)
api=Api(app)

class unitUsaha(Resource):
    def get(self):
        conn=cx_Oracle.connect('test/test@10.231.12.220:1094/testz')
        cur=conn.cursor()
        result = cur.execute("select uu_code,uu_nama,uu_tipe from unit_usaha where uu_code in ('Z001','CZ01')")
        items = [dict(zip([key[0] for key in cur.description],row)) for row in result]
        return json.dumps({'items':items})

api.add_resource(unitUsaha,'/unitUsaha')


if __name__=='__main__':
    app.run(debug=True)





