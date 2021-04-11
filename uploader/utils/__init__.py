import json
import os


def load_json(filename: str):
    base_dir = os.path.split(__file__)[0]
    data_path = os.path.join(base_dir, filename)
    with open(data_path, "r", encoding="utf-8") as data:
        json_data = json.load(data)
        return json_data
