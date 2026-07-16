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

My recommender will use content-based filtering. Each song will be compared with the user's favorite genre, favorite mood, target energy, target tempo, target valence, target danceability, and target acousticness. The system will calculate a weighted relevance score for each song, rankence, target danceability, and target acoustic all songs from highest score to lowest score, and return the strongest matches.

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

The `id`, `title`, and `artist` fields identify the song and will be used for displaying recommendations. Genre and mood are categorical recommendation features. Energy, tempo, valence, danceability, and acousticness are numerical recommendation features. The recommender will use all seven recommendation features when calculating how closely each song matches the user's taste profile.

### UserProfile Features

Each `UserProfile` object will store:

- `favorite_genre`
- `favorite_mood`
- `target_energy`
- `target_tempo_bpm`
- `target_valence`
- `target_danceability`
- `target_acousticness`

The categorical preferences use `favorite_` because they represent the user's preferred categories. The numerical preferences use `target_` because the recommender will measure how close each song's numerical value is to the user's desired value.

These preferences describe the musical experience the user wants. For example, one user may prefer positive, high-energy, danceable gym music, while another may prefer relaxed, low-energy, highly acoustic lofi music.

### Example User Profile

The first test profile represents a user looking for energetic and motivating music for basketball or the gym:

- Favorite genre: `hip-hop`
- Favorite mood: `intense`
- Target energy: `0.90`
- Target tempo: `135 BPM`
- Target valence: `0.70`
- Target danceability: `0.75`
- Target acousticness: `0.10`

This profile should rank energetic, intense, rhythm-focused, and low-acousticness songs higher than calm, slow, or highly acoustic tracks.

### User Profile Evaluation

The AI critique confirmed that this profile should clearly distinguish intense gym music from chill lofi music. The target energy and tempo are high, while the target acousticness is low. Those preferences strongly favor active and heavily produced songs over calm, slow, and acoustic tracks.

The profile is specific, but it is not too narrow for this simulation because genre and mood are weighted bonuses rather than mandatory filters. A song does not need to match every preference perfectly to receive a strong total score.

Energy, valence, and danceability may be somewhat related, but they represent different qualities. Energy measures intensity, valence measures emotional positivity, and danceability measures rhythm and suitability for movement. Tempo adds information about speed, while acousticness distinguishes acoustic music from more electronic or heavily produced music.

One important correction was changing `hiphop` to `hip-hop` so that the user's favorite genre matches the exact spelling used in `songs.csv`.

### Algorithm Recipe

The recommender will calculate a weighted relevance score for every song using the following rules:

- Mood match: 20 points
- Genre match: 15 points
- Energy closeness: up to 20 points
- Valence closeness: up to 15 points
- Danceability closeness: up to 10 points
- Tempo closeness: up to 10 points
- Acousticness closeness: up to 10 points

The maximum possible score is 100 points.

Genre and mood are categorical features. A song receives the full category points when its value exactly matches the user's preference. For example, a song receives 15 genre points when its genre matches the user's favorite genre.

Energy, valence, danceability, tempo, and acousticness are numerical features. These features receive points based on closeness to the user's target value. A smaller difference produces more points, while a larger difference produces fewer points.

For features already measured from `0.0` to `1.0`, the system can calculate closeness using:

`closeness = 1 - absolute difference`

For example, if the user's target energy is `0.90` and a song's energy is `0.82`, the difference is `0.08`, so the closeness is `0.92`. The energy contribution would be `0.92 × 20 = 18.4` points.

The system will not assume that higher values are always better. If a user wants calm music with a target energy of `0.30`, a song with energy `0.35` should receive more points than a song with energy `0.95`.

Tempo must be normalized because it uses a different scale. Energy, valence, danceability, and acousticness range from `0.0` to `1.0`, while tempo is measured in beats per minute. Normalizing the tempo difference prevents tempo from dominating the other numerical features.

After calculating a score for every song, the recommender will sort all songs from highest score to lowest score and return the top-ranked songs.

### Expected Limitations and Biases

This recommender may create a filter bubble because it mainly rewards songs that already resemble the user's stated preferences. A user who prefers intense hip-hop may repeatedly receive energetic and rhythm-focused music while receiving fewer opportunities to discover calm, acoustic, classical, jazz, or other genres.

Exact category matching may also be too rigid. For example, `pop` and `indie pop` are related styles, but the first version may treat them as completely different because their strings are not identical.

The catalog is also small and partly synthetic. This means the available genres, moods, and numerical values strongly influence which recommendations can appear. A future version could use partial genre similarity and occasionally include one exploratory recommendation outside the user's normal preferences.

### Scoring Rule vs. Ranking Rule

The scoring rule evaluates one song at a time. It answers the question: "How closely does this song match the user's taste profile?" The system compares the song's genre, mood, energy, valence, danceability, tempo, and acousticness with the user's preferences and applies the assigned weights.

The ranking rule is applied only after every song has received a score. It sorts the complete list of songs from highest score to lowest score so that the strongest matches appear first. The recommender then selects the top three songs from the ranked list.

### Recommendation Flow

`songs.csv` and the user taste profile  
→ Load every song from the catalog  
→ Loop through the songs one at a time  
→ Check the genre and mood matches  
→ Calculate closeness for energy, valence, danceability, tempo, and acousticness  
→ Multiply each result by its assigned weight  
→ Combine all points into one total relevance score  
→ Store each song with its score  
→ Sort all songs from highest score to lowest score  
→ Return the top three recommendations

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
```text
Loaded songs: 17

Top recommendations:

1. Sunrise City by Neon Echo
   Score: 98.40
   Reasons: mood match (+20.00), genre match (+15.00), energy closeness (+19.60), valence closeness (+14.40), danceability closeness (+9.90), acousticness closeness (+9.70), tempo closeness (+9.80)

2. Rooftop Lights by Indigo Parade
   Score: 81.45
   Reasons: mood match (+20.00), energy closeness (+19.20), valence closeness (+14.85), danceability closeness (+9.80), acousticness closeness (+8.00), tempo closeness (+9.60)

3. Gym Hero by Max Pulse
   Score: 73.95
   Reasons: genre match (+15.00), energy closeness (+17.40), valence closeness (+14.55), danceability closeness (+9.20), acousticness closeness (+9.00), tempo closeness (+8.80)

4. Neon Cathedral by Pulse Divine
   Score: 60.25
   Reasons: energy closeness (+18.20), valence closeness (+14.85), danceability closeness (+8.90), acousticness closeness (+9.10), tempo closeness (+9.20)

5. Concrete Sermon by Kofi Blaze
   Score: 57.15
   Reasons: energy closeness (+18.40), valence closeness (+11.55), danceability closeness (+9.70), acousticness closeness (+10.00), tempo closeness (+7.50)
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



