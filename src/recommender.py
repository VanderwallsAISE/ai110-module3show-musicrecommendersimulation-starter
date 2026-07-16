import csv
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and return a list of typed song dicts."""
    path = Path(csv_path)
    if not path.is_absolute():
        project_root = Path(__file__).resolve().parent.parent
        path = (project_root / csv_path).resolve()

    if not path.is_file():
        raise FileNotFoundError(f"Could not find songs CSV file at: {path}")

    songs: List[Dict] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_number, row in enumerate(reader, start=2):
            try:
                songs.append({
                    "id": int(row["id"].strip()),
                    "title": row["title"].strip(),
                    "artist": row["artist"].strip(),
                    "genre": row["genre"].strip(),
                    "mood": row["mood"].strip(),
                    "energy": float(row["energy"].strip()),
                    "tempo_bpm": int(row["tempo_bpm"].strip()),
                    "valence": float(row["valence"].strip()),
                    "danceability": float(row["danceability"].strip()),
                    "acousticness": float(row["acousticness"].strip()),
                })
            except (ValueError, KeyError) as e:
                raise ValueError(
                    f"Invalid data in {path} on line {line_number}: {row} ({e})"
                ) from e

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate one song's weighted score and return its reasons."""
    score = 0.0
    reasons: List[str] = []

    # Categorical features
    if song["mood"].strip().lower() == user_prefs["favorite_mood"].strip().lower():
        score += 20.0
        reasons.append("mood match (+20.00)")

    if song["genre"].strip().lower() == user_prefs["favorite_genre"].strip().lower():
        score += 15.0
        reasons.append("genre match (+15.00)")

    # Numerical features already measured from 0.0 to 1.0
    energy_points = (
        max(0.0, 1.0 - abs(song["energy"] - user_prefs["target_energy"]))
        * 20.0
    )
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    valence_points = (
        max(0.0, 1.0 - abs(song["valence"] - user_prefs["target_valence"]))
        * 15.0
    )
    score += valence_points
    reasons.append(f"valence closeness (+{valence_points:.2f})")

    danceability_points = (
        max(
            0.0,
            1.0
            - abs(
                song["danceability"]
                - user_prefs["target_danceability"]
            ),
        )
        * 10.0
    )
    score += danceability_points
    reasons.append(
        f"danceability closeness (+{danceability_points:.2f})"
    )

    acousticness_points = (
        max(
            0.0,
            1.0
            - abs(
                song["acousticness"]
                - user_prefs["target_acousticness"]
            ),
        )
        * 10.0
    )
    score += acousticness_points
    reasons.append(
        f"acousticness closeness (+{acousticness_points:.2f})"
    )

    # Tempo uses BPM, so normalize its difference
    tempo_points = (
        max(
            0.0,
            1.0
            - abs(
                song["tempo_bpm"]
                - user_prefs["target_tempo_bpm"]
            )
            / 100.0,
        )
        * 10.0
    )
    score += tempo_points
    reasons.append(f"tempo closeness (+{tempo_points:.2f})")

    return round(score, 2), reasons

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return the top k ranked recommendations."""
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)

        scored_songs.append(
            (song, score, explanation)
        )

    ranked_songs = sorted(
        scored_songs,
        key=lambda recommendation: recommendation[1],
        reverse=True,
    )

    return ranked_songs[:k]
