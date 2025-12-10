import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import gspread
from google.oauth2.service_account import Credentials
import numpy as np
from datetime import datetime, timedelta
import os

# Page configuration
st.set_page_config(
    page_title="Financial Dashboard",
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

@st.cache_data
def load_google_sheets_data(sheet_url, worksheet_name="Sheet1"):
    """
    Load data from Google Sheets using service account credentials
    """
    try:
        # For demo purposes, we'll create sample data
        # In production, you would use actual Google Sheets credentials
        st.info("📝 Note: This is using sample data. To connect to your actual Google Sheet, please provide your credentials.")
        
        # Create sample financial data
        dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='M')
        np.random.seed(42)
        
        data = {
            'Date': dates,
            'Revenue': np.random.normal(100000, 20000, len(dates)),
            'Expenses': np.random.normal(70000, 15000, len(dates)),
            'Profit': np.random.normal(30000, 8000, len(dates)),
            'Cash_Flow': np.random.normal(25000, 10000, len(dates)),
            'Assets': np.random.normal(500000, 50000, len(dates)),
            'Liabilities': np.random.normal(200000, 30000, len(dates)),
            'Equity': np.random.normal(300000, 40000, len(dates))
        }
        
        df = pd.DataFrame(data)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Profit_Margin'] = (df['Profit'] / df['Revenue']) * 100
        df['ROE'] = (df['Profit'] / df['Equity']) * 100
        
        return df
    
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def calculate_metrics(df):
    """
    Calculate key financial metrics
    """
    if df is None or df.empty:
        return {}
    
    latest = df.iloc[-1]
    previous = df.iloc[-2] if len(df) > 1 else latest
    
    metrics = {
        'total_revenue': latest['Revenue'],
        'total_expenses': latest['Expenses'],
        'net_profit': latest['Profit'],
        'profit_margin': latest['Profit_Margin'],
        'roe': latest['ROE'],
        'total_assets': latest['Assets'],
        'total_liabilities': latest['Liabilities'],
        'equity': latest['Equity'],
        'cash_flow': latest['Cash_Flow'],
        
        # Growth rates
        'revenue_growth': ((latest['Revenue'] - previous['Revenue']) / previous['Revenue']) * 100,
        'profit_growth': ((latest['Profit'] - previous['Profit']) / previous['Profit']) * 100,
        'expense_growth': ((latest['Expenses'] - previous['Expenses']) / previous['Expenses']) * 100,
    }
    
    return metrics

def create_revenue_chart(df):
    """
    Create revenue trend chart
    """
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Revenue'],
        mode='lines+markers',
        name='Revenue',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8)
    ))
    
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
    
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Assets'],
        mode='lines+markers',
        name='Assets',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Liabilities'],
        mode='lines+markers',
        name='Liabilities',
        line=dict(color='#ff7f0e', width=3),
        marker=dict(size=8)
    ))
    
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
    st.markdown('<h1 class="main-header">📊 Financial Dashboard</h1>', unsafe_allow_html=True)
    
    # Sidebar for configuration
    st.sidebar.header("⚙️ Configuration")
    
    # Google Sheets URL input
    sheet_url = st.sidebar.text_input(
        "Google Sheets URL",
        placeholder="https://docs.google.com/spreadsheets/d/...",
        help="Enter your Google Sheets URL here"
    )
    
    worksheet_name = st.sidebar.text_input(
        "Worksheet Name",
        value="Sheet1",
        help="Name of the worksheet containing your data"
    )
    
    # Load data
    df = load_google_sheets_data(sheet_url, worksheet_name)
    
    if df is not None:
        # Calculate metrics
        metrics = calculate_metrics(df)
        
        # Key Metrics Section
        st.header("📈 Key Financial Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Total Revenue",
                value=f"${metrics['total_revenue']:,.0f}",
                delta=f"{metrics['revenue_growth']:+.1f}%"
            )
        
        with col2:
            st.metric(
                label="Net Profit",
                value=f"${metrics['net_profit']:,.0f}",
                delta=f"{metrics['profit_growth']:+.1f}%"
            )
        
        with col3:
            st.metric(
                label="Profit Margin",
                value=f"{metrics['profit_margin']:.1f}%"
            )
        
        with col4:
            st.metric(
                label="ROE",
                value=f"{metrics['roe']:.1f}%"
            )
        
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
        st.header("📋 Raw Data")
        
        # Add filters
        col1, col2 = st.columns(2)
        
        with col1:
            date_range = st.date_input(
                "Select Date Range",
                value=(df['Date'].min(), df['Date'].max()),
                min_value=df['Date'].min(),
                max_value=df['Date'].max()
            )
        
        with col2:
            selected_columns = st.multiselect(
                "Select Columns",
                df.columns.tolist(),
                default=df.columns.tolist()
            )
        
        # Filter data
        if len(date_range) == 2:
            filtered_df = df[
                (df['Date'].dt.date >= date_range[0]) &
                (df['Date'].dt.date <= date_range[1])
            ]
        else:
            filtered_df = df
        
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
            label="📥 Download Data as CSV",
            data=csv,
            file_name="financial_data.csv",
            mime="text/csv"
        )
        
    else:
        st.error("❌ Unable to load data. Please check your Google Sheets configuration.")

if __name__ == "__main__":
    main() 