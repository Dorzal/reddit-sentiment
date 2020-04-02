from flask import Flask
import DataService 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return DataService.retrieveData()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')