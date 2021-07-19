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
        neg_output.append({'content':t['content']})
    list_len2 = len(neg_output)
    neg_pick_num = random.randint(0,list_len2)
    random_neg_tweet = neg_output[neg_pick_num]

    neutral_output = []
    for t in mongo.db.tweets.find({'sentiment':'0.0'}):
        neutral_output.append({'content':t['content']})
    list_len3 = len(neutral_output)
    neutral_pick_num = random.randint(0,list_len3)
    random_neutral_tweet = neutral_output[neutral_pick_num]

    return render_template('final_index.html', random_neg_tweet=random_neg_tweet, random_pos_tweet=random_pos_tweet)


@app.route('/scrape')
def scrape():

   

    return 



if __name__ == "__main__":
    app.run(debug=True)