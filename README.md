# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

My version of the Music Recommender Simulation will use a simple content-based recommendation approach. The system will compare a user's taste profile with each song's attributes, such as genre, mood, energy, tempo, valence, danceability, and acousticness. Instead of using a real machine-learning model, the recommender will calculate a weighted score for each song and rank the songs from most to least relevant. The goal is to show how data can be transformed into personalized predictions using clear rules.

---

## How The System Works

Real-world music platforms such as Spotify, YouTube, and TikTok use different types of data to predict what users may enjoy next. They may use behavioral information such as likes, skips, replays, listening time, playlist additions, shares, and search history. They can also use information about the music itself, including genre, mood, tempo, energy, valence, danceability, and acousticness.

Collaborative filtering makes recommendations based on patterns from multiple users. For example, if two users enjoy many of the same songs, the system may recommend songs that one user liked to the other user. Content-based filtering instead compares the attributes of songs with the preferences stored in a user's taste profile.

My recommender will use content-based filtering. Each song will be compared with the user's preferred genre, mood, energy, tempo, valence, and danceability. The system will calculate a weighted relevance score for each song, rank all songs from highest score to lowest score, and return the strongest matches.

### Song Data

Each `Song` object will store:

- `id`
- `title`
- `artist`
- `genre`
- `mood`
- `energy`
- `tempo_bpm`
- `valence`
- `danceability`
- `acousticness`

The `id`, `title`, and `artist` identify the song. The remaining attributes describe the song's musical style and vibe. The first version of the recommender will primarily score genre, mood, energy, tempo, valence, and danceability. Acousticness may be used in a later experiment or future improvement.

### UserProfile Features

Each `UserProfile` object will store:

- `preferred_genre`
- `preferred_mood`
- `preferred_energy`
- `preferred_tempo_bpm`
- `preferred_valence`
- `preferred_danceability`

These preferences describe the kind of musical experience the user wants. For example, one user may prefer happy, high-energy, danceable pop music, while another may prefer relaxed, low-energy lofi music.

### Algorithm Recipe

The recommender will calculate a weighted score for every song:

- Genre match: 25 points
- Mood match: 20 points
- Energy closeness: up to 20 points
- Valence closeness: up to 15 points
- Danceability closeness: up to 10 points
- Tempo closeness: up to 10 points

The maximum possible score is 100 points.

Genre and mood are categorical features, so the system will award points when the values match the user's preferences. Energy, valence, danceability, and tempo are numerical features, so the system will award more points when the song's values are closer to the user's preferred values.

The system will not assume that higher values are always better. For example, a user who prefers an energy level of `0.30` should receive more points for a song with an energy level of `0.35` than for a song with an energy level of `0.95`.

After calculating a score for every song, the recommender will sort all songs from highest score to lowest score and return the top-ranked songs.

### Scoring Rule vs. Ranking Rule

The scoring rule evaluates one song at a time. It answers the question: "How closely does this song match the user's taste profile?" The system calculates the score by comparing the song's attributes with the user's preferences and applying the selected weights.

The ranking rule is used after every song receives a score. It sorts the complete list of songs from highest score to lowest score so that the strongest matches appear first. The recommender then selects the top results from that ranked list.

### Recommendation Flow

User taste profile  
→ Compare the profile with each song  
→ Calculate a weighted relevance score  
→ Repeat for every song in the catalog  
→ Rank all songs from highest to lowest score  
→ Return the top recommendations

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



