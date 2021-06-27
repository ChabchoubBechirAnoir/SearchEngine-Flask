import pandas as pd 
import pymongo
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df = pd.read_csv(r"C:\Users\BechirAnoirChabchoub\Desktop\AIM\mirflickr_1M\ht_descriptors\result.txt",sep=" " ,header=None)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
data = df
kmeans = KMeans(n_clusters=200)
kmeans.fit(data)
y = kmeans.fit_predict(data)
df = pd.DataFrame(y)  
df.to_csv('ht.csv', header=False, index = False)  
df = pd.read_csv(r"C:\Users\BechirAnoirChabchoub\Desktop\AIM\mirflickr_1M\eh_descriptors\result.txt",sep=" " ,header=None)
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
data = df
kmeans = KMeans(n_clusters=200)
kmeans.fit(data)
y1 = kmeans.fit_predict(data)
df = pd.DataFrame(y1)  
df.to_csv('eh.csv', header=False, index = False)  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["allInDB"]
mycol = mydb["full"]
dataToAdd = []
for i in range (1,101):
    dataToAdd = []
    for j in range(10000):
        id = str(j+(i-1)*10000)
        idinc = str(j+1+(i-1)*10000)
        path = "thumbnails/" + str(i-1) + "/" + id + ".jpg"
        tags = [line.rstrip() for line in open("C:/Users/BechirAnoirChabchoub/Desktop/AIM/mirflickr_1M/tags/" + str(i) + "/tags" + idinc + ".txt",encoding="utf8")]
        family_ht = y[j+(i-1)*10000]
        family_eh = y1[j+(i-1)*10000]
        mydict = {
            "_id": j+(i-1)*10000,
            "path": path,
            "tags" : tags,
            "family_ht" : int(family_ht),
            "family_eh" : int(family_eh)
        }
        dataToAdd.append(mydict)
        print(mydict)
    x = mycol.insert_many(dataToAdd) 