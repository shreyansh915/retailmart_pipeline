RetailMart Daily Sales ETL Pipeline
A robust, modular, and human-engineered ETL (Extract, Transform, Load) pipeline designed for RetailMart Pvt. Ltd. to ingest, clean, and transform multi-source daily sales data into production-ready analytical tables.

📌 Project Overview
RetailMart collects daily transaction records across multiple Indian retail hubs. This pipeline automates the ingestion of raw, inconsistent CSV files, applies strict data-cleansing data rules, runs performance metrics calculations, and stores the structured output in an optimized SQLite relational database for seamless business intelligence reporting.

Data Architecture Flow
Extract: Ingests transactional data, product sheets, and store registries from local disk storage.
Transform: Drops relational duplicates, handles missing transactional attributes via structural imputation, standardizes schemas, and computes algorithmic retail metrics.
Load: Streams the finalized dimensional model directly into a local SQLite transactional schema.
🛠️ Tech Stack & Prerequisites
Language: Python 3.8+
Data Core: Pandas, NumPy
Database Engine: SQLite3 / SQLAlchemy
Ensure you have the required packages installed before executing the scripts:

pip install pandas numpy
python generate_data.py
python pipeline.py