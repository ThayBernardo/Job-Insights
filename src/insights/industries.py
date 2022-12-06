from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    all = read(path)
    unique_industries = set()
    for industry in all:
        if industry["industry"] != '':
            unique_industries.add(industry["industry"])
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    types = []
    for indu in jobs:
        if (indu["industry"] == industry):
            types.append(indu)
    return types
