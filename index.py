import sqlite3
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flasgger import Swagger


app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

DATABASE = 'banks.db'

conn = sqlite3.connect(DATABASE, check_same_thread=False)

@app.route('/healthcheck')
def health():
    return jsonify({"message":'ok'})

# Route to get all banks
@app.route('/banks', methods=['GET'])
def get_banks():
    """
    Get all banks
    ---
    responses:
      200:
        description: A list of banks
        schema:
          id: Banks
          properties:
            id:
              type: integer
              description: The bank ID
            name:
              type: string
              description: The name of the bank
    """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM banks')
    banks = cursor.fetchall()
    bank_list = [{'id': bank[0], 'name': bank[1]} for bank in banks]
    return jsonify(bank_list)

# Route to get a specific branch by IFSC code
@app.route('/branches/<string:ifsc>', methods=['GET'])
def get_branch(ifsc):
    """
    Get branch details by IFSC code
    ---
    parameters:
      - name: ifsc
        in: path
        type: string
        required: true
        description: IFSC code of the branch
    responses:
      200:
        description: Branch details
        schema:
          id: Branch
          properties:
            ifsc:
              type: string
              description: The IFSC code of the branch
            branch:
              type: string
              description: The name of the branch
            address:
              type: string
              description: The address of the branch
            city:
              type: string
              description: The city of the branch
            district:
              type: string
              description: The district of the branch
            state:
              type: string
              description: The state of the branch
            bank:
              type: object
              description: The bank details
              properties:
                id:
                  type: integer
                  description: The ID of the bank
                name:
                  type: string
                  description: The name of the bank
      404:
        description: Branch not found
    """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM branches WHERE ifsc = ?', (ifsc,))
    branch = cursor.fetchone()
    if not branch:
        abort(404, description=f"Branch with IFSC '{ifsc}' not found")
    
    branch_details = {
        'ifsc': branch[0],
        'branch': branch[2],
        'address': branch[3],
        'city': branch[4],
        'district': branch[5],
        'state': branch[6],
        'bank': {
            'id': branch[1],
            'name': get_bank_name(branch[1])
        }
    }
    return jsonify(branch_details)

# Helper function to get bank name from bank_id
def get_bank_name(bank_id):
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM banks WHERE id = ?', (bank_id,))
    bank_name = cursor.fetchone()[0]
    return bank_name

if __name__ == '__main__':
    # Connect to SQLite database
    app.run(debug=True)