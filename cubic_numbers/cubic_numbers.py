"""https://www.codewars.com/kata/hidden-cubic-numbers/python"""

import re
import typing


def find_legit_numbers(s: str) -> typing.List[str]:
    p = re.compile(r"\d{1,3}")
    words = p.findall(s)
    return words


def check_if_cubic(n: str) -> bool:
    if sum(map(lambda n: n ** 3, map(int, n))) == int(n):
        # the above is not the most readable solution, agreed xp
        return True
    else:
        return False


def is_sum_of_cubes(s: str) -> str:
    numbers = find_legit_numbers(s)
    if numbers:
        cubics = [number for number in numbers if check_if_cubic(number)]
        if cubics:
            return f'{" ".join(cubics)} {sum(map(int, cubics))} Lucky'
    return "Unlucky"


if __name__ == "__main__":
    assert is_sum_of_cubes("0 9026315 -827&()") == "0 0 Lucky"
    assert is_sum_of_cubes("aqdf& 0 1 xyz 153 777.777") == "0 1 153 154 Lucky"
    assert is_sum_of_cubes("No numbers!") == "Unlucky"
    assert is_sum_of_cubes("QK29 45[&erui") == "Unlucky"
