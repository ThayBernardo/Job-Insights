from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        return list(csv.DictReader(file))


def get_unique_job_types(path: str) -> List[str]:
    all_jobs = read(path)
    unique_jobs = set()
    for jobs in all_jobs:
        unique_jobs.add(jobs["job_type"])
    return unique_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    types = []
    for job in jobs:
        if (job["job_type"] == job_type):
            types.append(job)
    return types
