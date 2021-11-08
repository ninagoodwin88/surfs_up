from Flask import Flask, jsonify

# # from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello world'


app = Flask(__name__)
@app.route("/welcome")
def welcome():
    return ('''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

if __name__ == "__main__":
    app.run(debug=True)    