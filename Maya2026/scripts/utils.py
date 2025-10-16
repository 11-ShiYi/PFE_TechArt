import os, json

def write_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def get_root_dir():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  
    return base_dir