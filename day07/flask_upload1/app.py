from flask import Flask, render_template, request
import os
from flask_script import Manager
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
manager = Manager(app)

# 设置保存位置
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.path.dirname(__file__), 'uploads')

# 创建文件对象，主要用来设置的上传类型
photos = UploadSet('photos', IMAGES)

# 将上传对象跟app实例完成绑定
configure_uploads(app, photos)
# 配置上传文件大小,siz默认64M，如果设置为None,则按照我们设置的大小'MAX_CONTENT_LENGTH'
patch_request_class(app, size=None)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/uploads/', methods=['GET', 'POST'])
def uploads():
    img_url = None
    if request.method == "POST":
        # 保存文件
        filename = photos.save(request.files['photos'])
        # 获取保存的url
        img_url = photos.url(filename)
    return render_template('index.html', img_url=img_url)


if __name__ == '__main__':
    app.run()
