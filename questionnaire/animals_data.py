import enum


class Animals(enum.Enum):
    daddylonglegs = 1
    bee = 2
    penguin = 3
    eagle = 4
    giraffe = 5
    octopus = 6
    tiger = 7
    elephant = 8
    jellyfish = 9
    bull = 10
    parrot = 11
    dolphin = 12
    python = 13
    crocodile = 14
    cat = 15
    leopard = 16
    monkey = 17
    zebra = 18
    sheep = 19
    rat = 20
    owl = 21
    spider = 22
    frog = 23
    polarbear = 24
    snail = 25
    tortoise = 26
    rabbit = 27
    salmon = 28
    rhino = 29
    fox = 30


class AnimalsCatogories(enum.Enum):
    Mammals = 1
    FLYING_ANIMALS = 2
    WATER_ANIMALS = 3
    BEAK = 4
    NOCTURNAL_ANIMALS = 5
    SHELL_ANIMALS = 6
    SLITHERING_ANIMALS = 7
    WHISKERS = 8
    PAWS = 9
    STRIPES = 10
    FUR = 11
    FOURLEGGED_ANIMALS = 12
    STINGING_ANIMALS = 13
    TAIL = 14
    SCALES = 15
    CARNIVORES = 16
    SPOTS = 17
    GILLS = 18
    HORNS = 19
    FEATHERS = 20


animals_metadata = {
    AnimalsCatogories.Mammals: [
        Animals.giraffe,
        Animals.tiger,
        Animals.elephant,
        Animals.bull,
        Animals.dolphin,
        Animals.cat,
        Animals.leopard,
        Animals.monkey,
        Animals.zebra,
        Animals.sheep,
        Animals.rat,
        Animals.polarbear,
        Animals.rabbit,
        Animals.rhino,
        Animals.fox
    ],
    AnimalsCatogories.FLYING_ANIMALS: [
        Animals.daddylonglegs,
        Animals.bee,
        Animals.eagle
    ],
    AnimalsCatogories.WATER_ANIMALS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.BEAK: [
        Animals.penguin,
        Animals.eagle,
        Animals.parrot,
        Animals.owl
    ],
    AnimalsCatogories.NOCTURNAL_ANIMALS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.SHELL_ANIMALS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.SLITHERING_ANIMALS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.WHISKERS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.PAWS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino,
    ],
    AnimalsCatogories.STRIPES: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.FUR: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.FOURLEGGED_ANIMALS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.STINGING_ANIMALS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.TAIL: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.SCALES: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.CARNIVORES: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.SPOTS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.GILLS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ],
    AnimalsCatogories.HORNS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.rhino,
        Animals.fox
    ],
    AnimalsCatogories.FEATHERS: [
        Animals.penguin,
        Animals.octopus,
        Animals.jellyfish,
        Animals.dolphin,
        Animals.crocodile,
        Animals.frog,
        Animals.polarbear,
        Animals.tortoise,
        Animals.salmon,
        Animals.rhino
    ]
}

animals_questions = [
    {
        'idx': 1,
        'key': AnimalsCatogories.Mammals.value,
        'keyName': AnimalsCatogories.Mammals.name,
        'text': 'Is your animal a mammal?'
    },
    {
        'idx': 2,
        'key': AnimalsCatogories.FLYING_ANIMALS.value,
        'keyName': AnimalsCatogories.FLYING_ANIMALS.name,
        'text': 'Does your animal fly?'
    },
    {
        'idx': 3,
        'key': AnimalsCatogories.WATER_ANIMALS.value,
        'keyName': AnimalsCatogories.WATER_ANIMALS.name,
        'text': 'Does you your animal live in water only or on land & in water?'
    },
    {
        'idx': 4,
        'key': AnimalsCatogories.BEAK.value,
        'keyName': AnimalsCatogories.BEAK.name,
        'text': 'Does your animal have a beak?'
    },
    {
        'idx': 5,
        'key': AnimalsCatogories.NOCTURNAL_ANIMALS.value,
        'keyName': AnimalsCatogories.NOCTURNAL_ANIMALS.name,
        'text': 'Is your animal nocturnal?'
    },
    {
        'idx': 6,
        'key': AnimalsCatogories.SHELL_ANIMALS.value,
        'keyName': AnimalsCatogories.SHELL_ANIMALS.name,
        'text': 'Does your animal have a shell?'
    },
    {
        'idx': 7,
        'key': AnimalsCatogories.SLITHERING_ANIMALS.value,
        'keyName': AnimalsCatogories.SLITHERING_ANIMALS.name,
        'text': 'Does your animal slither?'
    },
    {
        'idx': 8,
        'key': AnimalsCatogories.WHISKERS.value,
        'keyName': AnimalsCatogories.WHISKERS.name,
        'text': 'Does your animal have whiskers?'
    },
    {
        'idx': 9,
        'key': AnimalsCatogories.PAWS.value,
        'keyName': AnimalsCatogories.PAWS.name,
        'text': 'Does your animal have paws?'
    },
    {
        'idx': 10,
        'key': AnimalsCatogories.STRIPES.value,
        'keyName': AnimalsCatogories.STRIPES.name,
        'text': 'Does your animal have stripes?'
    },
    {
        'idx': 11,
        'key': AnimalsCatogories.FUR.value,
        'keyName': AnimalsCatogories.FUR.name,
        'text': 'Does your animal have fur?'
    },
    {
        'idx': 12,
        'key': AnimalsCatogories.FOURLEGGED_ANIMALS.value,
        'keyName': AnimalsCatogories.FOURLEGGED_ANIMALS.name,
        'text': 'Does your animal have four legs?'
    },
    {
        'idx': 13,
        'key': AnimalsCatogories.STINGING_ANIMALS.value,
        'keyName': AnimalsCatogories.STINGING_ANIMALS.name,
        'text': 'Can your animal sting? '
    },
    {
        'idx': 14,
        'key': AnimalsCatogories.TAIL.value,
        'keyName': AnimalsCatogories.TAIL.name,
        'text': 'Does your animal have a tail?'
    },
    {
        'idx': 15,
        'key': AnimalsCatogories.SCALES.value,
        'keyName': AnimalsCatogories.SCALES.name,
        'text': 'Does your animal have horns or tusks'
    },
    {
        'idx': 16,
        'key': AnimalsCatogories.CARNIVORES.value,
        'keyName': AnimalsCatogories.CARNIVORES.name,
        'text': 'Is your animal a carnivore?'
    },
    {
        'idx': 17,
        'key': AnimalsCatogories.SPOTS.value,
        'keyName': AnimalsCatogories.SPOTS.name,
        'text': 'Does your animal have patterned spots?'
    },
    {
        'idx': 18,
        'key': AnimalsCatogories.GILLS.value,
        'keyName': AnimalsCatogories.GILLS.name,
        'text': 'Does your animal have gills?'
    },
    {
        'idx': 19,
        'key': AnimalsCatogories.HORNS.value,
        'keyName': AnimalsCatogories.HORNS.name,
        'text': 'Does your animal have horns or tusks?'
    },
    {
        'idx': 20,
        'key': AnimalsCatogories.FEATHERS.value,
        'keyName': AnimalsCatogories.FEATHERS.name,
        'text': 'Does your animal have feathers?'
    }
]
