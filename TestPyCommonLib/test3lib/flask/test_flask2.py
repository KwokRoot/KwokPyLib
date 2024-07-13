from flask import Flask, request, send_file, jsonify, send_from_directory
import os

# 上传，浏览器访问：http://ip:8080
# 查看，浏览器访问：http://ip:8080/list
# 下载，浏览器访问：http://ip:8080/uploads/文件名

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file[]')
        uploaded_files = []
        for file in files:
            if file:
                filename = file.filename
                file.save(os.path.join('uploads', filename))
                uploaded_files.append(filename)
        return ', '.join(uploaded_files) + ' uploaded successfully.'
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>File Upload</h1>
    <form action="/" method="post" enctype="multipart/form-data">
        <input type="file" name="file[]" multiple>
        <input type="submit" value="Upload">
    </form>
</body>
</html>
    '''


@app.route('/list', methods=['GET'])
def list_files():
    files = os.listdir('uploads')
    return jsonify({'files': files})


@app.route('/uploads/<filename>')
def get_file(filename):
    return send_file(os.path.join('uploads', filename), as_attachment=True)


# 设置文件目录
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(host='0.0.0.0', port=8080, debug=True)

