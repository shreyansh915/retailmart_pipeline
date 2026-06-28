import pandas as pd
import numpy as np

# Creating mock products
products_data = {
    'product_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'product_name': ['Tata Salt 1kg', 'Maggi 2-Min Noodles', 'Britannia Marie Gold', 'Fortune Mustard Oil', 
                    'Amul Butter 500g', 'Catch Turmeric Powder', 'Aashirvaad Atta 5kg', 'Surf Excel Easy Wash',
                    'Dettol Liquid Handwash', 'Taj Mahal Tea 250g'],
    'category': ['Grocery', 'Packaged Foods', 'Bakery', 'Cooking Medium', 'Dairy', 
                 'Spices', 'Grocery', 'Household', 'Personal Care', 'Beverages'],
    'price': [28.0, 14.0, 40.0, 175.0, 275.0, 32.0, 260.0, 140.0, 99.0, 150.0]
}
pd.DataFrame(products_data).to_csv('products.csv', index=False)

# Creating mock stores
stores_data = {
    'store_id': [1, 2, 3, 4, 5],
    'store_name': ['RetailMart Malviya Nagar', 'RetailMart Connaught Place', 'RetailMart Indiranagar', 'RetailMart Andheri West', 'RetailMart Salt Lake'],
    'city': ['Jaipur', 'Delhi', 'Bangalore', 'Mumbai', 'Kolkata'],
    'region': ['North', 'North', 'South', 'West', 'East']
}
pd.DataFrame(stores_data).to_csv('stores.csv', index=False)

# Creating messy sales data (with 15 rows, missing values, and duplicates)
sales_data = {
    'sale_id': [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2011, 2012, 2013, 2013],
    'store_id': [1, 2, 3, 1, 4, 5, 2, 3, 4, 1, 5, 5, 2, 3, 3],
    'product_id': [101, 103, 102, 105, 104, 107, 106, 109, 108, 110, 102, 102, 105, 101, 101],
    'quantity': [2, 1, np.nan, 1, 3, 2, 1, np.nan, 2, 1, 4, 4, 1, 5, 5],
    'sale_date': ['2026-06-20', '2026-06-20', '2026-06-21', '2026-06-21', '2026-06-21', 
                 '2026-06-22', '2026-06-22', '2026-06-22', '2026-06-23', '2026-06-23', 
                 '2026-06-24', '2026-06-24', '2026-06-24', '2026-06-24', '2026-06-24'],
    'amount': [56.0, 40.0, 14.0, np.nan, 525.0, 520.0, 32.0, 99.0, np.nan, 150.0, 56.0, 56.0, 275.0, 140.0, 140.0]
}
pd.DataFrame(sales_data).to_csv('sales_data.csv', index=False)
print("Mock datasets generated successfully with intentional anomalies.")
