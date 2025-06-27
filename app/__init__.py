from flask import Flask
from .db import init_mysql

def create_app():
    app = Flask(__name__)
    
    # Conexión a MySQL
    mysql = init_mysql(app)
    
    # Importar rutas
    from .routes import main
    app.register_blueprint(main)
    
    app.mysql = mysql
    return app
