# ds-1
@app.route('/predict',methods=['POST','GET']) This route is used to predict airbnb price by defining values of each parameter. The model is a CNN model using tensorflow.

city = string
room_type = string
security_deposit = float
guest_included = int
mininum_nights = int




To get the price prediction, from the api we need to pass values of parameters in the URL as below
https://airbnbapi-ds.herokuapp.com/predict?city=new%20york&room_type=HOTEL%20ROOM&security_deposit=100&guest_included=2&mininum_nights=2
