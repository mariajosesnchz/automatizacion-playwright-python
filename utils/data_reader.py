import json

def cargar_datos():
    with open("utils/data.json", "r", encoding="utf-8") as f:
        return json.load(f)