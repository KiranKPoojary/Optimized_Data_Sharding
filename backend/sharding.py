import pandas as pd
import hashlib
import os
import logging

SHARDS_FOLDER = 'shards'
os.makedirs(SHARDS_FOLDER, exist_ok=True)


def perform_sharding(filepath, algorithm):
    logging.debug(f"Reading file: {filepath}")
    data = pd.read_csv(filepath)

    logging.debug(f"CSV Columns: {list(data.columns)}")

    # Ensure 'ID' column exists
    if 'ID' not in data.columns:
        logging.warning("'ID' column not found. Adding default index-based 'ID' column.")
        data['ID'] = range(1, len(data) + 1)

    # Handle Sharding based on Algorithm
    if algorithm == 'hash':
        logging.info("Using Hash-based sharding.")
        data['Shard'] = data['ID'].apply(lambda x: int(hashlib.md5(str(x).encode()).hexdigest(), 16) % 5)

    elif algorithm == 'kmeans':
        from sklearn.cluster import KMeans

        # Use numeric columns for KMeans clustering
        numeric_columns = data.select_dtypes(include='number').columns
        if len(numeric_columns) == 0:
            raise KeyError(f"No numeric columns found for KMeans clustering. Columns: {list(data.columns)}")

        logging.info(f"Using KMeans with columns: {list(numeric_columns)}")
        data['Shard'] = KMeans(n_clusters=5, random_state=42).fit_predict(data[numeric_columns])

    elif algorithm == 'dbscan':
        from sklearn.cluster import DBSCAN

        # Use numeric columns for DBSCAN clustering
        numeric_columns = data.select_dtypes(include='number').columns
        if len(numeric_columns) == 0:
            raise KeyError(f"No numeric columns found for DBSCAN clustering. Columns: {list(data.columns)}")

        logging.info(f"Using DBSCAN with columns: {list(numeric_columns)}")
        data['Shard'] = DBSCAN(eps=0.5, min_samples=5).fit_predict(data[numeric_columns])

    else:
        raise ValueError("Invalid sharding algorithm. Choose 'hash', 'kmeans', or 'dbscan'.")

    # Save each shard
    for shard_id in data['Shard'].unique():
        shard_data = data[data['Shard'] == shard_id]
        shard_path = os.path.join(SHARDS_FOLDER, f"shard_{shard_id}.csv")
        shard_data.to_csv(shard_path, index=False)
        logging.debug(f"Shard saved: {shard_path}")
