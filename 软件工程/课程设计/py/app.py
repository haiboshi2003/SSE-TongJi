import base64
import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from flask import Flask, request, send_from_directory, jsonify, send_file
import os

import sys

# 添加模块所在的目录到Python路径中
module_directory = r'HOG_SVM'
sys.path.append(module_directory)

import cv2
from HOG_SVM import SVM_predict

from detect2 import parse_opt, mymain

app = Flask(__name__)
# 允许所有域的跨域请求
CORS(app)

# MySQL 数据库连接配置
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456789',
    'database': 'glasstest',
}


def save_to_mysql(image_path, column):
    try:
        # 连接到 MySQL 数据库
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 读取图片数据并插入到数据库
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            cursor.execute("INSERT INTO glass ({}) VALUES (%s)".format(column), (image_data,))

        # 提交更改并关闭连接
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error saving to MySQL: {e}")


UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

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
        # 将base64编码的图片数据插入到 MySQL 数据库
        save_to_mysql(image_path, "result")

        # 将base64编码的图片数据放入字典中
        response_data = {
            'imageBase64': encoded_image,
        }

        # 返回JSON响应
        return jsonify(response_data)


@app.route('/svm', methods=['POST'])
def svm_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], 'test1.jpg')
        file.save(filename)
        #svm检测
        SVM_predict.SVM_detect_default('data\\test1.jpg', 1, "detect\\exp\\svmresult.jpg",
                                       'HOG_SVM\\weights\\models.dat')
        # 替换为实际的图片路径
        image_path = 'detect/exp/svmresult.jpg'

        # 读取图片文件并进行base64编码
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        # 将base64编码的图片数据插入到 MySQL 数据库
        save_to_mysql(image_path, "result")

        # 将base64编码的图片数据放入字典中
        response_data = {
            'imageBase64': encoded_image,
        }

        # 返回JSON响应
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='localhost', port=7078)
