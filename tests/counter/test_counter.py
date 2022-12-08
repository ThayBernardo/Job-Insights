from src.pre_built.counter import count_ocurrences


def test_counter():
    word = 'Python'
    assert count_ocurrences('data/jobs.csv', word.casefold()) == 1639
