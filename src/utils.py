import json
import os

def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_collections_root():
    # Assumes collections are stored in ./collections/
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "collections")

def get_collection_dirs(root):
    # Only returns subdirectories in the collections root
    return [os.path.join(root, d) for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
