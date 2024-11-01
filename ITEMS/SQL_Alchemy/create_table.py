import sqlalchemy as db
from create_db import host, password, user, database, port
# Defining the Engine

engine = db.create_engine("sqlite:///users.db", echo=True)

# Create the Metadata Object
metadata_obj = db.MetaData()

# Define the profile table

profile = db.Table(
    'profile',
    metadata_obj,
    db.Column('email', db.String, primary_key=True),
    db.Column('name', db.String),
    db.Column('contact', db.Integer),
)

# Create the profile table
metadata_obj.create_all(engine)