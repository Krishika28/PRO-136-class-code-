from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route('/')
def all_Planet_Data():
    return jsonify({
        "planet_data": data,
        "message": "success"
    })

@app.route('/planet')
def planet_data(): 
    name = request.args.get("planet_name")
    planet_info = next(item for item in data if item["name"]==name)
    return jsonify({
        "data": planet_info,
        "message": "success"
    })

if __name__=='__main__':
    app.run(debug=True)