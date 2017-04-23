import os
import json

from flask import Flask, request, abort, jsonify, Response
from werkzeug.local import LocalProxy

from asnlookup_client import ASNClient

def get_asn_client():
    endpoint = os.getenv("ASNLOOKUP_SERVER_ADDR", "tcp://localhost:5555")
    return ASNClient(endpoint)

asn_client = LocalProxy(get_asn_client)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!\n'

@app.route('/health')
def hello_world():
    asn_client.lookup("8.8.8.8")
    return 'ok\n'

@app.route('/lookup')
def lookup():
    ip = request.args.get('ip', '')
    if not ip:
        abort(400)

    resp = asn_client.lookup(ip)
    return jsonify(resp)

@app.route('/lookup_many', methods=['POST'])
def lookup_many():
    f = request.files['ips']
    ips = [line.strip().decode('utf-8') for line in f]
    resp = asn_client.lookup_many(ips)
    def generate():
        for row in resp:
            yield json.dumps(row) + "\n"
    return Response(generate(), mimetype='application/json')

def main():
    app.run()

if __name__ == '__main__':
    main()
