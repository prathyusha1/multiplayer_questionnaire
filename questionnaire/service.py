from typing import List
from .animals_data import animals_questions, AnimalsCatogories, animals_metadata


def get_questions():
    return animals_questions

def identify_animal(categories: List[AnimalsCatogories]):
    category_animals = []
    for category in categories:
        category_animals.append(animals_metadata[category])
    intersection_list = set.intersection(*category_animals)
    if len(intersection_list) == 1:
        return intersection_list[0]
    return None
    