# 📊 Financial Dashboard

A modern, interactive financial dashboard built with Python and Streamlit that works with uploaded Excel files to visualize your financial data.

## 🚀 Features

- **📁 Simple File Upload**: Just upload your Excel file - no complex setup required
- **📊 Interactive Charts**: Revenue trends, profit margins, balance sheet overview
- **💰 Key Metrics**: Revenue, profit, ROE, profit margins with growth indicators
- **📋 Data Filtering**: Filter by date range and select specific columns
- **📥 Export Data**: Download filtered data as CSV
- **🎨 Modern UI**: Clean, professional interface with responsive design
- **📱 Mobile Friendly**: Works on desktop and mobile devices

## 🛠️ Installation

1. **Clone or download this project**
2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Dashboard

```bash
source venv/bin/activate
streamlit run financial_dashboard_simple.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

## 📱 Usage

1. **Prepare your Excel file** with the required columns (see format below)
2. **Upload your Excel file** using the file uploader in the dashboard
3. **View your financial dashboard** with interactive charts and metrics
4. **Filter and export data** as needed

## 📊 Excel File Format

Your Excel file should have the following columns (first row as headers):

| Column | Description | Required | Example |
|--------|-------------|----------|---------|
| Date | Date of the record | Yes (for charts) | 2024-01-01 |
| Revenue | Total revenue | No | 100000 |
| Expenses | Total expenses | No | 70000 |
| Profit | Net profit | No | 30000 |
| Cash_Flow | Cash flow | No | 25000 |
| Assets | Total assets | No | 500000 |
| Liabilities | Total liabilities | No | 200000 |
| Equity | Total equity | No | 300000 |

**Notes:**
- The first row should contain column headers
- The dashboard will automatically calculate additional metrics like Profit Margin and ROE
- You can include any combination of these columns - the dashboard adapts to what you have
- Date column is required for time series charts

## 📊 Dashboard Sections

### File Upload
- Simple drag-and-drop or click-to-upload interface
- Supports `.xlsx` and `.xls` formats
- Shows data preview after upload

### Key Metrics
- **Total Revenue**: Current revenue with growth percentage
- **Net Profit**: Current profit with growth percentage
- **Profit Margin**: Profit as percentage of revenue
- **ROE**: Return on Equity

### Charts
- **Revenue vs Expenses Trend**: Line chart showing revenue and expenses over time
- **Profit Margin Trend**: Profit margin percentage over time
- **Balance Sheet Overview**: Assets, liabilities, and equity trends
- **Monthly Cash Flow**: Bar chart of cash flow by month

### Data Table
- Interactive table with all your financial data
- Filter by date range
- Select specific columns to display
- Download filtered data

## 🛠️ Customization

### Adding New Charts
1. Create a new function in `financial_dashboard_simple.py`
2. Use Plotly to create the chart
3. Add it to the main dashboard layout

### Modifying Metrics
1. Update the `calculate_metrics()` function
2. Add new metrics to the metrics dictionary
3. Display them in the metrics section

### Styling
1. Modify the CSS in the `st.markdown()` section
2. Update colors, fonts, and layout as needed

## 📝 Troubleshooting

### Common Issues

1. **"No module named streamlit"**
   - Make sure you're in the virtual environment: `source venv/bin/activate`
   - Install packages: `pip install -r requirements.txt`

2. **"Error loading Excel file"**
   - Check that your Excel file has the correct format
   - Ensure the first row contains column headers
   - Try saving the file as `.xlsx` format

3. **"No financial metrics found"**
   - Check that your Excel file has the expected column names
   - Make sure the data is in the correct format (numbers for financial values)

4. **Dashboard not loading**
   - Make sure you're running: `streamlit run financial_dashboard_simple.py`
   - Check that the virtual environment is activated
   - Try a different port if 8501 is busy: `streamlit run financial_dashboard_simple.py --server.port 8502`

## 🔄 Alternative Versions

- **`financial_dashboard.py`**: Original version with Google Sheets integration (requires setup)
- **`financial_dashboard_simple.py`**: Simplified version with Excel upload (recommended)

## 🎯 Execution Types Reference

A new application that displays a reference guide for execution type icons:

### Features
- **Icon Mappings**: Maps Ant Design icons to Lucide React equivalents
- **Execution Types**: Covers 9 different execution types (TEST_MANUAL, EXEC_MANUAL, etc.)
- **Color Reference**: Shows the color scheme for each execution type
- **Implementation Guide**: Provides code examples for React implementation

### Running the Application

```bash
source venv/bin/activate
python run_execution_types.py
# Or directly with streamlit:
streamlit run execution_types_reference.py
```

The application includes:
- Interactive table with all execution types
- Color-coded reference with emojis
- Implementation examples for React + Lucide
- Detailed breakdown of each execution type
- Links to Lucide icon library

This reference guide was generated from [Figma Make](https://www.figma.com/make/IrOhNPKQwgaWvmO996VL0c/Select-Icons-for-Execution-Types) design.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this dashboard.

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues or need help:

1. Check the troubleshooting section above
2. Ensure all dependencies are properly installed
3. Verify your Excel file format matches the requirements
4. Make sure you're using the virtual environment

---

**Happy Dashboarding! 📊✨** 