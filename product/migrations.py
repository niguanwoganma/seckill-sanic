import sys
from config import load_config
from peewee import MySQLDatabase
from models import Product


config = load_config()

db = MySQLDatabase(**config["DB_CONFIG"])


try:
    db.create_tables([Product])
except Exception as e:
    pass
