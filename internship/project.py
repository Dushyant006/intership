import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Setup Parameters
np.random.seed(42)  # For reproducible results
num_days = 365
start_date = datetime(2025, 5, 25)  # 1 year of historical data
date_list = [start_date + timedelta(days=x) for x in range(num_days)]

# Corporate Structure Lookups
departments = ['Production', 'Development', 'Testing', 'Data Science']
services = ['Compute (EC2/VMs)', 'Storage (S3/Blob)', 'Database (RDS/SQL)', 'Networking']
regions = ['us-east-1', 'us-west-2', 'eu-west-1', 'ap-south-1']

# Resource pools to simulate persistent infrastructure
resource_pool = []
for i in range(1, 51):  # 50 unique servers/databases running in the company
    resource_pool.append({
        'id': f'res-{1000 + i}',
        'dept': np.random.choice(departments),
        'service': np.random.choice(services),
        'region': np.random.choice(regions)
    })

# 2. Generate Daily Records
data_rows = []

for current_date in date_list:
    # Introduce a massive billing spike on specific days (Simulating Anomaly)
    is_anomaly_day = (current_date.month == 10 and current_date.day in [12, 13, 14]) or \
                     (current_date.month == 2 and current_date.day == 5)
    
    for res in resource_pool:
        # Base cost depending on service type
        if res['service'] == 'Compute (EC2/VMs)':
            base_cost = np.random.uniform(20, 150)
            avg_cpu = np.random.uniform(5, 85)  # Normal distributed CPU
        elif res['service'] == 'Database (RDS/SQL)':
            base_cost = np.random.uniform(50, 300)
            avg_cpu = np.random.uniform(10, 60)
        elif res['service'] == 'Storage (S3/Blob)':
            base_cost = np.random.uniform(5, 40)
            avg_cpu = 0  # Storage doesn't use CPU
        else:  # Networking
            base_cost = np.random.uniform(10, 60)
            avg_cpu = 0

        # Injecting "Idle/Zombie" infrastructure rules
        # Let's force a couple of specific Development/Testing resources to always have low CPU but high cost
        if res['id'] in ['res-1005', 'res-1012', 'res-1028'] and res['dept'] in ['Development', 'Testing']:
            base_cost = np.random.uniform(250, 400)  # Very expensive
            avg_cpu = np.random.uniform(1, 4)        # Barely used!

        # Apply the anomaly spike multiplier if it matches our rogue dates
        if is_anomaly_day and res['id'] == 'res-1042':
            cost = base_cost * 15  # 15x cost explosion!
            avg_cpu = 98.5          # Maxed out server
        else:
            cost = base_cost

        # Append row
        data_rows.append({
            'Date': current_date.strftime('%Y-%m-%d'),
            'Resource_ID': res['id'],
            'Department': res['dept'],
            'Service_Type': res['service'],
            'Region': res['region'],
            'Daily_Cost_USD': round(cost, 2),
            'Avg_CPU_Utilization_Pct': round(avg_cpu, 2)
        })

# 3. Create DataFrame and Export
df = pd.DataFrame(data_rows)
df.to_csv('cloud_cost_data.csv', index=False)
print("🎯 Success! 'cloud_cost_data.csv' has been generated with hidden patterns for your dashboard.")