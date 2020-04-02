from flask import Flask, request
import DataService 

app = Flask(__name__)

@app.route('/api/data')
def getData():
    subject = request.args.get('subject')
    DataService.retrieveData(subject)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')