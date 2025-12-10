#!/usr/bin/env python3
"""Script to create a sample Excel file for testing."""
import pandas as pd

# Create sample user data
data = {
    'id': ['1', '2', '3'],
    'name': ['John Doe', 'Jane Smith', 'Bob Johnson'],
    'email': ['john@example.com', 'jane@example.com', 'bob@example.com'],
    'phone': ['123-456-7890', '098-765-4321', '555-123-4567'],
    'role': ['admin', 'user', 'user']
}

df = pd.DataFrame(data)
df.to_excel('sample_users.xlsx', index=False)
print("✅ Sample Excel file created: sample_users.xlsx")
print(f"   Contains {len(df)} sample users")

