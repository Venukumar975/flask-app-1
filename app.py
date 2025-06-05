from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def info():
    return f"name : venu , ph : 8990998494"

if __name__ == '__main__':
    app.run(debug=True)