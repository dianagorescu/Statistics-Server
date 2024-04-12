"""This module contains routes for the application."""
import json

import logging
from logging.handlers import RotatingFileHandler

from flask import request, jsonify
from app import webserver

# Configure logging with UTC/GMT timestamp
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('webserver.log', maxBytes=1024*1024, backupCount=5)
    ]
)

# Create a logger
logger = logging.getLogger('webserver')


@webserver.route('/api/post_endpoint', methods=['POST'])
def post_endpoint():

    if request.method == 'POST':
        # Assuming the request contains JSON data
        data = request.json

        # Process the received data
        # For demonstration purposes, just echoing back the received data
        response = {"message": "Received data successfully", "data": data}

        # Sending back a JSON response
        return jsonify(response)
    
    # Method Not Allowed
    return jsonify({"error": "Method not allowed"}), 405

@webserver.route('/api/get_results/<job_id>', methods=['GET'])
def get_response(job_id):

    # Invalid job
    if int(job_id) > webserver.job_counter:
        return jsonify({'status': 'error'}), 400

    # Valid and done job
    if int(job_id) in webserver.tasks_runner.done_jobs:

        # Extract the result from the file and send it
        file_path = f"results/job_{job_id}.json"
        with open(file_path, "r", encoding='utf-8') as f:
            result = json.load(f)

        logger.info('Job_id:%s exiting with result: %s', job_id, result)

        return jsonify({'status': 'done', 'data': result}), 200

    # Valid job, but it is still running
    return jsonify({'status': 'running'}), 200

@webserver.route('/api/states_mean', methods=['POST'])
def states_mean_request():
    data = request.json
    logger.info('Entering with parameters: %s', data)

    job_id = webserver.job_counter
    webserver.job_counter += 1

    job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "states_mean" , 
        "question_data" : data['question'],
        "status" : "running"
    }

    webserver.tasks_runner.coada_joburi.put(job_struct)
    return jsonify({"job_id": str(job_id) }), 200

@webserver.route('/api/state_mean', methods=['POST'])
def state_mean_request():
    data = request.json
    logger.info('Entering with parameters: %s', data)

    job_id = webserver.job_counter
    webserver.job_counter += 1

    job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "state_mean" , 
        "question_data" : data['question'],
        "nume_stat" : data['state'],
        "status" : "running"
    }

    webserver.tasks_runner.coada_joburi.put(job_struct)
    return jsonify({"job_id": str(job_id) }), 200


@webserver.route('/api/best5', methods=['POST'])
def best5_request():
    data = request.json
    logger.info('Entering with parameters: %s', data)

    job_id = webserver.job_counter
    webserver.job_counter += 1

    job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "best5" , 
        "question_data" : data['question'],
        "status" : "running"
    }

    webserver.tasks_runner.coada_joburi.put(job_struct)
    return jsonify({"job_id": str(job_id) }), 200

@webserver.route('/api/worst5', methods=['POST'])
def worst5_request():
    data = request.json
    logger.info('Entering with parameters: %s', data)

    job_id = webserver.job_counter
    webserver.job_counter += 1

    job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "worst5" , 
        "question_data" : data['question'],
        "status" : "running"
    }

    webserver.tasks_runner.coada_joburi.put(job_struct)
    return jsonify({"job_id": str(job_id) }), 200

@webserver.route('/api/global_mean', methods=['POST'])
def global_mean_request():
    data = request.json
    logger.info('Entering with parameters: %s', data)

    job_id = webserver.job_counter
    webserver.job_counter += 1

    job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "global_mean" , 
        "question_data" : data['question'],
        "status" : "running"
    }

    webserver.tasks_runner.coada_joburi.put(job_struct)
    return jsonify({"job_id": str(job_id) }), 200

@webserver.route('/api/diff_from_mean', methods=['POST'])
def diff_from_mean_request():
    data = request.json
    logger.info('Entering with parameters: %s', data)

    job_id = webserver.job_counter
    webserver.job_counter += 1

    job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "diff_from_mean" , 
        "question_data" : data['question'],
        "status" : "running"
    }

    webserver.tasks_runner.coada_joburi.put(job_struct)
    return jsonify({"job_id": str(job_id) }), 200

@webserver.route('/api/state_diff_from_mean', methods=['POST'])
def state_diff_from_mean_request():
    data = request.json
    logger.info('Entering with parameters: %s', data)

    job_id = webserver.job_counter
    webserver.job_counter += 1

    job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "state_diff_from_mean" , 
        "question_data" : data['question'],
        "nume_stat" : data['state'],
        "status" : "running"
    }

    webserver.tasks_runner.coada_joburi.put(job_struct)
    return jsonify({"job_id": str(job_id) }), 200

@webserver.route('/api/mean_by_category', methods=['POST'])
def mean_by_category_request():
    data = request.json
    logger.info('Entering with parameters: %s', data)

    job_id = webserver.job_counter
    webserver.job_counter += 1

    job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "mean_by_category" , 
        "question_data" : data['question'],
        "status" : "running"
    }

    webserver.tasks_runner.coada_joburi.put(job_struct)
    return jsonify({"job_id": str(job_id) }), 200

@webserver.route('/api/state_mean_by_category', methods=['POST'])
def state_mean_by_category_request():
    data = request.json
    logger.info('Entering with parameters: %s', data)

    job_id = webserver.job_counter
    webserver.job_counter += 1

    job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "state_mean_by_category" , 
        "question_data" : data['question'],
        "nume_stat" : data['state'],
        "status" : "running"
    }

    webserver.tasks_runner.coada_joburi.put(job_struct)
    return jsonify({"job_id": str(job_id) }), 200

@webserver.route('/api/graceful_shutdown', methods=['GET'])
def graceful_shutdown_response():
    """
    This endpoint makes the application shutdown 
    in order to stop accepting requests
    """
    webserver.tasks_runner.graceful_shutdown()

    return jsonify({"status_server": "shutdown" }), 200


@webserver.route('/api/jobs', methods=['GET'])
def jobs_response():
    """
    This endpoint returns the job_ids up to that moment and their statuses
    """
    result = []
    for job_id in webserver.tasks_runner.coada_joburi.queue:
        if int(job_id) in webserver.tasks_runner.done_jobs:
            result.append({"job_id_{job_id}" : "done"})
        else:
            result.append({"job_id_{job_id}" : "running"})

    return jsonify({"status": "done", "data": result}), 200


@webserver.route('/api/num_jobs', methods=['GET'])
def num_jobs_response():
    """
    This endpoint returns the number of jobs left
    """
    result = webserver.tasks_runner.coada_joburi.qsize() - len(webserver.tasks_runner.done_jobs)

    return jsonify({result}), 200


# You can check localhost in your browser to see what this displays
@webserver.route('/')
@webserver.route('/index')
def index():
    routes = get_defined_routes()
    msg = f"Hello, World!\n Interact with the webserver using one of the defined routes:\n"

    # Display each route as a separate HTML <p> tag
    paragraphs = ""
    for route in routes:
        paragraphs += f"<p>{route}</p>"

    msg += paragraphs
    return msg

def get_defined_routes():
    routes = []
    for rule in webserver.url_map.iter_rules():
        methods = ', '.join(rule.methods)
        routes.append(f"Endpoint: \"{rule}\" Methods: \"{methods}\"")
    return routes
