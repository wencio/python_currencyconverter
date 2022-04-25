     

from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import streamlit as st
import datetime as dt
import pandas as pd


st.title('Currency Dashboard')
countries = ('EUR','INR','SEK','AUD','CHF','GBP','JPY','CAD','NZD')
dropdown = st.multiselect('Pick your assets',countries)
start = st.date_input('Pick your date',value=pd.to_datetime('2021-01-01'))

b = BtcConverter()  
c = CurrencyRates()


st.subheader('Currency converter {}'.format(dropdown))

for i in dropdown:
    data = c.get_rate('USD',i,start)
    st.write("USD currency rates of ",i,"is: ",data )

st.write("USD currency rates of Bitcoin is:",b.get_previous_price('USD', start))
   


 