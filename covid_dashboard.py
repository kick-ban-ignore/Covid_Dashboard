### Covid-19 Dashboard

import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
from bs4 import BeautifulSoup
import requests

#Title and header
st.title("Covid-19 Dashboard")
'''
EDA for Covid-19 related numbers: cases and deaths by country and worldwide
***************************************************************************
'''

#Data import and columns selection
data = "https://covid.ourworldindata.org/data/ecdc/full_data.csv"
df = st.cache(pd.read_csv)(data)  # caches DF, @st.cache for functions

# Country Selection:
countries = list(df["location"].unique()) #creating a list with countries
countries.insert(0, "World") #with World as first item
del countries[-2]

country = st.sidebar.selectbox('Pick a country!', countries)

df_filtered = df[df["location"] == country]
latest_deathcount = df_filtered.iloc[-1:,5]
latest_casecount = df_filtered.iloc[-1:,4]

st.write(country + "  -  Confirmed Cases: " + str(latest_casecount.values) + "  -  Confirmed Deaths: " + str(latest_deathcount.values))


# Create Bar charts using plotly
fig_deaths = go.Figure(data=[
	go.Bar(name="Total Deaths", x=df_filtered.date, y=df_filtered['total_deaths'],
 				),
 	go.Bar(name="New Deaths", x=df_filtered.date, y=df_filtered['new_deaths']
                      )])
fig_cases = go.Figure(data=[
	go.Bar(name="Total Cases", x=df_filtered.date, y=df_filtered['total_cases']
 				),
 	go.Bar(name="New Cases", x=df_filtered.date, y=df_filtered['new_cases']
                      )])

# Customize aspect
fig_cases.update_layout(title_text='Cases in ' + country, xaxis_rangeslider_visible=True)
fig_deaths.update_layout(title_text='Deaths in ' + country, xaxis_rangeslider_visible=True)


# Plot the 4 different charts
st.plotly_chart(fig_cases)
st.plotly_chart(fig_deaths)


# About me
if st.button("About"):
	st.subheader("Covid-19 Data EDA Webapp")
	'''
	Data from [Our World in Data] (https://ourworldindata.org/coronavirus-source-data)
		
	Built with Streamlit
	
	By Max [@kick_ban_ignore](https://www.twitter.com/kick_ban_ignore)
	'''
