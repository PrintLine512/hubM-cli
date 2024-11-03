from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from config import db_url

engine = create_engine(db_url)
Base = automap_base()
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

server_model = Base.classes['servers']

