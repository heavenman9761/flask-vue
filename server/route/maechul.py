from flask import request, jsonify
from flask_restx import Resource, Api, Namespace
from models.database import db_session
from models.Model import TbMaeChulMyungSe, TbMaeChulHapGae
from util.auth import *

MaeChul = Namespace('MaeChul')

@MaeChul.route('/daymaechul')
class getDayMaeChul(Resource):
    def post(self):
        try:
            post_data = request.get_json()
            user_token = post_data['token']
            data = verify_token(user_token)
            if data != None:
                try:
                    print(post_data)
                    response_object = {'status': 'success'}
                    print(post_data['maeJangCode'], post_data['startDate'], post_data['endDate'])
                    queries = db_session.query(TbMaeChulHapGae).filter(TbMaeChulHapGae.MaeJangCode == post_data['maeJangCode'],
                        TbMaeChulHapGae.MaeChulDate >= post_data['startDate'],
                        TbMaeChulHapGae.MaeChulDate <= post_data['endDate']).all()

                    queries = db_session.query(TbMaeChulHapGae) 
                    entries = [dict(MaeJangCode = q.MaeJangCode, MaeChulDate = q.MaeChulDate) for q in queries]
                    response_object = {'status': 'success', 'msg':'ok'}
                    response_object['datas'] = entries 

                    return response_object, 200
                finally:
                    db_session.close()
            else:
                return {}, 204

            # for instance in db_session.query(TbUsers).order_by(TbUsers.userid):
            #     print (instance.userid, instance.password)
        finally:
            db_session.close()

        return {}, 200