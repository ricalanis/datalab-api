"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, Response

import geo
import tools
import json

app = Flask(__name__, static_url_path='/static')

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response

app.after_request(add_cors_headers)

@app.route('/get_near_points', methods=['GET'])
def files():
    longitude = float(request.args.get('longitude'))
    latitude = float(request.args.get('latitude'))
    mode = request.args.get('mode')
    head = int(request.args.get('head'))
    near_points = geo.nearest_response(longitude, latitude, mode, head)
    response = tools.format_response(longitude, latitude, mode, head, near_points)
    text_response = json.dumps(response).replace('": NaN','": "NaN"')
    return Response(text_response, mimetype='application/json')


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.after_request(add_cors_headers)
    app.run(threaded=True, host='0.0.0.0', debug=True)
