from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import math
import yfinance as yf
#%matplotlib inline
from sklearn.preprocessing import MinMaxScaler
##from tensorflow.keras.layers import Dense, Dropout, LSTM
# Create your views here.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import math
import pickle as pk
import yfinance as yf
#matplotlib inline
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

def prediction(ticker):
    global next_days 
    global day_step
    global prediction
    global data
    global train_len 
    day_step = 150
    data = yf.download(tickers = ticker, period='5y', interval='1d')
    df = data.filter(['Close'])
    df=df.values
    #get the lengh of training set
    train_len= math.ceil(len(df) * 0.9) #math.ceil to round up  
    #scaling 
    scaler = MinMaxScaler(feature_range=(0,1)) #Scaler function 
    scaled_df = scaler.fit_transform(df)
    #create the training data set
    train_data = scaled_df[0:train_len , :]

    #split the data into x_train and y_train 
    x_train = []
    y_train = []
    for i in range (day_step , len(train_data)):
        x_train.append(train_data[i-day_step:i , 0]) # form 0 : 59
        y_train.append(train_data[i,0])        # at position 60
    #     if i == day_step :              #for example
    #         print(x_train)
    #         print(y_train)
    
    #print(x_train)
    x_train, y_train = np.array(x_train), np.array(y_train) #convert to numpy array
    x_train = np.reshape(x_train , (x_train.shape[0],x_train.shape[1],1)) #(num. of samples , num of time steps , num. of features)
    model = Sequential()
    model.add(LSTM(units = 120 , return_sequences=True , input_shape =(x_train.shape[1],1)))
    #model.add(Dropout(0.5))  # dropout rate of 20%
    model.add(LSTM(units =120 , return_sequences=False))
    #model.add(Dropout(0.5))  # dropout rate of 20%  
    model.add(Dense(units =60))
    model.add(Dense(units =1))
    model.compile(optimizer = 'adam' , loss= 'mean_squared_error')
    model.fit(x_train ,y_train , batch_size =1 , epochs=8)
    test_data = scaled_df[train_len - day_step : , :] #-day_step to fit the y_test

    x_test=[]
    y_test=df[train_len: , :]

    for i in range (day_step, len(test_data)):
        x_test.append(test_data[i-day_step:i , 0])
    #convert the data to a numpy array
    x_test= np.array(x_test)
    #reshape the data into 3 dimintions due to lstm 
    x_test = np.reshape (x_test,(x_test.shape[0],x_test.shape[1],1))
    prediction = model.predict(x_test)
    #inverse scaler
    prediction = scaler.inverse_transform(prediction)
    x_input = test_data[len(test_data)-day_step : ].reshape(1,-1)
    temp_input=list(x_input)
    temp_input=temp_input[0].tolist()
    lst_output=[]
    #n_steps=100
    i=0
    next_days = 30
    while(i<next_days):
        
        if(len(temp_input)>day_step):
            #print(temp_input)
            x_input=np.array(temp_input[1:])
            ##print("{} day input {}".format(i,x_input))
            x_input=x_input.reshape(1,-1)
            x_input = x_input.reshape((1, day_step, 1))  # reshape for LSTM
            #print(x_input)
            yhat = model.predict(x_input, verbose=0)   #predict
            ##print("{} day output {}".format(i,yhat))
            temp_input.extend(yhat[0].tolist())       # add the new day 
            temp_input=temp_input[1:]
            #print(temp_input)
            lst_output.extend(yhat.tolist())
            i=i+1
            
        else:
            x_input = x_input.reshape((1, day_step,1))  # reshape for LSTM
            yhat = model.predict(x_input, verbose=0)
            print(yhat[0])
            temp_input.extend(yhat[0].tolist())
            print(len(temp_input))
            lst_output.extend(yhat.tolist())
            i=i+1
    print(scaler.inverse_transform(lst_output))
    output=scaler.inverse_transform(lst_output)
    

    return data,train_len,day_step,next_days,df,output
            

data, train_len,day_step,next_days,df,output,model = prediction('AAPL')

def predict_next_day():
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_df=scaler.fit_transform(df)
    actual_data = scaled_df[len(scaled_df) - day_step :]
    actual_data

    for i in range (day_step, len(actual_data)):
        actual_data.append(actual_data[i-day_step:i , 0])

    #convert the data to a numpy array
    actual_data= np.array(actual_data)
    #reshape the data into 3 dimintions due to lstm 
    actual_data = np.reshape (actual_data,(actual_data.shape[1],actual_data.shape[0],1))
    
    saved_model=  pk.load(open('C:\Users\max\anaconda3\envs\stockmarket\StockMarketProject\PredictionModel\saved_data\saved_AAPL.sav', 'rb'))
    #The next day Predicted Price  
    first_next_date = saved_model.predict(actual_data)
    #invers scaler
    first_next_date = scaler.inverse_transform(first_next_date)
    
    return first_next_date


def plot_predicrtions():
    day_new=np.arange(1,day_step+1)
    day_pred=np.arange(day_step+1,day_step+next_days+1)
    plt.plot(day_new,df[len(df)-day_step:])
    plt.plot(day_pred,output)




