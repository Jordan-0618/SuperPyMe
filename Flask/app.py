import requests
import pymongo
import random

from flask import Flask, render_template, redirect, jsonify, json
from flask_pymongo import PyMongo
from bson import json_util, ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/scraped_tweets"

mongo = PyMongo(app)


@app.route('/')
def home():
    
    ##connect to mongodb to get sample 
    pos_output = []
    for t in mongo.db.tweets.find({"sentiment":"1.0"}):
        pos_output.append({'content':t['content'], 'city':t['city']})
    list_len1 = len(pos_output)
    pos_pick_num = random.randint(0,list_len1)
    random_pos_tweet = pos_output[pos_pick_num]

    neg_output = []
    for t in mongo.db.tweets.find({"sentiment":"-1.0"}):
        neg_output.append({'content':t['content'], 'city':t['city']})
    list_len2 = len(neg_output)
    neg_pick_num = random.randint(0,list_len2)
    random_neg_tweet = neg_output[neg_pick_num]


    return render_template('final_index-with-tableau.html', random_neg_tweet=random_neg_tweet, random_pos_tweet=random_pos_tweet)


@app.route('/scrape')
def scrape():

    pos_output = []
    for t in mongo.db.tweets.find({"sentiment":"1.0"}):
        pos_output.append({'content':t['content'], 'city':t['city']})
    list_len1 = len(pos_output)
    pos_pick_num = random.randint(0,list_len1)
    random_pos_tweet = pos_output[pos_pick_num]

    neg_output = []
    for t in mongo.db.tweets.find({"sentiment":"-1.0"}):
        neg_output.append({'content':t['content'], 'city':t['city']})
    list_len2 = len(neg_output)
    neg_pick_num = random.randint(0,list_len2)
    random_neg_tweet = neg_output[neg_pick_num]

    return redirect('/', code=302)



if __name__ == "__main__":
    app.run(debug=True)