from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from config import db_url

engine = create_engine(db_url)
Base = automap_base()
Base.metadata.reflect(bind=engine)

server_model = Base.classes.servers