# Observatory Service

# Import framework
from flask import Flask, request, render_template, Response
from flask_restful import Resource, Api
from flask import abort, make_response, jsonify
import time
from timeit import default_timer as timer
from json2table import convert
import json
import logging

from flaskr.search_food_items import FoodMenu

logger = logging.getLogger(__name__)

# Instantiate the app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
api = Api(app)

class TacoTime(Resource):
    def get(self):
        return {
            'Tacos': ["7-Layer Burrito",
                "Beefy 5-Layer Burrito",
                "Beefy Fritos® Burrito",
                "Beefy Mini Quesadilla"
            ]
        }

# Create routes
api.add_resource(TacoTime, '/')

@app.route("/home")
def home():
    return 'Its Taco Time!'

@app.route('/get_menu_items', methods=['GET'])
def get_menu_items():
    # retrieve and validate required parameters from request
    item_type = request.args.get('item_type')
    keyword_search = request.args.get('keyword_search')
    names_only = request.args.get('names_only')
    if not item_type:
        abort(make_response(jsonify(status='error',
                                    message='Missing item_type'), 400))
    if not keyword_search:
        abort(make_response(jsonify(status='error',
                                    message='Missing keyword_search'), 400))
    if not names_only:
        abort(make_response(jsonify(status='names_only: True or False',
                                    message='Missing site_id'), 400))

    food_menu = FoodMenu(item_type)
    food_items = food_menu.search_items(keyword_search, names_only)
    return jsonify(data=food_items, category="success", status=200)
#
# @app.route('/get_item_by_health_indicator', methods=['GET'])
# def get_item_by_health_indicator():
#     start = timer()
#     # retrieve and validate required parameters from request
#     item_type = request.args.get('item_type')
#     keyword_search = request.args.get('keyword_search')
#     indicator = request.args.get('indicator')
#     high_low = request.args.get('high_low', default='low')
#     if not item_type:
#         abort(make_response(jsonify(status='error',
#                                     message='Missing item_type'), 400))
#     if not keyword_search:
#         abort(make_response(jsonify(status='error',
#                                     message='Missing keyword_search'), 400))
#     if not indicator:
#         abort(make_response(jsonify(status='names_only: True or False',
#                                     message='Missing site_id'), 400))
#
#     food_menu = FoodMenu(item_type)
#     food_items = food_menu.healthy_item(keyword_search, indicator, high_low)
#     return jsonify(data=food_items, category="success", status=200)

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)