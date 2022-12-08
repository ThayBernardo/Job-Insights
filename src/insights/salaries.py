from typing import Union, List, Dict
from .jobs import read
import math


def get_max_salary(path: str) -> int:
    all_items = read(path)
    salary = int()
    for money in all_items:
        if (money["max_salary"].isnumeric()):
            if (salary < int(money["max_salary"])):
                salary = int(money["max_salary"])
    return salary


def get_min_salary(path: str) -> int:
    all_items = read(path)
    salary = math.inf
    for money in all_items:
        if (money["min_salary"].isnumeric()):
            if (salary > int(money["min_salary"])):
                salary = int(money["min_salary"])
    return salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    # Tive ajuda na resolução do exercicio
    if (
        # Por que dessa forma type(job["min_salary"]) is not int não funciona ?
        # type(job.get("min_salary")) is not int
        # or type(job.get("max_salary")) is not int
        "min_salary" not in job
        or "max_salary" not in job
        or str(job["max_salary"]).isdigit() is False
        or str(job["min_salary"]).isdigit() is False
        # isinstance verifica se o primeiro parametro é de algum dos tipos
        # do segundo parametro
        or isinstance(salary, (int, str)) is False
        or int(job["min_salary"]) > int(job["max_salary"])
    ):
        raise ValueError
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    list_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs.append(job)
        except ValueError:
            pass
    return list_jobs
