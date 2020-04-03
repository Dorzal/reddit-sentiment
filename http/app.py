from flask import Flask, request
import DataService 
#serveur Api
app = Flask(__name__)

#appel le service Dataservice en lui passant les arguments reçu dans la route
@app.route('/api/data')
def getData():
    subject = request.args.get('subject')
    DataService.retrieveData(subject)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')