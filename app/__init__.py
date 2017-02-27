from flask import Flask

#实例化flask应用
app = Flask(__name__)
# 从config加载配置
app.config.from_object("config")

from app import views, models