# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None
# add your model's MetaData object here
# for 'autogenerate' support
from app.database import Base, SQLALCHEMY_DATABASE_URL
target_metadata = Base.metadata

# Set the database URL
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
