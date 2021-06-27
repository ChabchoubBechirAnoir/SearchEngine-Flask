from flask import Flask , jsonify  , render_template , send_file , url_for ,request
import pymongo
from bson.objectid import ObjectId 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["allInDB"]
mycol = mydb["full"]
app = Flask(__name__)
class MetaData:
  def __init__(self,id,path,tags,family_ht,family_eh):
    self.id = id
    self.path = path
    self.tags = tags
    self.family_ht = family_ht
    self.family_eh = family_eh

@app.route('/search/<tag>/<page>', methods=["GET", "POST"])
def search(tag,page):
    query = {}
    if request.method == "POST":
        tag = request.form.get('tag')
        query = { 'tags': tag }
    print(query)
    page = int(page)
    pics = mycol.find(query)[page*50:(page+1)*50]
    allpics =[]
    for pic in pics: 
        tmp = MetaData(pic["_id"],pic["path"],pic["tags"],pic["family_ht"],pic["family_eh"])
        allpics.append(tmp)
    return render_template('card.html', pics = allpics, page = page, tag = tag)

@app.route('/picture/<id>', methods=["GET", "POST"])
def picture(id):
    myquery = { '_id' : int(id)}
    pics = mycol.find(myquery)
    main =[]
    for pic in pics: 
        tmp = MetaData(pic["_id"],pic["path"],pic["tags"],pic["family_ht"],pic["family_eh"])
        main.append(tmp)    
        innerquery = { "$and" : [ { "family_eh" : tmp.family_eh}, { "family_ht" :  tmp.family_ht} ] }
        pics = mycol.find(innerquery)
    allpics =[]
    for pic in pics: 
        tmp = MetaData(pic["_id"],pic["path"],pic["tags"],pic["family_ht"],pic["family_eh"])
        allpics.append(tmp)
    return render_template('oneresult.html', pics = allpics , main = main)



if __name__ == '__main__':
    app.run(debug=True)