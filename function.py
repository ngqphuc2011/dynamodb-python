from flask import Flask
from flask import render_template, request, redirect
import boto3
import json


app = Flask(__name__)


@app.route("/")
def index():
    client = boto3.client("lambda")
    respond = client.invoke(
        FunctionName="movieFunction",
        InvocationType="RequestResponse",
        Payload=json.dumps({
            "action": "readall"
        }).encode("utf-8")
    )
    res = json.loads(respond["Payload"].read())
    return render_template("index.html", res=res)


@app.route("/movie/<movieDetail>")
def movieDetail(movieDetail):
    client = boto3.client("lambda")
    detail = movieDetail.split("+")

    y = detail[1].split(".")
    year = int(y[0])
    title = detail[0]

    respond = client.invoke(
        FunctionName="movieFunction",
        InvocationType="RequestResponse",
        Payload=json.dumps({
            "action": "read",
            "key": {
                "year": year,
                "title": title
            }
        }).encode("utf-8")
    )
    res = json.loads(respond["Payload"].read())
    return render_template("movie-detail.html", res=res)


@app.route("/add-movie", methods=['GET', 'POST'])
def addMovie():
    client = boto3.client("lambda")
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        actors = request.form['actors']
        directors = request.form['directors']
        genres = request.form['genres']
        plot = request.form['plot']
        rank = request.form['rank']
        rating = request.form['rating']

        respond = client.invoke(
            FunctionName="movieFunction",
            InvocationType="RequestResponse",
            Payload=json.dumps({
                "action": "create",
                "item": {
                    "year": int(year),
                    "title": title,
                    "info": {
                        "directors": directors,
                        "rating": int(rating),
                        "genres": genres,
                        "plot": plot,
                        "rank": int(rank),
                        "actors": actors
                    }
                }
            }).encode("utf-8")
        )
        res = json.loads(respond["Payload"].read())
        print(res)
        return redirect("/")

    return render_template("add-movie.html")


@app.route("/delete-movie/<movieDetail>")
def deleteMovie(movieDetail):
    client = boto3.client("lambda")
    detail = movieDetail.split("+")

    y = detail[1].split(".")
    year = int(y[0])
    title = detail[0]

    respond = client.invoke(
        FunctionName="movieFunction",
        InvocationType="RequestResponse",
        Payload=json.dumps({
            "action": "delete",
            "key": {
                "year": year,
                "title": title
            }
        }).encode("utf-8")
    )
    res = json.loads(respond["Payload"].read())
    print(res)

    return redirect("/")


@app.route("/edit-movie", methods=['GET', 'POST'])
def editMovie():
    client = boto3.client("lambda")

    if request.method == 'GET':
        respond = client.invoke(
            FunctionName="movieFunction",
            InvocationType="RequestResponse",
            Payload=json.dumps({
                "action": "read",
                "key": {
                    "year": 0,
                    "title": "a"
                }
            }).encode("utf-8")
        )
        res = json.loads(respond["Payload"].read())
        return render_template("edit-movie.html", res = res, req = request)

    if request.method == 'POST':
        y = request.form['year'].split(".")
        year = int(y[0])
        print(year)
        
        title = request.form['title']
        actors = request.form['actors']
        directors = request.form['directors']
        genres = request.form['genres']
        plot = request.form['plot']
        rk = int(request.form['rank'])
        rating = int(request.form['rating'])

        respond = client.invoke(
            FunctionName="movieFunction",
            InvocationType="RequestResponse",
            Payload=json.dumps({
                "action": "update",
                "key": {
                    "year": year,
                    "title": title 
                },
                "updateExpression": "set info.rating = :r, info.directors = :d, info.genres = :g, info.plot = :p, info.#ir = :rk, info.actors = :a",
                "expressionAttributeNames": {
                    "#ir": "rank"
                },
                "expressionAttributeValues": {
                    ":r": rating,
                    ":d": directors,
                    ":g": genres,
                    ":p": plot,
                    ":rk": rk,
                    ":a": actors
                },
                "returnValues": "UPDATED_NEW"
            }).encode("utf-8")
        )
        res = json.loads(respond["Payload"].read())
        return redirect("/")
    return render_template("edit-movie.html")
