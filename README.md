# **Supply Chain Optimization & Demand Forecasting Dashboard**

### 📊 **An Interactive Dashboard for Supply Chain Management and Forecasting**

---

## 📌 **Project Overview**

The **Supply Chain Optimization & Demand Forecasting Dashboard** is a powerful interactive tool designed to help businesses optimize their supply chain processes, forecast demand, and identify potential disruptions. Built using **Streamlit**, **Pandas**, and **Plotly**, this dashboard provides real-time insights and recommendations to improve decision-making in supply chain management.

### **Key Features**

1. **Demand Forecasting**  
   Predict future product demand using a simple moving average model and visualize forecasts with interactive charts.

2. **Inventory Recommendations**  
   Get automated alerts and recommendations for restocking based on current inventory levels and reorder thresholds.

3. **Potential Supply Chain Disruptions**  
   Identify potential risks based on supplier reliability and lead times.

4. **What-If Scenario Analysis**  
   Simulate real-time supply chain scenarios to understand the impact of changes in lead times, reliability, and forecast periods.

5. **Interactive Data Visualization**  
   Leverage Plotly for dynamic, customizable charts to explore historical and forecasted data.

---

## 🗂️ **Project Structure**

```
Supply-Chain-Optimization-Demand-Forecasting-Dashboard/
│-- supply_chain.py
│-- supply_chain_sample_data.csv
│-- data.py
│-- supply_chain_updated_data.csv
│-- README.md
```

- **`supply_chain.py`**: Main Python script that runs the Streamlit dashboard.
- **`supply_chain_sample_data.csv`**: Sample dataset used for the dashboard.
- **`data.py`**: to edit the columns in the dataset used for the dashboard.
- **`supply_chain_updated_data.csv`**: updated dataset used for the dashboard.
- **`README.md`**: Documentation for the project.

---

## ⚙️ **Installation Instructions**

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/Supply-Chain-Optimization-Demand-Forecasting-Dashboard.git
   cd Supply-Chain-Optimization-Demand-Forecasting-Dashboard
   ```

2. **Set Up a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate          # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**  
   ```bash
   streamlit run supply_chain.py
   ```

5. **Open in Browser**  
   The app will launch in your default browser at:  
   ```
   http://localhost:8501
   ```

---

## 🗄️ **Dataset Details**

Ensure your dataset contains the following columns:

| **Column Name**         | **Description**                                       |
|--------------------------|-------------------------------------------------------|
| `Date`                  | Date of the sales record (format: YYYY-MM-DD)         |
| `Product_ID`            | Unique identifier for each product                    |
| `Units_Sold`            | Number of units sold on the given date                |
| `Sales_Price`           | Price per unit of the product                         |
| `Inventory_Level`       | Current inventory level for the product               |
| `Reorder_Threshold`     | Minimum stock level before a restock is needed        |
| `Lead_Time`             | Estimated delivery time (in days)                     |
| `Supplier_Reliability`  | Supplier reliability percentage (e.g., 70%-99%)       |

---

## 🚀 **How to Use the Dashboard**

1. **Filters in the Sidebar**  
   - **Select Product**: Choose a specific product from the dropdown menu.  
   - **Forecast Period (Days)**: Select a time frame for forecasting (between 7 to 30 days).

2. **Demand Forecasting**  
   - Displays historical sales data and forecasts future demand using a moving average model.  
   - Visualize the forecast with interactive Plotly charts.

3. **Inventory Recommendations**  
   - Provides alerts based on current inventory levels compared to the reorder threshold.  
   - **Warning** if inventory is low and **Success** if inventory is sufficient.

4. **Potential Supply Chain Disruptions**  
   - Identifies potential disruption risks based on `Lead_Time` and `Supplier_Reliability`.

5. **What-If Scenario Analysis**  
   - Simulate different scenarios by adjusting parameters in the sidebar and observe real-time changes.

---

## 🛠️ **Customization and Enhancements**

### **Additional Elements for the Dashboard**

You can extend the dashboard by adding more elements related to supply chain management:

1. **Cost Analysis**  
   - Calculate and display holding costs, stockout costs, and order costs.

2. **Supplier Performance Trends**  
   - Visualize historical data for supplier reliability and delivery performance.

3. **Lead Time Trends**  
   - Track changes in supplier lead times over time.

### **Advanced Forecasting Models**

Consider implementing advanced models like:

- **ARIMA**: For time-series forecasting.  
- **Prophet**: For robust forecasting with trends and seasonality.  
- **LSTM**: For deep learning-based predictions.

---

## 📦 **Dependencies**

The following libraries are required for this project:

- **Streamlit**: For building the interactive dashboard.  
- **Pandas**: For data manipulation and analysis.  
- **Plotly**: For interactive data visualization.  
- **NumPy**: For numerical operations.

Install them using:

```bash
pip install streamlit pandas numpy plotly
```

## 🤝 **Contributing**

Contributions are welcome! If you want to improve this project:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## 📄 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📧 **Contact**

For any questions or suggestions, feel free to reach out:

- **Name**: Gargi Chakraborty  
- **Email**: [your.email@example.com]  
- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)  

---

Happy Optimizing! 🚀📊
