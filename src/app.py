from flask import Flask
from flask_cors import CORS
from config import config

#Routes
from routes import Reservation 

app=Flask(__name__)
CORS(app)

def page_not_found(error):   
    return "<h1>Not found page aa</h1>", 404

if __name__=='__main__':
    app.config.from_object(config['development'])
    
    #Blueprints
    app.register_blueprint(Reservation.main, url_prefix='/api/reservation')

    # Error handlers
    app.register_error_handler(404,page_not_found)
    app.run(host='0.0.0.0', port=5001)
    

    