from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index_takesi.html')

if __name__ == "__main__":
    app.run()