from flask import Flask, jsonify, request
from constants import DATA_DIR
from utils import get_data, get_data_by_query

app = Flask(__name__)


@app.post("/perform_query")
def perform_query():
    """
    Gets a query both from JSON or address line and uses it to filter file data.
    :return: filtered data as JSON
    """
    req_data = dict(request.args)  # get query from address line
    # req_data = request.get_json()  # get query from JSON

    try:
        file_data = get_data(f'{DATA_DIR}/{req_data["file_name"]}')
        result = get_data_by_query(req_data, file_data)

    except FileNotFoundError:
        return 'File not found', 400

    except KeyError:
        return 'Request is wrong. Query key(s) not allowed', 400

    except (ValueError, IndexError, TypeError):
        return 'Request is wrong. Query value(s) not allowed', 400

    return result, 200


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
