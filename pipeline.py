import os
import sqlite3
import pandas as pd
import numpy as np

def run_pipeline():
    db_name = 'retail_mart.db'
    
    # 1. Ingestion
    if not (os.path.exists('sales_data.csv') and os.path.exists('products.csv') and os.path.exists('stores.csv')):
        print("[Error] Missing raw CSV files. Run generate_data.py first.")
        return
        
    sales_df = pd.read_csv('sales_data.csv')
    products_df = pd.read_csv('products.csv')
    stores_df = pd.read_csv('stores.csv')
    
    # Print shapes
    print(f"Initial Shapes -> Sales: {sales_df.shape}, Products: {products_df.shape}, Stores: {stores_df.shape}\n")
    
    # --- ADDED: Print the first 5 rows of each DataFrame ---
    print("--- Sales Data (First 5 Rows) ---")
    print(sales_df.head(5), "\n")
    
    print("--- Products Data (First 5 Rows) ---")
    print(products_df.head(5), "\n")
    
    print("--- Stores Data (First 5 Rows) ---")
    print(stores_df.head(5), "\n")
    # ------------------------------------------------------
    
    # Check for missing values
    print("--- Sales Missing Value Summary ---")
    print(sales_df.isnull().sum(), "\n")
    
    print("--- Products Missing Value Summary ---")
    print(products_df.isnull().sum(), "\n")
    
    print("--- Stores Missing Value Summary ---")
    print(stores_df.isnull().sum(), "\n")
    
    # 2. Data Cleaning
    initial_rows = len(sales_df)
    sales_df.drop_duplicates(inplace=True)
    dupes_removed = initial_rows - len(sales_df)
    print(f"Removed {dupes_removed} duplicate rows.")

    sales_df['quantity'] = sales_df['quantity'].fillna(0)
    sales_df.dropna(subset=['amount'], inplace=True)
    
    sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])
    sales_df['amount'] = sales_df['amount'].astype(float)
    print(f"Cleaned Sales Shape: {sales_df.shape}\n")

    # 3. Transformation
    merged_df = sales_df.merge(products_df, on='product_id', how='inner')
    merged_df = merged_df.merge(stores_df, on='store_id', how='inner')
    
    merged_df['total_revenue'] = merged_df['quantity'] * merged_df['price']
    
    rev_array = merged_df['total_revenue'].to_numpy()
    print(f"Revenue Stats -> Mean: {np.mean(rev_array):.2f}, Max: {np.max(rev_array)}, Min: {np.min(rev_array)}\n")
    
    print("--- Total Revenue by City ---")
    city_rev = merged_df.groupby('city')['total_revenue'].sum().sort_values(ascending=False)
    print(city_rev, "\n")

    # 4. Loading to SQLite
    try:
        conn = sqlite3.connect(db_name)
        merged_df.to_sql('retail_sales', conn, if_exists='replace', index=False)
        
        # SQL Query: Top 3 best-selling products
        top_products_query = """
            SELECT product_name, SUM(quantity) as total_qty 
            FROM retail_sales 
            GROUP BY product_name 
            ORDER BY total_qty DESC 
            LIMIT 3;
        """
        print("--- Top 3 Best-Selling Products (SQL) ---")
        print(pd.read_sql(top_products_query, conn), "\n")
        
        # 5. Reporting Insights
        store_daily_query = """
            SELECT store_name, sale_date, SUM(total_revenue) as daily_revenue 
            FROM retail_sales 
            GROUP BY store_name, sale_date;
        """
        print("--- Daily Revenue Per Store (SQL) ---")
        print(pd.read_sql(store_daily_query, conn).head(5), "\n")
        
        print("================ SUMMARY REPORT ================")
        print(f"Total Transactions : {len(merged_df)}")
        print(f"Total Revenue      : INR {merged_df['total_revenue'].sum():.2f}")
        print(f"Top Selling City   : {city_rev.index[0]} (INR {city_rev.values[0]:.2f})")
        
        top_prod = merged_df.groupby('product_name')['quantity'].sum().idxmax()
        print(f"Top Selling Product: {top_prod}")
        print("================================================")
        
    except sqlite3.Error as e:
        print(f"[Database Error] Failures occurred during database execution: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    run_pipeline()
