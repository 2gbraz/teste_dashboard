import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
import io

# Page configuration
st.set_page_config(
    page_title="Financial Dashboard - Transposed",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .positive-change {
        color: #28a745;
    }
    .negative-change {
        color: #dc3545;
    }
</style>
""", unsafe_allow_html=True)

def load_transposed_excel_data(uploaded_file):
    """
    Load data from uploaded Excel file with transposed structure
    (dates as columns, metrics as rows)
    """
    try:
        if uploaded_file is not None:
            # Read Excel file
            df = pd.read_excel(uploaded_file, engine='openpyxl', index_col=0)
            
            # Transpose the data to get dates as index and metrics as columns
            df_transposed = df.T
            
            # Convert index to datetime
            df_transposed.index = pd.to_datetime(df_transposed.index)
            df_transposed.index.name = 'Date'
            
            # Reset index to make Date a column
            df_transposed = df_transposed.reset_index()
            
            # Calculate additional metrics if columns exist
            if 'Revenue' in df_transposed.columns and 'Profit' in df_transposed.columns:
                df_transposed['Profit_Margin'] = (df_transposed['Profit'] / df_transposed['Revenue']) * 100
            
            if 'Profit' in df_transposed.columns and 'Equity' in df_transposed.columns:
                df_transposed['ROE'] = (df_transposed['Profit'] / df_transposed['Equity']) * 100
            
            return df_transposed
        else:
            return None
    except Exception as e:
        st.error(f"Error loading Excel file: {str(e)}")
        return None

def calculate_metrics(df):
    """
    Calculate key financial metrics
    """
    if df is None or df.empty:
        return {}
    
    latest = df.iloc[-1]
    previous = df.iloc[-2] if len(df) > 1 else latest
    
    metrics = {}
    
    # Basic metrics
    if 'Revenue' in df.columns:
        metrics['total_revenue'] = latest['Revenue']
        if len(df) > 1:
            metrics['revenue_growth'] = ((latest['Revenue'] - previous['Revenue']) / previous['Revenue']) * 100
        else:
            metrics['revenue_growth'] = 0
    
    if 'Expenses' in df.columns:
        metrics['total_expenses'] = latest['Expenses']
        if len(df) > 1:
            metrics['expense_growth'] = ((latest['Expenses'] - previous['Expenses']) / previous['Expenses']) * 100
        else:
            metrics['expense_growth'] = 0
    
    if 'Profit' in df.columns:
        metrics['net_profit'] = latest['Profit']
        if len(df) > 1:
            metrics['profit_growth'] = ((latest['Profit'] - previous['Profit']) / previous['Profit']) * 100
        else:
            metrics['profit_growth'] = 0
    
    if 'Profit_Margin' in df.columns:
        metrics['profit_margin'] = latest['Profit_Margin']
    
    if 'ROE' in df.columns:
        metrics['roe'] = latest['ROE']
    
    if 'Assets' in df.columns:
        metrics['total_assets'] = latest['Assets']
    
    if 'Liabilities' in df.columns:
        metrics['total_liabilities'] = latest['Liabilities']
    
    if 'Equity' in df.columns:
        metrics['equity'] = latest['Equity']
    
    if 'Cash_Flow' in df.columns:
        metrics['cash_flow'] = latest['Cash_Flow']
    
    return metrics

def create_revenue_chart(df):
    """
    Create revenue trend chart
    """
    fig = go.Figure()
    
    if 'Date' in df.columns and 'Revenue' in df.columns:
        fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['Revenue'],
            mode='lines+markers',
            name='Revenue',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
    
    if 'Date' in df.columns and 'Expenses' in df.columns:
        fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['Expenses'],
            mode='lines+markers',
            name='Expenses',
            line=dict(color='#ff7f0e', width=3),
            marker=dict(size=8)
        ))
    
    fig.update_layout(
        title='Revenue vs Expenses Trend',
        xaxis_title='Date',
        yaxis_title='Amount ($)',
        hovermode='x unified',
        height=400
    )
    
    return fig

def create_profit_margin_chart(df):
    """
    Create profit margin chart
    """
    fig = go.Figure()
    
    if 'Date' in df.columns and 'Profit_Margin' in df.columns:
        fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['Profit_Margin'],
            mode='lines+markers',
            name='Profit Margin (%)',
            line=dict(color='#2ca02c', width=3),
            marker=dict(size=8)
        ))
    
    fig.update_layout(
        title='Profit Margin Trend',
        xaxis_title='Date',
        yaxis_title='Profit Margin (%)',
        hovermode='x unified',
        height=400
    )
    
    return fig

def create_balance_sheet_chart(df):
    """
    Create balance sheet chart
    """
    fig = go.Figure()
    
    if 'Date' in df.columns:
        if 'Assets' in df.columns:
            fig.add_trace(go.Scatter(
                x=df['Date'],
                y=df['Assets'],
                mode='lines+markers',
                name='Assets',
                line=dict(color='#1f77b4', width=3),
                marker=dict(size=8)
            ))
        
        if 'Liabilities' in df.columns:
            fig.add_trace(go.Scatter(
                x=df['Date'],
                y=df['Liabilities'],
                mode='lines+markers',
                name='Liabilities',
                line=dict(color='#ff7f0e', width=3),
                marker=dict(size=8)
            ))
        
        if 'Equity' in df.columns:
            fig.add_trace(go.Scatter(
                x=df['Date'],
                y=df['Equity'],
                mode='lines+markers',
                name='Equity',
                line=dict(color='#2ca02c', width=3),
                marker=dict(size=8)
            ))
    
    fig.update_layout(
        title='Balance Sheet Overview',
        xaxis_title='Date',
        yaxis_title='Amount ($)',
        hovermode='x unified',
        height=400
    )
    
    return fig

def create_cash_flow_chart(df):
    """
    Create cash flow chart
    """
    fig = go.Figure()
    
    if 'Date' in df.columns and 'Cash_Flow' in df.columns:
        fig.add_trace(go.Bar(
            x=df['Date'],
            y=df['Cash_Flow'],
            name='Cash Flow',
            marker_color='#17a2b8'
        ))
    
    fig.update_layout(
        title='Monthly Cash Flow',
        xaxis_title='Date',
        yaxis_title='Cash Flow ($)',
        height=400
    )
    
    return fig

def main():
    # Header
    st.markdown('<h1 class="main-header">📊 Financial Dashboard - Transposed Data</h1>', unsafe_allow_html=True)
    
    # File upload section
    st.header("📁 Upload Your Financial Data (Transposed Format)")
    
    uploaded_file = st.file_uploader(
        "Choose an Excel file",
        type=['xlsx', 'xls'],
        help="Upload your financial data Excel file with dates as columns and metrics as rows."
    )
    
    if uploaded_file is not None:
        # Load data
        df = load_transposed_excel_data(uploaded_file)
        
        if df is not None:
            st.success(f"✅ File uploaded successfully! Loaded {len(df)} time periods of data.")
            
            # Show data preview
            st.subheader("📋 Data Preview (After Transposition)")
            st.dataframe(df.head(), use_container_width=True)
            
            # Calculate metrics
            metrics = calculate_metrics(df)
            
            if metrics:
                # Key Metrics Section
                st.header("📈 Key Financial Metrics")
                
                # Create columns based on available metrics
                metric_cols = []
                if 'total_revenue' in metrics:
                    metric_cols.append(('Total Revenue', f"${metrics['total_revenue']:,.0f}", f"{metrics['revenue_growth']:+.1f}%"))
                
                if 'net_profit' in metrics:
                    metric_cols.append(('Net Profit', f"${metrics['net_profit']:,.0f}", f"{metrics['profit_growth']:+.1f}%"))
                
                if 'profit_margin' in metrics:
                    metric_cols.append(('Profit Margin', f"{metrics['profit_margin']:.1f}%", ""))
                
                if 'roe' in metrics:
                    metric_cols.append(('ROE', f"{metrics['roe']:.1f}%", ""))
                
                # Display metrics in columns
                if metric_cols:
                    cols = st.columns(len(metric_cols))
                    for i, (label, value, delta) in enumerate(metric_cols):
                        with cols[i]:
                            st.metric(label=label, value=value, delta=delta if delta else None)
                
                # Charts Section
                st.header("📊 Financial Charts")
                
                # First row of charts
                col1, col2 = st.columns(2)
                
                with col1:
                    revenue_fig = create_revenue_chart(df)
                    st.plotly_chart(revenue_fig, use_container_width=True)
                
                with col2:
                    profit_fig = create_profit_margin_chart(df)
                    st.plotly_chart(profit_fig, use_container_width=True)
                
                # Second row of charts
                col1, col2 = st.columns(2)
                
                with col1:
                    balance_fig = create_balance_sheet_chart(df)
                    st.plotly_chart(balance_fig, use_container_width=True)
                
                with col2:
                    cash_flow_fig = create_cash_flow_chart(df)
                    st.plotly_chart(cash_flow_fig, use_container_width=True)
                
                # Data Table Section
                st.header("📋 Full Data Table")
                
                # Add filters
                col1, col2 = st.columns(2)
                
                with col1:
                    if 'Date' in df.columns:
                        date_range = st.date_input(
                            "Select Date Range",
                            value=(df['Date'].min(), df['Date'].max()),
                            min_value=df['Date'].min(),
                            max_value=df['Date'].max()
                        )
                    else:
                        date_range = None
                
                with col2:
                    selected_columns = st.multiselect(
                        "Select Columns",
                        df.columns.tolist(),
                        default=df.columns.tolist()
                    )
                
                # Filter data
                filtered_df = df.copy()
                
                if date_range and len(date_range) == 2 and 'Date' in df.columns:
                    filtered_df = filtered_df[
                        (filtered_df['Date'].dt.date >= date_range[0]) &
                        (filtered_df['Date'].dt.date <= date_range[1])
                    ]
                
                if selected_columns:
                    filtered_df = filtered_df[selected_columns]
                
                # Display data
                st.dataframe(
                    filtered_df,
                    use_container_width=True,
                    hide_index=True
                )
                
                # Download button
                csv = filtered_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Filtered Data as CSV",
                    data=csv,
                    file_name="filtered_financial_data.csv",
                    mime="text/csv"
                )
            else:
                st.warning("⚠️ No financial metrics found in the data. Please check your Excel file format.")
        else:
            st.error("❌ Unable to load data from the uploaded file.")
    else:
        # Show instructions when no file is uploaded
        st.info("📝 **Instructions for Transposed Data Format:**")
        st.markdown("""
        1. **Prepare your Excel file** with the following structure:
           - **First column**: Metric names (Revenue, Expenses, Profit, etc.)
           - **Other columns**: Dates (2024-01-01, 2024-02-01, etc.)
           - **Data cells**: Financial values
        
        2. **Upload your Excel file** using the file uploader above
        
        3. **View your financial dashboard** with interactive charts and metrics
        
        **Note:** The dashboard will automatically transpose your data so dates become rows and metrics become columns.
        """)
        
        # Show sample data format
        st.subheader("📋 Sample Transposed Data Format")
        st.markdown("**Your Excel should look like this:**")
        
        sample_data = {
            'Metric': ['Revenue', 'Expenses', 'Profit', 'Cash_Flow', 'Assets', 'Liabilities', 'Equity'],
            '2023-01-01': [100000, 70000, 30000, 25000, 500000, 200000, 300000],
            '2023-02-01': [105000, 72000, 33000, 28000, 510000, 205000, 305000],
            '2023-03-01': [98000, 68000, 30000, 26000, 505000, 202000, 303000]
        }
        sample_df = pd.DataFrame(sample_data)
        st.dataframe(sample_df, use_container_width=True)
        
        st.markdown("**After transposition, it becomes:**")
        sample_transposed = sample_df.set_index('Metric').T
        sample_transposed.index.name = 'Date'
        sample_transposed = sample_transposed.reset_index()
        st.dataframe(sample_transposed, use_container_width=True)

if __name__ == "__main__":
    main() 