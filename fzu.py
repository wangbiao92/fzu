# -*- coding: utf-8 -*-
import os
from flask import Flask, request, url_for, send_from_directory, render_template
from werkzeug import secure_filename
# from PIL import Image


# 允许上传的文件类型
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

# 上传的文件路径
app.config['UPLOAD_FOLDER'] = 'upload_img/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # 上传成功返回的网页
            return render_template('index.html')
    # 无上传内容返回的页面          
    return render_template('index.html')

# def change_img_type():
#     img = Image.open("upload_img/eg_planets.jpg")
#     img.save("1.jpeg", format="jpeg")    


if __name__ == '__main__':
    # web服务器在运行时支持调试
    app.run(debug=True)
    change_img_type()