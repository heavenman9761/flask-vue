import jwt
from models.database import db_session
from models.Model import TbUsers
import bcrypt

SECRET_KEY = 'wntlrghltkict'

def jwtencode(payload):
    return jwt.encode(payload, SECRET_KEY, algorithm = 'HS256')

def verify_token(user_token):
    if user_token == None:
        return None
    else:
        try:
            data = jwt.decode(user_token, SECRET_KEY, algorithms=['HS256'])
            entry = db_session.query(TbUsers).filter(TbUsers.userid == data['email']).all()
            if entry.__len__() == 1:
                return data
            else:
                return None
            
        except jwt.ExpiredSignatureError:
            return None
        except:
            return None
        finally:
            db_session.close()

def encode_pw(pw):
    encrypted_password = bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt())  # str 객체, bytes로 인코드, salt를 이용하여 암호화
    return encrypted_password.decode("utf-8")  # str 객체  

def verify_pw(post_pw, saved_pw):
    return bcrypt.checkpw(post_pw.encode('utf-8'), saved_pw.encode('utf-8'))

