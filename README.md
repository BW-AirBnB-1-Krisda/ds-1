# ds-1
@app.route('/predict',methods=['POST','GET']) This route is used to predict airbnb price by defining values of each parameter. The model is a CNN model using tensorflow.






To get the price prediction, from the api we need to pass values of parameters in the URL as below
https://dspt7-airbnb.herokuapp.com/predict?city=NEW%20YORK&room_type=HOTEL%20ROOM&security_deposit=100.0&guests_included=2&mininum_nights=2
