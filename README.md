 # Project description 
 
 a airbnb api to provide to front end teams price recommendations based on machine learning for their application based on the city, room type, security deposit, if there is a guest , and what th minimum night one is staying at an airbnb a price is return for the criteria the user decides on.
 
 # Dataset 
 
 `
 data.csv
 `
 This dataset provides a list of airbnb rentals at all major US cities and the different features and price for them 
 
 # dependancies 
 
 `
 Flask
 pickle
 sklearn
 pandas
 numpy
 tensorflow
 `
 # How to Use 
 
 `/predict' This route is used to predict airbnb price by defining values of each parameter. The model is a CNN model using tensorflow.`

`city = string

room_type = string

security_deposit = float

guest_included = int

mininum_nights = int
`
To get the price prediction, from the api we need to pass values of parameters in the URL as below

`https://airbnbapi-ds.herokuapp.com/predict?city=Boston&room_type=Apartment&security_deposit=200&guests_included=2&mininum_nights=2`


# LIVE SITE:

https://top-chill-final.vercel.app/login
