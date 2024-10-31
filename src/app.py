from flask import Flask, jsonify 
from flask_migrate import Migrate
from models import db  # Importa solo db desde models
from routes import api_bp  # Importa las rutas

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starwars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  
migrate = Migrate(app, db)


app.register_blueprint(api_bp, url_prefix='/api')

@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Not Found", message=str(e)), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify(error="Internal Server Error", message=str(e)), 500

def create_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
