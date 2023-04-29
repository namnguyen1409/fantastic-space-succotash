import requests
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def proxy():
    try:
        src = request.args.get('src')
        url = request.args.get('url')

        headers = {
            'referer': url
        }

        r = requests.get(src, headers=headers, stream=True)
        return Response(r.iter_content(chunk_size=1024), content_type=r.headers['content-type'])
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2004)
