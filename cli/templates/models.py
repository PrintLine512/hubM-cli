from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import db_url

engine = create_engine(db_url)
Base = automap_base()
Base.prepare(engine, reflect=True)

server_model = Base.classes['servers']
Session = sessionmaker(bind=engine)
session = Session()
server = session.query(server_model).filter_by(name="Smart").first()
print(server.name)

