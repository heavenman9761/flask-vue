from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker 
from sqlalchemy.ext.declarative import declarative_base 

engine = create_engine("mariadb+mariadbconnector://root:Rudwns9760!@localhost:3307/mw_devices?charset=utf8")
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base() 
Base.query = db_session.query_property() 

def init_db(): 
    import Model 
    Base.metadata.create_all(engine)

