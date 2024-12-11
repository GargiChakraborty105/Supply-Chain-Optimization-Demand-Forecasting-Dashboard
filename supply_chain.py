import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import timedelta

# Load data
df = pd.read_csv("supply_chain_updated_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar filters
st.sidebar.header("Filters")
selected_product = st.sidebar.selectbox("Select Product", df["Product_ID"].unique())
forecast_days = st.sidebar.slider("Forecast Period (Days)", 7, 30, 14)

# Filter data
filtered_data = df[df["Product_ID"] == selected_product]

# Title
st.title("Supply Chain Optimization & Demand Forecasting")

# 1. Demand Forecasting
st.header(f"Demand Forecast for {selected_product}")

# Simple Forecasting Model (moving average)
filtered_data = filtered_data.set_index("Date")
forecast = filtered_data["Units_Sold"].rolling(window=7).mean().dropna()

# Forecast future dates
last_date = forecast.index[-1]
future_dates = [last_date + timedelta(days=i) for i in range(1, forecast_days + 1)]
future_forecast = [forecast.iloc[-1] + np.random.randint(-5, 5) for _ in future_dates]

# Plot Forecast
fig1 = px.line(x=forecast.index, y=forecast, labels={"x": "Date", "y": "Units Sold"}, title="Historical Demand & Forecast")
fig1.add_scatter(x=future_dates, y=future_forecast, mode='lines', name='Forecast')
st.plotly_chart(fig1)

# 2. Inventory Recommendations
st.header("Inventory Recommendations")
latest_inventory = filtered_data["Inventory_Level"].iloc[-1]
reorder_threshold = filtered_data["Reorder_Threshold"].iloc[-1]

if latest_inventory < reorder_threshold:
    st.warning(f"Inventory Level ({latest_inventory}) is below the Reorder Threshold ({reorder_threshold}). Consider restocking.")
else:
    st.success(f"Inventory Level ({latest_inventory}) is sufficient.")

# 3. Supplier Lead Time Analysis
st.header("Supplier Lead Time Analysis")
lead_time = filtered_data["Lead_Time"].iloc[-1]
supplier_reliability = filtered_data["Supplier_Reliability"].iloc[-1]

st.info(f"Current Lead Time: {lead_time} days. Supplier Reliability: {supplier_reliability}%.")
if supplier_reliability < 90:
    st.warning("Potential risk due to low supplier reliability. Consider alternate suppliers.")

# 4. Stock-Out Risk Assessment
st.header("Stock-Out Risk Assessment")
avg_daily_demand = filtered_data["Units_Sold"].mean()
days_to_stock_out = latest_inventory / avg_daily_demand if avg_daily_demand > 0 else np.inf

st.write(f"Estimated Days Until Stock-Out: {days_to_stock_out:.2f} days.")
if days_to_stock_out < lead_time:
    st.error("Risk of stock-out before the next delivery. Adjust inventory levels or lead times.")
else:
    st.success("Inventory levels are sufficient to cover lead times.")

# 5. Revenue Impact Analysis
st.header("Revenue Impact Analysis")
future_revenue = np.sum([units * filtered_data["Sales_Price"].iloc[-1] for units in future_forecast])
st.write(f"Projected Revenue for Next {forecast_days} Days: ${future_revenue:.2f}")

# What-If Scenario Analysis
st.header("What-If Scenario Analysis")
promo_impact = st.slider("Promotional Impact (%)", -50, 100, 0)
adjusted_forecast = [units * (1 + promo_impact / 100) for units in future_forecast]

fig2 = px.line(x=future_dates, y=adjusted_forecast, labels={"x": "Date", "y": "Units Sold"}, title="What-If Demand Forecast")
st.plotly_chart(fig2)

# Footer
st.sidebar.info("Built with Streamlit and Plotly")
