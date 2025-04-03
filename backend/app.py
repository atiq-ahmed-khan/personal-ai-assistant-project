from flask import Flask, jsonify
from logger import setup_logger

app = Flask(__name__)
logger = setup_logger()

@app.route('/welcome', methods=['GET'])
def welcome():
    logger.info("Welcome endpoint accessed")
    return jsonify({'message': 'Welcome to the AI Assistant!'})

if __name__ == '__main__':
    app.run(debug=True)
