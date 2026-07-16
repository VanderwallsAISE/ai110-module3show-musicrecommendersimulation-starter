"""
Command-line runner for the Music Recommender Simulation.
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    """Load songs and display the top recommendations."""
    songs = load_songs("data/songs.csv")

    print(f"Loaded songs: {len(songs)}")

    # Default pop/happy taste profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_tempo_bpm": 120,
        "target_valence": 0.80,
        "target_danceability": 0.80,
        "target_acousticness": 0.15,
    }

    recommendations = recommend_songs(
        user_prefs,
        songs,
        k=5,
    )

    print("\nTop recommendations:\n")

    for position, recommendation in enumerate(
        recommendations,
        start=1,
    ):
        song, score, explanation = recommendation

        print(
            f"{position}. {song['title']} "
            f"by {song['artist']}"
        )
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()