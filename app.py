from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ne-sunariz')
def ne_sunariz():
    return render_template("ne_sunariz.html")

@app.route('/iletisim')
def iletisim():
    return render_template("iletisim.html")

if __name__ == '__main__':
    app.run(debug=True)
