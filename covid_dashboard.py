### Covid-19 Dashboard

#Imports neccessary packages
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import locale

#Title and header
st.title("Covid-19 in Numbers")
'''
Data Analysis for Covid-19 related numbers: cases and deaths by country and worldwide
***************************************************************************
'''

#Data import and columns selection
#Case and Death numbers
data = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = st.cache(pd.read_csv)(data, sep=",")  # caches DF, @st.cache for functions

# Country Selection:
countries = list(df["location"].unique()) #creating a list with countries
countries.insert(0, "World") #with World as first item
del countries[-2]

country = st.sidebar.selectbox('Pick a country!', countries)

df_filtered = df[df["location"] == country]

#Getting the numbers
latest_deathcount = df_filtered.iloc[-1:,5]
latest_casecount = df_filtered.iloc[-1:,4]

st.write(country + "  -  Confirmed Cases: " + str(int(latest_casecount)) + "  -  Confirmed Deaths: "
		 + str(int(latest_deathcount)))

# Create Bar charts using plotly
fig_new_cases = go.Figure(data=[
 	go.Bar(name="New Cases", x=df_filtered.date, y=df_filtered['new_cases']
    )])
fig_new_deaths = go.Figure(data=[
 	go.Bar(name="New Deaths", x=df_filtered.date, y=df_filtered['new_deaths']
    )])
fig_total_cases = go.Figure(data=[
 	go.Bar(name="Total Cases", x=df_filtered.date, y=df_filtered['total_cases']
	)])
fig_total_deaths = go.Figure(data=[
	go.Bar(name="Total Deaths", x=df_filtered.date, y=df_filtered['total_deaths']
    )])

# Customize aspect
fig_new_cases.update_layout(title_text='New Cases in ' + country, xaxis_rangeslider_visible=True)
fig_new_deaths.update_layout(title_text='New Deaths in ' + country, xaxis_rangeslider_visible=True)
fig_total_cases.update_layout(title_text='Cum. Cases in ' + country, xaxis_rangeslider_visible=True)
fig_total_deaths.update_layout(title_text='Cum. Deaths in ' + country, xaxis_rangeslider_visible=True)

# Plot the 4 different charts
st.plotly_chart(fig_new_cases)
st.plotly_chart(fig_new_deaths)
st.plotly_chart(fig_total_cases)
st.plotly_chart(fig_total_deaths)


# About me
if st.button("About"):
	st.subheader("Covid-19 Data EDA Webapp")
	'''
	Data from [Our World in Data] (https://ourworldindata.org/coronavirus-source-data)
	
	Built with Streamlit
		
	By Max [@kick_ban_ignore](https://www.twitter.com/kick_ban_ignore)
	
	Wash your hands! :mask: :sweat_drops: :+1:
	'''
