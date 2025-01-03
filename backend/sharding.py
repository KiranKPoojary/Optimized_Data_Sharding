import pandas as pd
import hashlib
import os

SHARDS_FOLDER = 'shards'


def perform_sharding(filepath, algorithm):
    data = pd.read_csv(filepath)

    if algorithm == 'hash':
        data['Shard'] = data['ID'].apply(lambda x: int(hashlib.md5(str(x).encode()).hexdigest(), 16) % 5)
    elif algorithm == 'kmeans':
        from sklearn.cluster import KMeans
        data['Shard'] = KMeans(n_clusters=5).fit_predict(data[['Value']])
    elif algorithm == 'dbscan':
        from sklearn.cluster import DBSCAN
        data['Shard'] = DBSCAN(eps=0.5, min_samples=5).fit_predict(data[['Value']])

    for shard_id in data['Shard'].unique():
        shard_data = data[data['Shard'] == shard_id]
        shard_path = os.path.join(SHARDS_FOLDER, f"shard_{shard_id}.csv")
        shard_data.to_csv(shard_path, index=False)
