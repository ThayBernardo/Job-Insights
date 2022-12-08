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
        type(job.get("min_salary")) is not int
        or type(job.get("min_salary")) is not int
        # isinstance verifica se o primeiro parametro é de algum dos tipos
        # do segundo parametro
        or isinstance(salary, (int, float, str)) is False
        or ("min_salary" or "max_salary") not in job
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError
    return job["min_salary"] <= int(salary) <= job["max_salary"]


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    list_jobs = []
    for job in jobs:
        jobs_salary = {
            "min_salary": job["min_salary"],
            "max_salary": job["max_salary"]
        }
        job_actual = dict(jobs_salary)
        if matches_salary_range(job_actual, salary):
            list_jobs.append(job)
        else:
            raise ValueError
    return list_jobs
