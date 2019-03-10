## Inspiration
The [biggest challenges](https://www.gtnexus.com/resources/blog-posts/top-10-challenges-global-pharmaceutical-supply-chains) pharmaceutical companies are facing today include: 
+ Shipment visibility
+ Batch expiration tracking
+ Inventory management
+ Order management

We set out to tackle these issues by creating an intuitive visualization of pharmaceutical supply chain data. For this project we utilized the blockchain API provided by Merck & Co.

## What it does
+ Pulls data from Merck's [Blockchain API](https://github.com/merck-hackru/blockchain-api).
+ Sorts and organizes batch shipment attributes.
+ Creates an interactive map-based data visualization model
+ Provides a sortable, searchable table interface for shipping data

## How we built it
python, js, html, css, golang


## Challenges we ran into
* Most of Merck's 200 sample data entries shared attributes (e.g. most were at coords [0, 0])
  * We generated our own fake Merck data set using randomization in python and publicly available data on the 1000 most populated American cities 

## Accomplishments that we're proud of
*

## What we learned
javascript, bootstrap, html

