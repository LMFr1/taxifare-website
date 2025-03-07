import streamlit as st
import datetime
import requests

st.title("🚖 Taxi Fare - Predictions 🚖")

st.markdown('''
## ? 🗽 Where do you want to go 🗽 ?


### Please provide the following ride details:
''')
date = st.date_input("📅 Select the date of the ride", datetime.date.today())
time = st.time_input("⏰ Select the time of the ride", datetime.datetime.now().time())
pickup_longitude = st.number_input("📍Enter Pickup Longitude", value=-73.985428, format="%.6f")
pickup_latitude = st.number_input("📍Enter Pickup Latitude", value=40.748817, format="%.6f")
dropoff_longitude = st.number_input("📍Enter Dropoff Longitude", value=-73.985428, format="%.6f")
dropoff_latitude = st.number_input("📍Enter Dropoff Latitude", value=40.748817, format="%.6f")


passenger_count = st.slider("🧑‍🤝‍🧑 Select the number of passengers", min_value=1, max_value=8, value=1)

pickup_datetime = datetime.datetime.combine(date, time)
format_datetime = pickup_datetime.strftime("%Y-%m-%d %H:%M:%S")
format_datetime = format_datetime.replace(" ", "+")


st.markdown('''
## Click here to get your prediction 🖱️
''')

url = f"http://taxifare.lewagon.ai/predict?pickup_datetime={format_datetime}&pickup_longitude={pickup_longitude}&pickup_latitude={pickup_latitude}&dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_latitude}&passenger_count={passenger_count}"

if st.button("Get your Prediction here 🔮 "):
    response = requests.get(url)

    st.markdown('''
    ## 🚕 Your fare 🚕:
    ''')
    if response.status_code == 200:
        prediction = response.json().get("fare")
        st.success(f"Estimated Fare: ${prediction}")
    else:
        st.error("There is an error")
