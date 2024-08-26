from flask import Flask, request, jsonify, g
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
import logging
from db_connection import db 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def authenticate():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email e senha são obrigatórios'}), 400
    
    user = db.query("SELECT * FROM usuarios WHERE email = %s", (email,))
    if not user:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    
    user = user[0]

    if not check_password_hash(user['senha'], password):
        return jsonify({'message': 'Senha incorreta'}), 401
    
    token = jwt.encode({
        'sub': user['id'],
        'user_type': user['tipo_usuario'],
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token}), 200

def token_required(f):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token de acesso é necessário'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            g.current_user_id = data['sub']
            g.current_user_type = data['user_type']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido'}), 401

        return f(*args, **kwargs)
    return decorator

@app.route('/admin_action', methods=['POST'])
@token_required
def admin_action():
    if g.current_user_type != 'admin':
        return jsonify({'message': 'Acesso negado'}), 403
    
    # Código para ação administrativa aqui
    return jsonify({'message': 'Ação administrativa realizada com sucesso'}), 200

@app.teardown_appcontext
def close_db(error):
    if db.connection:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)
