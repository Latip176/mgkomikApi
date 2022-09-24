from flask import Flask, request, jsonify, url_for, redirect
from data.scrap import *

app = Flask(__name__)

@app.route("/")
def pengalihan():
    return redirect(url_for("getApi"))

@app.route('/api/komik/', methods=['GET','POST'])
def getApi():
    if request.method=="GET":
        key = request.args.get("judul")
        if(key):
            req = serachKomik(key).request("https://mgkomik.com/?s={}&post_type=wp-manga".format(key))
            if(req['jumlah-hasil-pencarian']==0):
                return jsonify({"data-info":"Hasil pencarian tidak ditemukan!","jumlah-hasil-pencarain":0})
            else:
                return jsonify(req)
        else:
            return jsonify({"error":"Search dulu bang, contoh /api/komik/?judul=test"})
    else:
        return jsonify({"error":"Pake method get bang jangan method post"})

if __name__=="__main__":
    app.run()