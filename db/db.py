from pathlib import Path
import json


DB = Path("/db/data/users.json")


def get_by_id(id: int):
    with open(DB, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for user in data:
            if user["id"] == id:
                return user
        return None


def write_to_db(id, role, name, group_id = None, lecturer_id = None, lang = "uk"):
    payload = {
        "id": id,
        "role": role,
        "name": name,
        "lang": lang,
    }

    if group_id is None and lecturer_id is None:
        raise Exception("You must specify group_id or lecturer_id")
    elif group_id is not None and lecturer_id is not None:
        raise Exception("You cannot specify both group_id and lecturer_id")
    else:
        if group_id is not None:
            payload["group_id"] = group_id
        elif lecturer_id is not None:
            payload["lecturer_id"] = lecturer_id

    with open(DB, 'r+', encoding='utf-8') as f:
        data = json.load(f)
        data.append(payload)

        f.truncate()
        f.seek(0)
        json.dump(payload, f, ensure_ascii=False, indent=2)