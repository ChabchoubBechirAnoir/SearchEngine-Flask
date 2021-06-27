# Search Engine
Searching in 1M Pictures |


#
## Bechir Anoir Chabchoub

 |
| --- | --- |

This project consists of building a search engine using one million pictures.

The input I got before starting this project is:

-A database of 1 million pictures (Thumbnails)

-EH Descriptors: every picture has a vector of features

-HT Descriptors: every picture has a vector of features

-Tags

To build the search engine, I followed this logic:

## Prepare the environment

So, for this project, I opted as technologies:

-MongoDB: as my NoSQL database (great choice for this kind of data) ![](RackMultipart20210627-4-1nw0386_html_ac3c26de3b492930.png)

-Python: to process the data and classify the pictures using KMeans

![](1.png)

-Flask: to Create the API rest architecture to send and receive data from the database

![](2.png) ![](3.jpg)

## Prepare the Data

In order to prepare Data:

I Created a class called Metadata where I am going to put:

The picture paths

The List of tags

The family (or group ) where I classified the picture using eh\_descriptor

The family (or group ) where I classified the picture using ht\_descriptor

![](4.png)

## Classify the Data

To Classify the data:
 I used K-means algorithm which is a very important algorithm in the world of Clustering.

Since we have a data with 1M lines. It took too much time to get the result

I stocked the Output of clustering from both descriptors in one file to make it reusable ( I don&#39;t need to start the K-means algorithm every time I try to reorder or change my data architecture ( mapping).

![](5.png)

## Put Data in the Database

After getting all the data well prepared, I started Injecting this data to the MongoDB , this action took too much time also.

![](6.png)

## Create the APIs

After getting everything ready (database is ready)

I prepared two APIs:

Search API:

-which is the main API, in this API, a template containing all the one million pictures rendered in one page. To reduce latency, I used paging to avoid having one or two minutes every time to charge the page.

![](7.png)

Look for Similarity API:

-when clicking on any picture. A page containing all the related pictures (or similar ) to this specific picture will be rendered

![](8.png)

## Frontend HTML Code

![](9.png)
