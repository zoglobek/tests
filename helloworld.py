from flask import Flask, Response
import cowsay
import io
from contextlib import redirect_stdout

app = Flask(__name__)

@app.route('/')
def hello():
    f = io.StringIO()
    with redirect_stdout(f):
        cowsay.cow("Hello, World!")
    output = f.getvalue()
    
    return f"""
    <html>
        <head><title>Cowsay Hello</title></head>
        <body style="background-color: #121212; color: #00ff00; padding: 20px;">
            <pre>{output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
