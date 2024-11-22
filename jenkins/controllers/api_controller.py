from flask import Blueprint, jsonify, session, current_app, request, g

api_bp = Blueprint('api', __name__)

@api_bp.before_request
def load_query():
    form_data = request.form
    g.query = form_data.get('q')
    
    if g.query is  None:
        response = {
            "status_code":      400,
            "error_message":    "Query must be provided"        
        }
        return jsonify(response), 400


@api_bp.route('/api/ask', methods=['POST'])
def ask():
    vdb = current_app.config['VDB']
    vectores = vdb.fetch(q.query)
    response = {
        "q":        g.query,
        "response": "",
        "prompt":   "",
        "vectors":  vectores

    }
    return jsonify(response), 200