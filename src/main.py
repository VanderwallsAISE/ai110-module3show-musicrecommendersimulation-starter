"""
Command-line runner for the Music Recommender Simulation.
"""

from .recommender import load_songs, recommend_songs


def display_recommendations(
    profile_name: str,
    user_prefs: dict,
    songs: list[dict],
) -> None:
    """Display the top five recommendations for one user profile."""
    recommendations = recommend_songs(
        user_prefs,
        songs,
        k=5,
    )

    print("=" * 70)
    print(f"PROFILE: {profile_name}")
    print("=" * 70)

    for position, recommendation in enumerate(
        recommendations,
        start=1,
    ):
        song, score, explanation = recommendation

        print(
            f"{position}. {song['title']} "
            f"by {song['artist']}"
        )
        print(f"   Genre: {song['genre']}")
        print(f"   Mood: {song['mood']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print()


def main() -> None:
    """Load the catalog and evaluate several user profiles."""
    songs = load_songs("data/songs.csv")

    print(f"Loaded songs: {len(songs)}\n")

    profiles = {
        "High-Energy Happy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.80,
            "target_tempo_bpm": 120,
            "target_valence": 0.80,
            "target_danceability": 0.80,
            "target_acousticness": 0.15,
        },

        "Chill Lofi Study Music": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.35,
            "target_tempo_bpm": 75,
            "target_valence": 0.55,
            "target_danceability": 0.55,
            "target_acousticness": 0.80,
        },

        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.92,
            "target_tempo_bpm": 150,
            "target_valence": 0.45,
            "target_danceability": 0.65,
            "target_acousticness": 0.08,
        },

        # Edge case: the labels say chill lofi,
        # but the numerical targets describe intense workout music.
        "Conflicting High-Energy Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.95,
            "target_tempo_bpm": 150,
            "target_valence": 0.75,
            "target_danceability": 0.85,
            "target_acousticness": 0.75,
        },
    }

    for profile_name, user_prefs in profiles.items():
        display_recommendations(
            profile_name,
            user_prefs,
            songs,
        )


if __name__ == "__main__":
    main()