from flask import Flask
from settei import get_config

app = Flask(__name__)

@app.route("/")
def settings():
    config = get_config('application', 'local')

    return str(config)

if __name__ == "__main__":
    app.run(debug=True)
