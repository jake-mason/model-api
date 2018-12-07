'''
Minimal API for providing predictions from a machine learning model
'''

import json
import traceback

from flask import Flask, request, abort
from flask_restful import Api, Resource

from app_utils import create_logger
from app_config import VALID_HTTP_METHODS
from predict import predict

app = Flask(__name__)
api = Api(app)

logger = create_logger()

class Predict(Resource):

	def post(self):
		''' Handle incoming POST requests '''
		try:
			# For tracking times at which calls were submitted
			logger.info('received request')

			json_data = request.get_json(force=True)

			user_agent = str(request.user_agent)
			remote_addr = str(request.remote_addr)

			logger.info('remote_addr: {}, user_agent: {}'.format(remote_addr, user_agent))
			logger.debug(json.dumps(json_data))

			data = json_data[0]

			result = predict(data)

			logger.info('Predicted median price (thousands): {}'.format(result))

			return result, 200
		except:
			logger.error(traceback.format_exc())
			logger.error('Unable to provide prediction')
			return 'Failure!', 400

class Status(Resource):
	def get(self):
		logger.info('Checking if the container is available')
		return 200

# Related to INC8813709
# The security scan saw a 200 status from an OPTIONS reqeust
# Must validate request type prior to proceeding
@app.before_request
def method_check():

	if not request.method in VALID_HTTP_METHODS:
		logger.error('Invalid request type: {}'.format(request.method))
		abort(405)

api.add_resource(Predict, '/predict')
api.add_resource(Status, '/status')

if __name__ == '__main__':

	logger.info('Serving requests')
	app.run('0.0.0.0')