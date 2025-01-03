import pandas as pd
import hashlib
import os
import logging

SHARDS_FOLDER = 'shards'
os.makedirs(SHARDS_FOLDER, exist_ok=True)


def perform_sharding(filepath, algorithm):
    logging.debug(f"Reading file: {filepath}")
    data = pd.read_csv(filepath)

    # Print column names for debugging
    logging.debug(f"CSV Columns: {list(data.columns)}")

    # Add 'ID' column if not present
    if 'ID' not in data.columns:
        logging.warning("'ID' column not found. Adding default index-based 'ID' column.")
        data['ID'] = range(1, len(data) + 1)

    if algorithm == 'hash':
        data['Shard'] = data['ID'].apply(lambda x: int(hashlib.md5(str(x).encode()).hexdigest(), 16) % 5)
    elif algorithm == 'kmeans':
        from sklearn.cluster import KMeans
        if 'Value' not in data.columns:
            raise KeyError(f"'Value' column not found in the dataset. Columns present: {list(data.columns)}")
        data['Shard'] = KMeans(n_clusters=5).fit_predict(data[['Value']])
    elif algorithm == 'dbscan':
        from sklearn.cluster import DBSCAN
        if 'Value' not in data.columns:
            raise KeyError(f"'Value' column not found in the dataset. Columns present: {list(data.columns)}")
        data['Shard'] = DBSCAN(eps=0.5, min_samples=5).fit_predict(data[['Value']])

    for shard_id in data['Shard'].unique():
        shard_data = data[data['Shard'] == shard_id]
        shard_path = os.path.join(SHARDS_FOLDER, f"shard_{shard_id}.csv")
        shard_data.to_csv(shard_path, index=False)
        logging.debug(f"Shard saved: {shard_path}")
