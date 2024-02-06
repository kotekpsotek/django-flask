from flask import Flask, jsonify, render_template, redirect
app = Flask(__name__, template_folder="./template")

def output():
    sr = """
        HI from Python Flask. The simpliest manner to create HTTP convinient app in python
    """
    return sr

@app.route("/")
def main():
    return output()

@app.post("/json-content")
def json_content():
    cd = { 'name': "Michał", "age": "Not disclosed" }
    return jsonify(cd), 202 # 204 is tricky

@app.get("/html")
def template_content():
    return render_template("index.html")

@app.get("/redirect")
def redirect_p():
    return redirect("/html")

if __name__ == "__main__":
    print("Server is running")
    app.debug = True # Turn on reload on each edition
    app.run(host='0.0.0.0', port="8080")