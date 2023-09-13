# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/api/greeting', methods=['GET'])
# def greet():
#     return jsonify(message="Hello from Flask!")

# if __name__ == '__main__':
#     app.run(debug=True)


# from random import randrange

# import flask as flask
# from flask import jsonify

# app = flask.Flask(__name__)


# @app.route('/api/chart_data')
# def getChartData():
#     array = list(map(lambda x: {'x': x, 'y': randrange(20)}, range(10)))
#     return jsonify(array)

from flask import Flask, jsonify, render_template, request 
import pandas as pd
from flask_cors import CORS
import requests
import configparser

app = Flask(__name__)
CORS(app)

@app.route('/api/getChartData', methods=['GET'])
def get_chart_data():
    # Read data from Excel file
    df = pd.read_excel("test_table.xlsx")
    
    # Convert the data to JSON format
    chart_data = df.to_dict(orient="records")
    
    return jsonify(chart_data)


@app.route('/api/getAbout', methods=['GET'])
def get_about_data():
    # Read data from Excel file
    df_about = pd.read_excel("test_about.xlsx")
    
    # Convert the data to JSON format
    about_data = df_about.to_dict(orient="records")
    
    return jsonify(about_data)


@app.route('/api/getTechMeta', methods=['GET'])
def get_tech_meta():
    # Read data from Excel file
    df_techMeta = pd.read_excel("test_techMeta.xlsx")
    
    # Convert the data to JSON format
    about_techMeta = df_techMeta.to_dict(orient="records")
    
    return jsonify(about_techMeta)


@app.route('/api/getDomain', methods=['GET'])
def get_domain():
    # Read data from Excel file
    df_domain = pd.read_excel("test_techDM.xlsx")
    
    # Convert the data to JSON format
    about_domain = df_domain.to_dict(orient="records")
    
    return jsonify(about_domain)


@app.route('/api/getkw', methods=['GET'])
def get_kw():
    # Read data from Excel file
    df_kw = pd.read_excel("test_techKW.xlsx")
    
    # Convert the data to JSON format
    about_kw = df_kw.to_dict(orient="records")
    
    return jsonify(about_kw)

@app.route('/api/getkcnd', methods=['GET'])
def get_kcnd():
    # Read data from Excel file
    df_kcnd = pd.read_excel("test_kcnd.xlsx")
    
    # Convert the data to JSON format
    about_kcnd = df_kcnd.to_dict(orient="records")
    
    return jsonify(about_kcnd)


@app.route('/api/getcomtoppat', methods=['GET'])
def get_comtoppat():
    # Read data from Excel file
    df_comtoppat= pd.read_excel("test_comtoppat.xlsx")
    
    # Convert the data to JSON format
    about_comtoppat = df_comtoppat.to_dict(orient="records")
    
    return jsonify(about_comtoppat)

@app.route('/api/gettopcorepat', methods=['GET'])
def get_topcorepat():
    # Read data from Excel file
    df_topcorepat = pd.read_excel("test_topcorepat.xlsx")
    
    # Convert the data to JSON format
    about_topcorepat = df_topcorepat.to_dict(orient="records")
    
    return jsonify(about_topcorepat)

@app.route('/api/gettechcompare', methods=['GET'])
def get_techcompare():
    # Read data from Excel file
    df_techcompare = pd.read_excel("test_techcompare.xlsx")
    
    # Convert the data to JSON format
    about_techcompare = df_techcompare.to_dict(orient="records")
    
    return jsonify(about_techcompare)



if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
 
