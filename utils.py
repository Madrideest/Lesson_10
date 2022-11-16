import json


def load_candidates():
    with open('data/candidates.json') as f:
        data = json.load(f)
    return data


def get_all():
    return load_candidates()


def get_by_pk(pk):
    data = load_candidates()
    for candidate in data:
        if candidate["pk"] == pk:
            return candidate


def get_by_skill(skill_name):
    data = load_candidates()

    candidate_by_skill = []

    for item in data:
        skills = item["skills"].lower().replace(' ', '').split(',')
        print(skills)
        if skill_name.lower() in skills or item["skills"].lower() == skill_name.lower():
            candidate_by_skill.append(item)

    return candidate_by_skill
