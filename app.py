from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger, swag_from

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

# Configure the PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dishi:root@localhost:5432/db1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = 'item'
    __table_args__ = {'schema': 'my_schema'}
    
    id = db.Column(db.Integer, primary_key=True)
    actualPrice = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String(200), nullable=True)
    eventVenuesID = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(200), nullable=True)
    listingPrice = db.Column(db.Float, nullable=False)
    lock = db.Column(db.Boolean, nullable=False, default=True)
    ordersID = db.Column(db.Integer, nullable=False)
    sellerID = db.Column(db.Integer, nullable=False)
    sellingPrice = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    validatedOn = db.Column(db.String(50), nullable=True)
    verified = db.Column(db.Boolean, nullable=False, default=True)

    def json(self):
        return {
            "actualPrice": self.actualPrice,
            "comment": self.comment,
            "eventVenuesID": self.eventVenuesID,
            "id": self.id,
            "imageUrl": self.imageUrl,
            "listingPrice": self.listingPrice,
            "lock": self.lock,
            "ordersID": self.ordersID,
            "sellerID": self.sellerID,
            "sellingPrice": self.sellingPrice,
            "status": self.status,
            "type": self.type,
            "validatedOn": self.validatedOn,
            "verified": self.verified
        }

class ItemListResource(Resource):
    # get 
    @swag_from({
        'responses': {
            200: {
                'description': 'OK',
                'content': {
                    'application/json': {
                        'example': {
                            "ticket": {
                                "cartTickets": [
                                    {
                                        "actualPrice": 0,
                                        "comment": "string",
                                        "eventVenuesID": 0,
                                        "id": 0,
                                        "imageUrl": "string",
                                        "listingPrice": 0,
                                        "lock": True,
                                        "ordersID": 0,
                                        "sellerID": 0,
                                        "sellingPrice": 0,
                                        "status": "string",
                                        "type": "string",
                                        "validatedOn": "string",
                                        "verified": True
                                    }
                                ]
                            },
                            "message": "cards fetched successfully",
                            "status": "success"
                        }
                    }
                }
            },
            400: {
                'description': 'Bad Request',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "string",
                            "status": "string"
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "string",
                            "status": "string"
                        }
                    }
                }
            }
        }
    })
    def get(self):
        cards = Item.query.all()
        return {
            "ticket": {
                "cartTickets": [item.json() for item in cards]
            },
            "message": "cards fetched successfully",
            "status": "success"
        }, 200

    # post 
    @swag_from({
        'responses': {
            201: {
                'description': 'Created',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "Item created successfully",
                            "status": "success",
                            "ticket": {
                                "id": 0,
                                "actualPrice": 0,
                                "comment": "string",
                                "eventVenuesID": 0,
                                "imageUrl": "string",
                                "listingPrice": 0,
                                "lock": True,
                                "ordersID": 0,
                                "sellerID": 0,
                                "sellingPrice": 0,
                                "status": "string",
                                "type": "string",
                                "validatedOn": "string",
                                "verified": True
                            }
                        }
                    }
                }
            },
            400: {
                'description': 'Bad Request',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "string",
                            "status": "string"
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "string",
                            "status": "string"
                        }
                    }
                }
            }
        }
    })
    def post(self):
        data = request.get_json()
        if not data:
            return {"message": "No input data provided", "status": "fail"}, 400

        required = ['actualPrice', 'eventVenuesID', 'listingPrice', 'ordersID', 'sellerID', 'sellingPrice', 'status', 'type']
        require = [field for field in required if field not in data]
        if require:
            return {"message": "Please provide all the following fields. Missing is :  '{}'".format(', '.join(require)), "status": "fail"}, 400
           

        try:
            new_item = Item(
                actualPrice=data['actualPrice'],
                comment=data.get('comment'),
                eventVenuesID=data['eventVenuesID'],
                imageUrl=data.get('imageUrl'),
                listingPrice=data['listingPrice'],
                lock=data.get('lock', True),
                ordersID=data['ordersID'],
                sellerID=data['sellerID'],
                sellingPrice=data['sellingPrice'],
                status=data['status'],
                type=data['type'],
                validatedOn=data.get('validatedOn'),
                verified=data.get('verified', True)
            )
            
            db.session.add(new_item)
            db.session.commit()
            
            return {
                "message": "Item created successfully",
                "status": "success",
                "ticket": new_item.json()
            }, 201
        except Exception as e:
            db.session.rollback()
            return {"message": str(e), "status": "fail"}, 500

    # delete all  
    @swag_from({
        'responses': {
            200: {
                'description': 'No Content',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "All tickets deleted successfully",
                            "status": "success"
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "An error occurred",
                            "status": "fail"
                        }
                    }
                }
            }
        }
    })
    def delete(self):
        try:
            # Delete all tickets
            db.session.query(Item).delete()
            db.session.commit()
            
            return {"message": "All tickets deleted successfully", "status": "success"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": str(e), "status": "fail"}, 500

class ItemResource(Resource):
    # get 
    @swag_from({
        'responses': {
            200: {
                'description': 'OK',
                'content': {
                    'application/json': {
                        'example': {
                            "actualPrice": 0,
                            "comment": "string",
                            "eventVenuesID": 0,
                            "id": 0,
                            "imageUrl": "string",
                            "listingPrice": 0,
                            "lock": True,
                            "ordersID": 0,
                            "sellerID": 0,
                            "sellingPrice": 0,
                            "status": "string",
                            "type": "string",
                            "validatedOn": "string",
                            "verified": True
                        }
                    }
                }
            },
            400: {
                'description': 'Bad Request',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "Invalid ID",
                            "status": "fail"
                        }
                    }
                }
            },
            404: {
                'description': 'Not Found',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "Item not found",
                            "status": "fail"
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "An error occurred",
                            "status": "fail"
                        }
                    }
                }
            }
        }
    })
    def get(self, id):
        try:
            item = Item.query.get(id)
            if not item:
                return {"message": "Item not found", "status": "fail"}, 404
            else:
                return item.json(), 200
        except Exception as e:
            return {"message": str(e), "status": "fail"}, 500

    # delete request 
    @swag_from({
        'parameters': [
            {
                'name': 'id',
                'in': 'path',
                'type': 'integer',
                'required': 'true',
                'description': 'ID of the ticket to delete'
            }
        ],
        'responses': {
            200: {
                'description': 'Deleted successfully',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "Item deleted successfully",
                            "status": "success"
                        }
                    }
                }
            },
            400: {
                'description': 'Bad Request',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "Invalid ID",
                            "status": "fail"
                        }
                    }
                }
            },
            404: {
                'description': 'Not Found',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "Item not found",
                            "status": "fail"
                        }
                    }
                }
            },
            500: {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'example': {
                            "message": "An error occurred",
                            "status": "fail"
                        }
                    }
                }
            }
        }
    })
    def delete(self, id):
        try:
            item = Item.query.get(id)
            if not item:
                return {"message": "Item not found", "status": "fail"}, 404
                
            db.session.delete(item)
            db.session.commit()

            return {"message": "Item deleted successfully", "status": "success"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": str(e), "status": "fail"}, 500
        
api.add_resource(ItemListResource, '/cart', '/cart/tickets')
api.add_resource(ItemResource, '/cart/tickets/<int:id>')

