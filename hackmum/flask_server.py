import time
from flask import Flask, Response

app = Flask(__name__)
with open(__file__) as f:
    data = f.read()

N_CHUNKS = len(data) / 100

@app.route('/read', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    def generate():
        start = 0
        end = start
        while True:
            end = start + int(N_CHUNKS)
            if end > len(data):
                end = None
            message = data[start:end]
            if message:
                yield message
                time.sleep(0.087/N_CHUNKS)
                start = end
                if start is None:
                    break
            else:
                break

    return Response(generate())


if __name__ == '__main__':
    app.run(threaded=True)

