from os import name
from flask import request, jsonify
from flask_restx import Resource, Api, Namespace
from sqlalchemy.sql.expression import null
from models.database import db_session
from models.Model import TbUsers
from datetime import datetime, timedelta
from util.auth import *

Users = Namespace('Users')

@Users.route('/')
class All_User(Resource):
    def post(self):
        try:
            post_data = request.get_json()
            user_token = post_data['token']
            data = verify_token(user_token)
            if data != None:
                try:
                    queries = db_session.query(TbUsers) 
                    entries = [dict(userid = q.userid, name = q.name, password = q.password) for q in queries]
                    response_object = {'status': 'success', 'msg':'ok'}
                    response_object['users'] = entries 

                    return response_object, 200
                finally:
                    db_session.close()
            else:
                return {}, 204

            # for instance in db_session.query(TbUsers).order_by(TbUsers.userid):
            #     print (instance.userid, instance.password)
        finally:
            db_session.close()

@Users.route('/login')
class LoginUser(Resource):
    def post(self):
        try:
            post_data = request.get_json()
            entry = db_session.query(TbUsers).filter(TbUsers.userid == post_data['email']).all()
            if entry.__len__() == 1:
                if verify_pw(post_data['password'], entry[0].password) == True:
                    response_object = {'status': 'success'}
                    response_object['userid'] = entry[0].userid
                    response_object['name'] = entry[0].name
                    response_object['msg'] = '로그인에 성공했습니다.'
                    payload = {
                        'email': entry[0].userid, 
                        'exp': datetime.utcnow() + timedelta(seconds = 60 * 60 * 24)    # 로그인 24시간 유지
                    } 
                    response_object['token'] = jwtencode(payload)
                    return response_object, 200

                else :
                    print(3)
                    return {}, 204
            else :
                print(4)
                return {}, 204
        finally:
            db_session.close()

@Users.route('/regi')
class Register(Resource):
    def post(self):
        try:
            post_data = request.get_json()
            entry = db_session.query(TbUsers).filter(TbUsers.userid == post_data['email']).all()
            if entry.__len__() == 0:
                if register_user(post_data['email'], post_data['password'], post_data['name']) == True:
                    response_object = {'status': 'Register Success', 'msg': '회원가입에 성공했습니다.'}
                    return response_object, 201
                else:
                    return {}, 204

            else:
                return {}, 203
        finally:
            db_session.close()

def register_user(userid, password, name):
    try:
        t = TbUsers(userid, encode_pw(password), name) 
        db_session.add(t) 
        db_session.commit()
        return True
    except:
        db_session.rollback()
        return False
    finally:
        db_session.close()


