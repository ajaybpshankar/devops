from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h2>Registration Page</h2>
        <form method="POST" action="/register">
            Name: <input type="text" name="name"/>
            <input type="submit"/>
        </form>
    '''

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    return f"Welcome {name}, registration successful!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
