from flask import Flask,render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def route_homepage():
    return ('<h1>Hello, world!</h1>')

@app.route('/it', methods=['GET'])
def route_homepage_it():
    return ('<h1>Ciao, Mondo!</h1>')

@app.route('/benvenuto', methods=['GET'])
def route_benvenuto():
    return render_template('benvenuto.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)