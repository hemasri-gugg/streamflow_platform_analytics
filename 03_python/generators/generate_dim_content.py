import random

import numpy as np
import pandas as pd

NUM_CONTENT = 2000

GENRES = [
    "Drama",
    "Action",
    "Comedy",
    "Romance",
    "Thriller",
    "Documentary",
    "Sci-Fi",
    "Fantasy",
    "Crime",
    "Animation"
]

GENRE_WEIGHTS = [
    0.18,
    0.16,
    0.15,
    0.12,
    0.10,
    0.08,
    0.08,
    0.05,
    0.05,
    0.03
]

LANGUAGES = [
    "English",
    "Hindi",
    "Spanish",
    "French",
    "German",
    "Japanese",
    "Korean"
]

LANGUAGE_WEIGHTS = [
    0.45,
    0.20,
    0.10,
    0.08,
    0.06,
    0.06,
    0.05
]

CONTENT_TYPES = [
    "Movie",
    "Series"
]

AGE_RATINGS = [
    "U",
    "U/A 13+",
    "U/A 16+",
    "A"
]

ADJECTIVES = [
    "Hidden", "Dark", "Silent", "Lost", "Broken",
    "Golden", "Crimson", "Forgotten", "Final",
    "Ancient", "Midnight", "Last", "Infinite",
    "Burning", "Secret", "Shadow", "Frozen",
    "Rising", "Fallen", "Eternal"
]

GENRE_WORDS = {
    "Action": [
        "Strike", "Mission", "Target", "Warrior",
        "Hunter", "Assault", "Force", "Vengeance",
        "Outlaw", "Frontline"
    ],

    "Drama": [
        "Promise", "Journey", "Hope", "Legacy",
        "Memory", "Home", "Truth", "Destiny",
        "Letters", "Crossroads"
    ],

    "Comedy": [
        "Roommates", "Vacation", "Neighbors",
        "Wedding", "Chaos", "Weekend",
        "Family", "Office", "Adventure", "Party"
    ],

    "Romance": [
        "Heartbeat", "Forever", "Love",
        "Moonlight", "Promise", "Destiny",
        "Together", "Embrace", "Sunrise", "Melody"
    ],

    "Thriller": [
        "Witness", "Identity", "Evidence",
        "Escape", "Nightfall", "Conspiracy",
        "Silence", "Cipher", "Suspect", "Pursuit"
    ],

    "Documentary": [
        "Planet", "Wildlife", "History",
        "Ocean", "Earth", "Origins",
        "Innovation", "Nature", "Civilization",
        "Expedition"
    ],

    "Sci-Fi": [
        "Galaxy", "Protocol", "Nova",
        "Quantum", "Orbit", "Android",
        "Nebula", "Eclipse", "Cosmos", "Singularity"
    ],

    "Fantasy": [
        "Kingdom", "Dragon", "Realm",
        "Magic", "Prophecy", "Crown",
        "Sword", "Phoenix", "Empire", "Chronicles"
    ],

    "Crime": [
        "Cartel", "Detective", "Mafia",
        "Heist", "Evidence", "Informer",
        "Gang", "Justice", "Verdict", "Trial"
    ],

    "Animation": [
        "Adventure", "Friends", "Forest",
        "Dreamland", "Heroes", "Castle",
        "Journey", "Magic", "Wonder", "Village"
    ]
}

TITLE_PATTERNS = [
    "{adj} {noun}",
    "The {noun}",
    "{adj} {noun}: Part II",
    "{noun} of the {adj} World",
    "Beyond the {noun}",
    "Return to {noun}"
]


def generate_title(genre):
    adjective = random.choice(ADJECTIVES)
    noun = random.choice(GENRE_WORDS[genre])
    pattern = random.choice(TITLE_PATTERNS)

    return pattern.format(
        adj=adjective,
        noun=noun
    )


def generate_content():

    records = []

    used_titles = set()

    for content_id in range(1, NUM_CONTENT + 1):

        content_type = np.random.choice(
            CONTENT_TYPES,
            p=[0.70, 0.30]
        )

        genre = np.random.choice(
            GENRES,
            p=GENRE_WEIGHTS
        )

        while True:
            title = generate_title(genre)
            if title not in used_titles:
                used_titles.add(title)
                break

        duration = (
            random.randint(80, 180)
            if content_type == "Movie"
            else random.randint(250, 1200)
        )

        records.append({
            "content_id": content_id,
            "title": title,
            "content_type": content_type,
            "genre": genre,
            "language": np.random.choice(
                LANGUAGES,
                p=LANGUAGE_WEIGHTS
            ),
            "release_year": random.randint(1995, 2025),
            "duration_minutes": duration,
            "imdb_rating": round(random.uniform(5.0, 9.8), 1),
            "age_rating": random.choice(AGE_RATINGS),
            "exclusive_content": random.choice([True, False]),
            "popularity_score": round(random.uniform(1, 100), 2)
        })

    return pd.DataFrame(records)


if __name__ == "__main__":

    df = generate_content()

    print(df.head())

    df.to_csv("02_data/dim_content.csv", index=False)

    print("\nContent Generated Successfully!")