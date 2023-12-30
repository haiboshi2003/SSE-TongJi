import base64

from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from flask import Flask, request, send_from_directory, jsonify,send_file
import os
from detect2 import parse_opt,mymain


app = Flask(__name__)
# 允许所有域的跨域请求
CORS(app)
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400s

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], 'test1.jpg')
        file.save(filename)
        opt = parse_opt()
        mymain(opt)
        # 替换为实际的图片路径
        image_path = 'detect/exp/test1.jpg'

        # 读取图片文件并进行base64编码
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        # 将base64编码的图片数据放入字典中
        response_data = {
            'imageBase64': encoded_image,
        }

        # 返回JSON响应
        return jsonify(response_data)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(host='localhost', port=7078)
