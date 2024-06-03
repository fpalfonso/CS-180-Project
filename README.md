# Predictive Maintenance System for Automotive Vehicles

Group 8:

ALFONSO, Francis Donald (THU)

DOLOJAN, Julian (THX)

PILAPIL, Marcus Corso (THX)

# Source of the datasets
The datasets are from: https://www.kaggle.com/datasets/navins7/vehicle-maintenance-record

# Model
The solution for the project can be found in `CS_180_Project_Group_8.ipynb`

# Web App
The web app was implemented by using `Streamlit.io`. The web app takes the vehicle type and mileage for input. The mileage can be in between `10000` and `100000`. The vehicle types are the 7 unique vehicles from the datasets which are:
```     
"Honda Jazz Petrol",
"Honda Jazz Diesel",
"Honda Amaze Petrol",
"Honda Amaze Diesel",
"Honda City Petrol",
"Honda City Diesel",
"Toyota Fortuner Diesel"
```

The output is the predicted maintenance based on the Naive Bayes Classification model. 

To run the app in your local host:
```
streamlit run app.py
```