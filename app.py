from sqlalchemy import create_engine
from flask import Flask, render_template, jsonify
from config import username, password, hostname, port, db
import pandas as pd

# username = "postgres"
# password = "2d9c92d9c9"
# hostname = "localhost"
# port = "5432"
# db = "project_3"



app = Flask(__name__)


engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db}')


@app.route("/api/v1.0/iris")
def iris():
    conn = engine.connect()
    query = "SELECT * FROM iris"
    df = pd.read_sql(query, conn)
    print(df)
    return df.to_json(orient="records")

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    # TO DO - get data from database
    # TO DO - pass data  to clean using sql query 
    # CONVERT TO A BUNCH OF LISTS 

    # SEND TO DASHBOARD.HTML
    data = {
        "width": [1,2,2,3,4,5],
        "length": [10,20,30,40,50,60],
    }

    name = "Drew"
    return render_template("dashboard.html", petals=data, name=name)


# @app.route("/api/v1.0/sumpetals")
# def sumpetaliris():
#     conn = engine.connect()
#     query = "SELECT SUM(petalwidthcm) as petalwidth, SUM(petallengthcm) as petallength FROM iris"
#     df = pd.read_sql(query, conn)
#     return df.to_json(orient="records")


if __name__ == "__main__":
    app.run(debug=True)