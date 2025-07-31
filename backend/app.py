from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__, static_folder='../frontend/dist', static_url_path='/')
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('ecommerce.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        if page < 1 or limit < 1:
            raise ValueError
    except ValueError:
        return jsonify({'error': 'Invalid pagination parameters'}), 400

    offset = (page - 1) * limit

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM products')
    total_count = cursor.fetchone()[0]

    cursor.execute('SELECT * FROM products LIMIT ? OFFSET ?', (limit, offset))
    products = cursor.fetchall()
    conn.close()

    product_list = [dict(row) for row in products]

    response = {
        'total': total_count,
        'page': page,
        'limit': limit,
        'products': product_list
    }

    return jsonify(response), 200

@app.route('/api/products/<id>', methods=['GET'])
def get_product_by_id(id):
    if not id.isdigit():
        return jsonify({'error': 'Invalid product ID format'}), 400

    product_id = int(id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    conn.close()

    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    return jsonify(dict(product)), 200

# Serve React frontend after build
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
