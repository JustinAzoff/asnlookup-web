from flask import Flask, request, abort, jsonify
from werkzeug.local import LocalProxy

from asnlookup_client import ASNClient

def get_asn_client():
    endpoint = os.getenv("ASNLOOKUP_SERVER_ADDR", "tcp://localhost:5555")
    return ASNClient(endpoint)

asn_client = LocalProxy(get_asn_client)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/lookup')
def lookup():
    ip = requst.args.get('ip', '')
    if not ip:
        abort(400)

    resp = asn_client.lookup(ip)
    return jsonify(resp)
