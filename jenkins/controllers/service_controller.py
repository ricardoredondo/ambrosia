from flask import Blueprint, jsonify, session, current_app, request, g

service_bp = Blueprint('service', __name__)

@service_bp.route('/status', methods=['GET'])
def status():
    print(current_app.config['VERSION'])
    
    response = { 
        "msg": "Up And Running",
        "version": current_app.config['VERSION']
        }
    return jsonify(response), 200