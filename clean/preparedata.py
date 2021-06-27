#tje data is stored using mongodb :D 
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["kmeans"]
mycol = mydb["result"]
dataToAdd = []
htlines = list("feature"+str(i) for i in range(1,44))
ehlines = list("feature"+str(i) for i in range(44,195))
for i in range (1,101):
    dataToAdd = []
    e = open("C:/Users/BechirAnoirChabchoub/Desktop/AIM/mirflickr_1M/eh_descriptors/eh"+str(i)+".txt", "r")
    h = open("C:/Users/BechirAnoirChabchoub/Desktop/AIM/mirflickr_1M/ht_descriptors/ht"+str(i)+".txt", "r")
    for j in range(10000):
        id = str(j+(i-1)*10000)
        idinc = str(j+1+(i-1)*10000)
        path = "thumbnails/" + str(i-1) + "/" + id + ".jpg"
        tags = [line.rstrip() for line in open("C:/Users/BechirAnoirChabchoub/Desktop/AIM/mirflickr_1M/tags/" + str(i) + "/tags" + idinc + ".txt",encoding="utf8")]
        ehline = e.readline()
        htline = h.readline()
        eh_descriptor = ehline.split()
        eh_descriptor = [float(i) for i in eh_descriptor]
        eh_descriptor= dict(zip(ehlines, eh_descriptor))
        ht_descriptor = htline.split()
        ht_descriptor = [float(i) for i in ht_descriptor]
        ht_descriptor= dict(zip(htlines, ht_descriptor))
        mydict = {
            "_id": j+(i-1)*10000,
            "path": path,
            "tags" : tags
        }
        mydict = {**mydict, **eh_descriptor}
        mydict = {**mydict, **ht_descriptor}
        dataToAdd.append(mydict)
        print(id)
    x = mycol.insert_many(dataToAdd)  
    e.close()
    h.close()
    
