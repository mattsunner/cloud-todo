import os

from flask import Flask, jsonify


app = Flask(__name__)

@app.get('/')
def index_route():
    return jsonify({"message": "Server is running correctly"})


@app.get('/health')
def health_status():
    try:
        return jsonify({"Server Resposne Code": f"200"})
    except:
        return jsonify({"Server Response Code": "Error Occured"})



if __name__ == '__main__':
    # Development Server
    port = int(os.environ.get('PORT', 5050))
    app.run(debug=True, host='0.0.0.0', port=port)