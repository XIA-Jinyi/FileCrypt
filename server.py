from flask import Flask, send_from_directory, request, jsonify
import pathlib
import base64


app = Flask('FileCrypt')


@app.route('/upload', methods=['PUT'])
def backup():
    try:
        path = request.json['path']
        data = request.json['data']
        file_path = pathlib.Path('backup') / pathlib.Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        data = base64.b64decode(data)
        with file_path.open('wb') as f:
            f.write(data)
        return jsonify(None), 200
    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)}), 400


@app.route('/availability', methods=['GET'])
def test():
    return jsonify(True), 200


@app.route('/download', methods=['PUT'])
def restore():
    try:
        path = request.json['path']
        file_path = pathlib.Path('backup') / pathlib.Path(path)
        with file_path.open('rb') as f:
            data = f.read()
        data = base64.b64encode(data).decode()
        return jsonify({'data': data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404


def main():
    app.run('0.0.0.0', port=3000)


if __name__ == '__main__':
    main()
