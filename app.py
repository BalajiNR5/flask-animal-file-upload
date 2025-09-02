from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
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
    file.seek(0)  # Reset pointer if you want to save the file later
    # Optionally save the file: file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({
        'filename': filename,
        'filetype': file_type,
        'filesize_bytes': file_size
    })

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])


