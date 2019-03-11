# Merck-Map: Merck Supply Chain Data Visualization
#### Kasey McFadden, Meet Patel, Abdullah Ramadan, Kailash Raman

## Results
1st Place Winner of Best Use of the Merck API Challenge at [HackRU](http://hackru-s19.devpost.com/). See the [DevPost Submission](https://devpost.com/software/merck-map).

## Usage
http://maps.merck-map.com/

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


## Biggest challenge we ran into
* Most of Merck's 200 sample data entries shared attributes (e.g. most were at coords [0, 0])
  * We generated our own fake Merck data set using randomization in python and publicly available data on the 1000 most populated American cities 

## Accomplishments that we're proud of
+ Creating interactive geographical map model without experience in html, js, css, etc.
+ Beautifying supply chain data with frontend design
+ Developing thorough understanding of Merck's blockchain-api, deciphering shipment data 

## What we learned
js, bootstrap, html

## Integrations
- Merck: pharmaceutical data blockchain API
- Google Cloud Platform: code hosting
- Domainer: domain name rental
