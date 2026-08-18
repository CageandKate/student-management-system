import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR /"data"/"students.json"


def load_students():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("学生数据文件格式错误")


def save_students(students):
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            students,
            f,
            ensure_ascii=False,
            indent=4
        )