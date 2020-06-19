from typing import List
from .animals_data import animals_questions, AnimalsCatogories, animals_metadata, Animals


def get_questions():
    return animals_questions

def identify_animal(categories: List[AnimalsCatogories]):
    possible_animals = []
    for animal in Animals:
        possible_animals.append(animal.value)
    for category in categories: 
        idx = category['idx']
        ans = category['ans']
        if ans == 1:
            for animal in possible_animals:
                if animal not in animals_metadata[idx]:
                    possible_animals.remove(animal)
        else:
            for animal in possible_animals:
                if animal in animals_metadata[idx]:
                    possible_animals.remove(animal)
    animal_names = []
    for animal in possible_animals:
        animal_names.append(Animals(animal).name)
    if len(animal_names):
        return animal_names
    return None
    