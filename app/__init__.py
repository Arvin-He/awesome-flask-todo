from flask import Flask
from flask_mongoengine import MongoEngine

#实例化flask应用
app = Flask(__name__)
# 从config加载配置
app.config.from_object("config")

db = MongoEngine(app)

from app import views, models