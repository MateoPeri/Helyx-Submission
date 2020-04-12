# Solar Predictor

## What inspired us
Hi!
We're Juan Daniel López and Mateo Periago, 16-year old students from Murcia, Spain.
We decided to make this project because our region is always extremely sunny. We figured that there was a lot of wasted potential, as the energy of the sun is not exploited enough in our country.


## What we've learned
Overall, we think that we've learned lots with this project. We've trained models based on time series with Facebook Prophet, which we had never done before. We have also learned about the Open Data program that our region has. We used it to get our data. Hosting our website on AWS was also a new experience for us. Finally, designing the website that would serve our models was really fun and we learned a lot about Streamlit and networking in general.


## How we built it
We used the databases provided by the IMIDA, the Murcian Institute of Agrarian R+D.
These databases were composed of weather data picked up by several weather stations in our region. Most results date back to January 2000, and go up to December 2018. So we had plenty of data to train a model and make good predictions. All this data can be found in the data folder. There are 27 CSV files, one for each weather station in the region.
We were interested primarily on the solar radiation values, as you can use them to calculate how much would a solar panel produce.

To train the model, we used Facebook Prophet, a library that is commonly used for time series data. After much processing of the data and many headaches, we managed to get an accuracy score of 75%, which is not bad.
We used Pandas and Numpy for the data processing, as well as a small library (called utm) for converting from utm coordinates to latitude and longitude.
We also learned about Altair, a graphing library that can make awesome charts with ease.

The data is presented as a website, which we made on Streamlit. It allows everyone interested in environmental sustainability to know the amount of energy they are able to get from a solar panel depending on the day, as well as some energy comparisons (like how many light bulbs a panel can power) to make people realize the real impact this could have. The website is hosted in AWS EC2.


## Challenges we faced

We were stuck for quite some time because our model was giving very bad predictions. It turned out to be a mistake on our side, as we had some files that were missing many values, causing the model to predict badly. We ended up discarding those files.

Hosting our web on AWS was also quite challenging, as we had little experience with the Linux command line, so setting everything up was a difficult but rewarding experience.
The domain name is a sub domain of my website which points to the AWS instance. We also had to acquire a static IP for our website.

## More insight

In our opinion, this is a very innovative idea in our region, as there is a lot of energy that could be harvested but goes instead to waste. This project can impact people (and governments), and make them realize that solar power can be a good alternative to fossil fuels, as solar is a clean and renewable source of energy. It would be a great way of fighting against climate change, while providing us with sustainable energy.
