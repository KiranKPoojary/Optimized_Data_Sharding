import os
import pandas as pd

SHARDS_FOLDER = 'shards'

def get_metadata():
    metadata = []
    for shard_file in os.listdir(SHARDS_FOLDER):
        shard_path = os.path.join(SHARDS_FOLDER, shard_file)
        shard_data = pd.read_csv(shard_path)
        metadata.append({
            "shard_file": shard_file,
            "rows": len(shard_data),
            "columns": list(shard_data.columns)
        })
    return metadata
