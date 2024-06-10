from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="tixito_db",
            user="postgres",
            password="345483",
            host="localhost"
        )
        return conn
    except psycopg2.OperationalError as e:
        app.logger.error(f"Operational error: {e}")
        return None
    except Exception as e:
        app.logger.error(f"General error: {e}")
        return None

@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Bad Request: No data provided", "status_code": 400}), 400

    actualPrice = data.get('actualPrice', 0)
    comment = data.get('comment', '')
    eventVenuesID = data.get('eventVenuesID', 0)
    imageURL = data.get('imageURL', '')
    listingPrice = data.get('listingPrice', 0)
    lock = data.get('lock', False)
    ordersID = data.get('ordersID', 0)
    sellerID = data.get('sellerID', 0)
    sellingPrice = data.get('sellingPrice', 0)
    status = data.get('status', '')
    type = data.get('type', '')
    validatedOn = data.get('validatedOn')
    verified = data.get('verified', False)

    if not sellerID:
        return jsonify({"error": "Unauthorized: No seller ID provided", "status_code": 401}), 401

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed", "status_code": 500}), 500

    cursor = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cursor.execute("""
            INSERT INTO tickets (actualPrice, comment, eventVenuesID, imageURL, listingPrice, lock, ordersID, sellerID, sellingPrice, status, type, validatedOn, verified)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;
        """, (actualPrice, comment, eventVenuesID, imageURL, listingPrice, lock, ordersID, sellerID, sellingPrice, status, type, validatedOn, verified))

        new_ticket = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        if new_ticket:
            return jsonify({"data": new_ticket, "status_code": 201}), 201
        else:
            return jsonify({"error": "No Content: Ticket creation failed", "status_code": 204}), 204
    except Exception as e:
        app.logger.error(f"Error inserting ticket: {e}")
        conn.rollback()
        cursor.close()
        conn.close()
        return jsonify({"error": str(e), "status_code": 400}), 400


@app.route('/tickets', methods=['GET'])
def get_tickets():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed", "status_code": 500}), 500

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute('SELECT * FROM tickets;')
        tickets = cursor.fetchall()
        cursor.close()
        conn.close()

        if not tickets:
            return jsonify({"message": "No Content: No tickets found", "status_code": 204}), 204

        return jsonify({"data": {"tickets": tickets}, "message": "success", "status": "ok", "status_code": 200}), 200
    except Exception as e:
        app.logger.error(f"Error fetching tickets: {e}")
        cursor.close()
        conn.close()
        return jsonify({"error": str(e), "status_code": 500}), 500


@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket_by_id(ticket_id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed", "status_code": 500}), 500

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute('SELECT * FROM tickets WHERE id = %s;', (ticket_id,))
        ticket = cursor.fetchone()
        cursor.close()
        conn.close()

        if ticket:
            return jsonify({"data": ticket, "status_code": 200}), 200
        else:
            return jsonify({"error": "Ticket not found", "status_code": 404}), 404
    except Exception as e:
        app.logger.error(f"Error fetching ticket by ID: {e}")
        cursor.close()
        conn.close()
        return jsonify({"error": str(e), "status_code": 500}), 500


@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket_by_id(ticket_id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed", "status_code": 500}), 500

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute('DELETE FROM tickets WHERE id = %s RETURNING *;', (ticket_id,))
        deleted_ticket = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        if deleted_ticket:
            return jsonify({"message": "Ticket deleted successfully", "data": deleted_ticket, "status_code": 200}), 200
        else:
            return jsonify({"error": "Ticket not found", "status_code": 404}), 404
    except Exception as e:
        app.logger.error(f"Error deleting ticket by ID: {e}")
        conn.rollback()
        cursor.close()
        conn.close()
        return jsonify({"error": str(e), "status_code": 500}), 500


@app.route('/tickets/<int:ticket_id>/price', methods=['PATCH'])
def update_ticket_price(ticket_id):
    data = request.get_json()

    if not data or 'price' not in data:
        return jsonify({"error": "Bad Request: 'price' not provided", "status_code": 400}), 400

    new_price = data['price']

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed", "status_code": 500}), 500

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute('UPDATE tickets SET sellingPrice = %s WHERE id = %s RETURNING *;', (new_price, ticket_id))
        updated_ticket = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        if updated_ticket:
            return jsonify({"message": "Ticket price updated successfully", "data": updated_ticket, "status_code": 200}), 200
        else:
            return jsonify({"error": "Ticket not found", "status_code": 404}), 404
    except Exception as e:
        app.logger.error(f"Error updating ticket price: {e}")
        conn.rollback()
        cursor.close()
        conn.close()
        return jsonify({"error": str(e), "status_code": 500}), 500


@app.route('/tickets/<int:ticket_id>/validate', methods=['PATCH'])
def validate_ticket(ticket_id):
    data = request.get_json()

    if not data or 'validatedOn' not in data:
        return jsonify({"error": "Bad Request: 'validatedOn' not provided", "status_code": 400}), 400

    validatedOn = data['validatedOn']

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed", "status_code": 500}), 500

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute('UPDATE tickets SET validatedOn = %s WHERE id = %s RETURNING *;', (validatedOn, ticket_id))
        updated_ticket = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        if updated_ticket:
            return jsonify({"message": "Ticket validated successfully", "data": updated_ticket, "status_code": 200}), 200
        else:
            return jsonify({"error": "Ticket not found", "status_code": 404}), 404
    except Exception as e:
        app.logger.error(f"Error validating ticket: {e}")
        conn.rollback()
        cursor.close()
        conn.close()
        return jsonify({"error": str(e), "status_code": 500}), 500


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not Found", "status_code": 404}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal Server Error", "status_code": 500}), 500

if __name__ == '__main__':
    app.run(debug=True)
