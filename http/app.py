from flask import Flask, request
import DataService 

app = Flask(__name__)

@app.route('/api/data')
def getData():
    subject = request.args.get('subject')
    if(subject):
        return subject
    else:
        return 'rien'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')