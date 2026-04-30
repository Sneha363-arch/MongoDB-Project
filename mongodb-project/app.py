from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["bigdata"]
collection = db["students"]

# ---------- UI ----------
@app.route("/")
def home():
    return render_template("index.html")


# ---------- BASIC ----------
@app.route("/students")
def get_students():
    page = int(request.args.get("page", 1))
    limit = 20
    skip = (page - 1) * limit

    data = list(collection.find({}, {"_id": 0}).skip(skip).limit(limit))
    total = collection.count_documents({})

    return jsonify({
        "data": data,
        "total": total
    })


# ---------- ANALYTICS ----------
@app.route("/avg")
def avg():
    result = list(collection.aggregate([
        {"$group": {"_id": "$grade", "avg": {"$avg": "$average"}}}
    ]))
    return jsonify(result)


@app.route("/top")
def top():
    result = list(collection.find({}, {"_id": 0}).sort("average", -1).limit(5))
    return jsonify(result)


@app.route("/count-dept")
def count_dept():
    result = list(collection.aggregate([
        {"$group": {"_id": "$dept", "count": {"$sum": 1}}}
    ]))
    return jsonify(result)


# ---------- SEARCH / FILTER ----------
@app.route("/search/<name>")
def search(name):
    result = list(collection.find(
        {"name": {"$regex": name, "$options": "i"}},
        {"_id": 0}
    ))
    return jsonify(result)


@app.route("/filter/<grade>")
def filter_grade(grade):
    result = list(collection.find({"grade": grade.upper()}, {"_id": 0}))
    return jsonify(result)


@app.route("/sort/<order>")
def sort(order):
    direction = -1 if order == "desc" else 1
    result = list(collection.find({}, {"_id": 0}).sort("total", direction))
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)