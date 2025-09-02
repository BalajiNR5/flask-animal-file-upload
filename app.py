from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['UPLOAD_FOLDER'] = './uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    filename = file.filename
    file_type = file.content_type
    file_size = len(file.read())
    file.seek(0)  # reset pointer if you want to save later
    return jsonify({
        'filename': filename,
        'filetype': file_type,
        'filesize_bytes': file_size
    })

# Vercel does not run app.run(), just expose `app`
if __name__ != "__main__":
    application = app  # 👈 Expose as "application" for gunicorn/vercel

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
