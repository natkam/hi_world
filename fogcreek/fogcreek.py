"""
https://www.fogcreek.com/jobs/SupportEngineerLevel1
"""
from typing import List, Union, cast


def get_the_message(text: str) -> str:
    counted_letters_array: List[List[Union[str, int]]] = [
        [letter, text.count(letter)] for letter in "abcdefghijklmnopqrstuvwxyz_"
    ]
    sorted_letters_array = sorted(
        counted_letters_array, key=lambda letter: letter[1], reverse=True
    )
    message = read_till_underscore(sorted_letters_array)
    return message


def read_till_underscore(sorted_letters_array: List[List[Union[str, int]]]) -> str:
    i = 0
    word = ""
    while sorted_letters_array[i][0] != "_":
        word += cast("str", sorted_letters_array[i][0])
        i += 1
    return word


if __name__ == "__main__":
    with open("fogcreek.txt", "r") as f:
        text = f.read().strip()
    print(get_the_message(text))
