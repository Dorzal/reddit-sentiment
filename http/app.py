from flask import Flask, request
import DataService 
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def getData():
    subject = request.args.get('sujet')
    return DataService.retrieveData(subject)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')