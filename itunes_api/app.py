from flask import Flask,render_template,request
import requests
import urllib.request
import json
import sys

app = Flask(__name__)

@app.route('/appstore',methods=['GET'])
def appstore():
    return render_template('appstore.html',title="appstore検索",message="探したいアプリのキーワードをいれてください")

@app.route('/appstore',methods=['POST'])
def form():
    #itunes APIで検索
    field=request.form['field']
    url = 'https://itunes.apple.com/search?term='
    
    #日本語をurlに変換
    param =  urllib.parse.quote(field)
    
    response = requests.get(url+ param+"&media=software&entity=software&country=jp")
    jsonData = response.json()
    jsonData = jsonData['results']

    return render_template('appstore.html',title="appstore検索",message="検索語句：%s"%field,json_object=jsonData)

if __name__ =='__main__':
    app.run(debug=True)