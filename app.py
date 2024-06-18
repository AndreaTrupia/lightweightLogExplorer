from flask import Flask, jsonify, request, render_template
import os
# from dotenv import load_dotenv

app = Flask(__name__)
# load_dotenv()
# Percorso alla directory principale dei file
files_directory = os.environ.get('FILES_DIRECTORY')

def list_files_recursive(directory):
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):  # Filtrare solo i file .txt, se necessario
                file_path = os.path.join(root, file)
                files_list.append(file_path)
    return files_list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/files')
def get_files():
    files_list = list_files_recursive(files_directory)
    # Rimuovere il percorso base per inviare solo i nomi dei file al client
    files_list = [os.path.relpath(file, files_directory) for file in files_list]
    return jsonify(files_list)

@app.route('/read_file', methods=['POST'])
def read_file():
    data = request.get_json()
    filename = data.get('filename')
    file_path = os.path.join(files_directory, filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
