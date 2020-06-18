from typing import List
from .animals_data import animals_questions, AnimalsCatogories, animals_metadata, Animals


def get_questions():
    return animals_questions

def identify_animal(categories: List[AnimalsCatogories]):
    print("categories", categories)
    possible_animals = []
    for animal in Animals:
        possible_animals.append(animal.value)
    for category in categories: 
        print("idx", category['idx'])
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
    print("**possible animals", possible_animals)
    if len(possible_animals) == 1:
        return possible_animals
    return None
    