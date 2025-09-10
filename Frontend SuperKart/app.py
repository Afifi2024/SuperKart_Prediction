import streamlit as st
import requests

st.title("SuperKart Prediction App")

Flask_url = "https://afifi00-flask-superkart-prediction.hf.space"



Product_Id = st.text_input("Product_Id",
                                 value="FD6114",
                                 help="Enter product identifier (e.g., FD6114, NC1180, DR2699)")

Product_Weight = st.number_input("Product_Weight",
                                       value=12.66,
                                       min_value=5.81,
                                       max_value=21.04,
                                       step=0.01,
                                       format="%.2f",
                                       help="Weight of the product")

Product_Sugar_Content = st.selectbox("Product_Sugar_Content",
                                           ["Low Sugar", "Regular", "No Sugar", "reg"],
                                           index=0,
                                           help="Sugar content level of the product")

Product_Allocated_Area = st.number_input("Product_Allocated_Area",
                                               value=0.027,
                                               min_value=0.004,
                                               max_value=0.297,
                                               step=0.001,
                                               format="%.6f",
                                               help="Space allocated for product display")

Product_Type = st.selectbox("Product_Type",
                                   ["Frozen Foods", "Dairy", "Canned", "Baking Goods",
                                    "Health and Hygiene", "Snack Foods", "Meat",
                                    "Fruits and Vegetables", "Household", "Breakfast",
                                    "Hard Drinks", "Breads", "Starchy Foods", "Others",
                                    "Seafood", "Soft Drinks"],
                                   index=0,
                                   help="Category/type of the product")

Product_MRP = st.number_input("Product_MRP",
                                    value=117.08,
                                    min_value=31.23,
                                    max_value=266.89,
                                    step=0.01,
                                    format="%.2f",
                                    help="Maximum Retail Price of the product")



Store_Id = st.text_input("Store_Id",
                                value="OUT004",
                                help="Store identifier (e.g., OUT004, OUT003, OUT001, OUT002)")

Store_Establishment_Year = st.number_input("Store_Establishment_Year",
                                                 min_value=1985,
                                                 max_value=2009,
                                                 value=2009,
                                                 step=1,
                                                 help="Year when the store was established")

Store_Size = st.selectbox("Store_Size",
                                 ["Small", "Medium", "High"],
                                 index=1,  # Default to "Medium"
                                 help="Size category of the store")

Store_Location_City_Type = st.selectbox("Store_Location_City_Type",
                                              ["Tier 1", "Tier 2", "Tier 3"],
                                              index=1,  # Default to "Tier 2"
                                              help="City tier classification")

Store_Type = st.selectbox("Store_Type",
                                 ["Supermarket Type1", "Supermarket Type2", "Supermarket Type3",
                                  "Departmental Store", "Food Mart", "Grocery Store"],
                                 index=1,  # Default to "Supermarket Type2"
                                 help="Type/format of the store")


data = {
            "Product_Id": Product_Id,
            "Product_Weight": Product_Weight,
            "Product_Sugar_Content": Product_Sugar_Content,
            "Product_Allocated_Area": Product_Allocated_Area,
            "Product_Type": Product_Type,
            "Product_MRP": Product_MRP,
            "Store_Id": Store_Id,
            "Store_Establishment_Year": Store_Establishment_Year,
            "Store_Size": Store_Size,
            "Store_Location_City_Type": Store_Location_City_Type,
            "Store_Type": Store_Type
        }
if st.button("Predict"):
    response = requests.post(f"{Flask_url}/predict", json=data)
    if response.status_code == 200:
        result = response.json()
        SuperKart_prediction = result.get("Prediction", "No Prediction returned")
        st.write(f"Based on the information provided, the product with ID {Product_Id} has sales total: {SuperKart_prediction}.")
        print(f"Based on the information provided, the product with ID {Product_Id} has sales total: {SuperKart_prediction}.")
    else:
        st.error(f"Error in API request: {response.status_code}")
        st.error(f"Response: {response.text}")
