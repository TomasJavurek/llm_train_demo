"""Optional local Flask server for the static training playground."""
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=None)

@app.get('/')
def index():
    return send_from_directory('.', 'index.html')

@app.get('/<path:filename>')
def assets(filename):
    if filename not in {'style.css', 'app.js'}:
        return 'Not found', 404
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
