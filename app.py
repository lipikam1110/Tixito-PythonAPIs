from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from datetime import datetime


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "CRUD API"})


app = Flask(__name__)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

#PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mohin123@localhost:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=True)

# Define Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=True)
    user_id = db.Column(db.Integer, nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.String(500), nullable=False)
    age_criteria = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

'''
# GET endpoint
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'description': item.description} for item in items])

# POST endpoint
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data.get('description'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id, 'name': new_item.name, 'description': new_item.description}), 201

# PUT endpoint 
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = Item.query.get_or_404(item_id)
    item.name = data['name']
    item.description = data.get('description', item.description)
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description})

# DELETE endpoint 
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return '', 204
'''

#Endpoint for review-----------------------------------------------------
@app.route('/review', methods=['POST'])
@app.route('/review', methods=['POST'])
def create_review():
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'message': 'No input data provided',
                'status': 'error'
            }), 400

        if 'orderId' not in data or 'rating' not in data or 'reviews' not in data or 'userID' not in data:
            return jsonify({
                'message': 'Missing required parameters',
                'status': 'error'
            }), 400

        new_review = Review(
            order_id=data['orderId'],
            rating=data['rating'],
            review=data['reviews'],
            user_id=data['userID']
        )

        db.session.add(new_review)
        db.session.commit()

        return jsonify({
            'data': {
                'id': new_review.id,
                'orderId': new_review.order_id,
                'rating': new_review.rating,
                'reviews': new_review.review,
                'userID': new_review.user_id
            },
            'message': 'Review created successfully',
            'status': 'success'
        }), 201

    except Exception as e:
        return jsonify({
            'message': str(e),
            'status': 'error'
        }), 500
    
@app.route('/review', methods=['POST'])
def get_review():
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'message': 'No input data provided',
                'status': 'error'
            }), 400

        if 'orderId' not in data or 'rating' not in data or 'reviews' not in data or 'userID' not in data:
            return jsonify({
                'message': 'Missing required parameters',
                'status': 'error'
            }), 400

        new_review = Review(
            order_id=data['orderId'],
            rating=data['rating'],
            review=data['reviews'],
            user_id=data['userID']
        )

        db.session.add(new_review)
        db.session.commit()

        return jsonify({
            'data': {
                'id': new_review.id,
                'orderId': new_review.order_id,
                'rating': new_review.rating,
                'reviews': new_review.review,
                'userID': new_review.user_id
            },
            'message': 'Review created successfully',
            'status': 'success'
        }), 201

    except Exception as e:
        return jsonify({
            'message': str(e),
            'status': 'error'
        }), 500

@app.route('/review/user/<int:id>', methods=['GET'])
def get_user_reviews(id):
    try:
        if not isinstance(id, int):
            return jsonify({
                'message': 'Invalid user ID',
                'status': 'error'
            }), 400

        reviews = Review.query.filter_by(user_id=id).all()
        if not reviews:
            return jsonify({
                'message': 'No reviews found for the user',
                'status': 'error'
            }), 404

        user_reviews = [{
            'id': review.id,
            'orderID': review.order_id,
            'rating': review.rating,
            'reviews': review.review,
            'userID': review.user_id
        } for review in reviews]

        return jsonify({
            'data': {
                'userReviews': user_reviews
            },
            'message': 'User reviews retrieved successfully',
            'status': 'success'
        }), 200

    except Exception as e:
        return jsonify({
            'message': str(e),
            'status': 'error'
        }), 500

# POST endpoint for event----------------------------------------------------------------------
@app.route('/event', methods=['POST'])
def create_event():
    data = request.get_json()
    new_event = Event(
        about=data['about'],
        age_criteria=data['ageCriteria'],
        category=data['category'],
        city=data['city'],
        duration=data['duration'],
        language=data['language'],
        name=data['name'],
        time=datetime.strptime(data['time'], '%Y-%m-%dT%H:%M:%S.%fZ')
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({
        'id': new_event.id,
        'about': new_event.about,
        'ageCriteria': new_event.age_criteria,
        'category': new_event.category,
        'city': new_event.city,
        'duration': new_event.duration,
        'language': new_event.language,
        'name': new_event.name,
        'time': new_event.time.isoformat() + 'Z'
    }), 201

# GET endpoint to retrieve all events
@app.route('/event', methods=['GET'])
def get_events():
    events = Event.query.all()
    event_list = [
        {
            'id': event.id,
            'about': event.about,
            'ageCriteria': event.age_criteria,
            'category': event.category,
            'city': event.city,
            'duration': event.duration,
            'language': event.language,
            'name': event.name,
            'time': event.time.isoformat() + 'Z'
        }
        for event in events
    ]
    return jsonify({'events': event_list, 'message': 'Events retrieved successfully', 'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)