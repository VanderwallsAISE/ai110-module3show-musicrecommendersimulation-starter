# 🎧 Model Card: VibeRank 1.0

## 1. Model Name

**VibeRank 1.0**

---

## 2. Intended Use

VibeRank 1.0 is a classroom music-recommender simulation. It generates personalized song suggestions by comparing a user's stated preferences with the attributes of each song in the catalog.

The system assumes that the user can describe the kind of music they want through preferences such as genre, mood, energy, tempo, valence, danceability, and acousticness.

This project is intended for learning and experimentation. It is not designed for real users or production use.

---

## 3. How the Model Works

The recommender gives every song a weighted relevance score.

A matching mood adds 20 points, and a matching genre adds 15 points. The system also compares the song's energy, valence, danceability, tempo, and acousticness with the user's target values. Songs whose numerical features are closer to the user's preferences receive more points.

The numerical weights are:

- Energy closeness: up to 20 points
- Valence closeness: up to 15 points
- Danceability closeness: up to 10 points
- Tempo closeness: up to 10 points
- Acousticness closeness: up to 10 points

The highest possible score is 100 points. After every song receives a score, the system sorts the complete catalog from highest score to lowest score and returns the top recommendations.

The system also provides reasons explaining how each song earned its points. I expanded the starter logic by adding more numerical features, a complete 100-point scoring system, multiple test profiles, edge-case testing, and explanations for the recommendations.

---

## 4. Data

The recommender uses a catalog of 17 fictional songs stored in `data/songs.csv`.

Each song includes identification information:

- `id`
- `title`
- `artist`

Each song also includes recommendation features:

- `genre`
- `mood`
- `energy`
- `tempo_bpm`
- `valence`
- `danceability`
- `acousticness`

The original catalog contained 10 songs. I added seven fictional songs to increase the variety of genres and moods.

The dataset is still very small and partially AI-generated. It does not represent the full range of real music, languages, cultures, artists, genres, or listener preferences.

---

## 5. Strengths

The recommender works best when the user's categorical and numerical preferences agree.

The High-Energy Happy Pop profile produced a reasonable result because `Sunrise City` matched both the requested genre and mood and was also close to the numerical targets.

The Chill Lofi profile correctly ranked calm, slow, and highly acoustic songs near the top. The Deep Intense Rock profile also produced an intuitive first result because `Storm Runner` matched the requested genre, mood, energy, and tempo.

Another strength is explainability. The system shows the points contributed by each feature, so a user can understand why a song ranked highly.

---

## 6. Limitations and Bias

The recommender uses a small and partially synthetic catalog of only 17 songs, so the available data strongly influences the results. It uses exact string matching, which treats related genres such as `pop` and `indie pop` as completely different. The system may create a filter bubble because it repeatedly rewards music that resembles the user's existing preferences.

Its feature weights were manually chosen rather than learned from real listener behavior, so different weights could produce significantly different rankings. The system also does not use listening history, skips, likes, lyrics, cultural context, or feedback from real users.

The small catalog creates another imbalance. Genres with only one song have fewer opportunities to appear than genres represented by several songs. The system can also behave strangely when a user's categorical preferences conflict with their numerical targets.

---

## 7. Evaluation

### Profiles Tested

The recommender was tested with four different user profiles:

1. High-Energy Happy Pop
2. Chill Lofi Study Music
3. Deep Intense Rock
4. Conflicting High-Energy Lofi

### High-Energy Happy Pop Results

```text
PROFILE: High-Energy Happy Pop

1. Sunrise City by Neon Echo
   Genre: pop
   Mood: happy
   Score: 98.40
   Reasons: mood match (+20.00), genre match (+15.00), energy closeness (+19.60), valence closeness (+14.40), danceability closeness (+9.90), acousticness closeness (+9.70), tempo closeness (+9.80)

2. Rooftop Lights by Indigo Parade
   Genre: indie pop
   Mood: happy
   Score: 81.45
   Reasons: mood match (+20.00), energy closeness (+19.20), valence closeness (+14.85), danceability closeness (+9.80), acousticness closeness (+8.00), tempo closeness (+9.60)

3. Gym Hero by Max Pulse
   Genre: pop
   Mood: intense
   Score: 73.95
   Reasons: genre match (+15.00), energy closeness (+17.40), valence closeness (+14.55), danceability closeness (+9.20), acousticness closeness (+9.00), tempo closeness (+8.80)

4. Neon Cathedral by Pulse Divine
   Genre: edm
   Mood: euphoric
   Score: 60.25
   Reasons: energy closeness (+18.20), valence closeness (+14.85), danceability closeness (+8.90), acousticness closeness (+9.10), tempo closeness (+9.20)

5. Concrete Sermon by Kofi Blaze
   Genre: hip-hop
   Mood: confident
   Score: 57.15
   Reasons: energy closeness (+18.40), valence closeness (+11.55), danceability closeness (+9.70), acousticness closeness (+10.00), tempo closeness (+7.50)
```

### Chill Lofi Study Music Results

```text
PROFILE: Chill Lofi Study Music

1. Library Rain by Paper Lanterns
   Genre: lofi
   Mood: chill
   Score: 98.05
   Reasons: mood match (+20.00), genre match (+15.00), energy closeness (+20.00), valence closeness (+14.25), danceability closeness (+9.70), acousticness closeness (+9.40), tempo closeness (+9.70)

2. Midnight Coding by LoRoom
   Genre: lofi
   Mood: chill
   Score: 96.55
   Reasons: mood match (+20.00), genre match (+15.00), energy closeness (+18.60), valence closeness (+14.85), danceability closeness (+9.30), acousticness closeness (+9.10), tempo closeness (+9.70)

3. Spacewalk Thoughts by Orbit Bloom
   Genre: ambient
   Mood: chill
   Score: 78.00
   Reasons: mood match (+20.00), energy closeness (+18.60), valence closeness (+13.50), danceability closeness (+8.60), acousticness closeness (+8.80), tempo closeness (+8.50)

4. Focus Flow by LoRoom
   Genre: lofi
   Mood: focused
   Score: 77.20
   Reasons: genre match (+15.00), energy closeness (+19.00), valence closeness (+14.40), danceability closeness (+9.50), acousticness closeness (+9.80), tempo closeness (+9.50)

5. Coffee Shop Stories by Slow Stereo
   Genre: jazz
   Mood: relaxed
   Score: 59.70
   Reasons: energy closeness (+19.60), valence closeness (+12.60), danceability closeness (+9.90), acousticness closeness (+9.10), tempo closeness (+8.50)
```

### Deep Intense Rock Results

```text
PROFILE: Deep Intense Rock

1. Storm Runner by Voltline
   Genre: rock
   Mood: intense
   Score: 98.85
   Reasons: mood match (+20.00), genre match (+15.00), energy closeness (+19.80), valence closeness (+14.55), danceability closeness (+9.90), acousticness closeness (+9.80), tempo closeness (+9.80)

2. Gym Hero by Max Pulse
   Genre: pop
   Mood: intense
   Score: 75.60
   Reasons: mood match (+20.00), energy closeness (+19.80), valence closeness (+10.20), danceability closeness (+7.70), acousticness closeness (+9.70), tempo closeness (+8.20)

3. Iron Verdict by Ashen Crown
   Genre: metal
   Mood: aggressive
   Score: 59.30
   Reasons: energy closeness (+19.20), valence closeness (+12.90), danceability closeness (+8.70), acousticness closeness (+9.50), tempo closeness (+9.00)

4. Night Drive Loop by Neon Echo
   Genre: synthwave
   Mood: moody
   Score: 54.80
   Reasons: energy closeness (+16.60), valence closeness (+14.40), danceability closeness (+9.20), acousticness closeness (+8.60), tempo closeness (+6.00)

5. Neon Cathedral by Pulse Divine
   Genre: edm
   Mood: euphoric
   Score: 54.30
   Reasons: energy closeness (+19.40), valence closeness (+9.90), danceability closeness (+7.40), acousticness closeness (+9.80), tempo closeness (+7.80)
```

### Conflicting High-Energy Lofi Results

```text
PROFILE: Conflicting High-Energy Lofi

1. Midnight Coding by LoRoom
   Genre: lofi
   Mood: chill
   Score: 76.65
   Reasons: mood match (+20.00), genre match (+15.00), energy closeness (+9.40), valence closeness (+12.15), danceability closeness (+7.70), acousticness closeness (+9.60), tempo closeness (+2.80)

2. Library Rain by Paper Lanterns
   Genre: lofi
   Mood: chill
   Score: 74.15
   Reasons: mood match (+20.00), genre match (+15.00), energy closeness (+8.00), valence closeness (+12.75), danceability closeness (+7.30), acousticness closeness (+8.90), tempo closeness (+2.20)

3. Focus Flow by LoRoom
   Genre: lofi
   Mood: focused
   Score: 56.80
   Reasons: genre match (+15.00), energy closeness (+9.00), valence closeness (+12.60), danceability closeness (+7.50), acousticness closeness (+9.70), tempo closeness (+3.00)

4. Gym Hero by Max Pulse
   Genre: pop
   Mood: intense
   Score: 55.20
   Reasons: energy closeness (+19.60), valence closeness (+14.70), danceability closeness (+9.70), acousticness closeness (+3.00), tempo closeness (+8.20)

5. Spacewalk Thoughts by Orbit Bloom
   Genre: ambient
   Mood: chill
   Score: 55.00
   Reasons: mood match (+20.00), energy closeness (+6.60), valence closeness (+13.50), danceability closeness (+5.60), acousticness closeness (+8.30), tempo closeness (+1.00)
```

### Accuracy and Observations

The normal profiles produced results that mostly matched my expectations. `Sunrise City` ranked first for the High-Energy Happy Pop profile because it matched both the requested genre and mood while also being close to every numerical target. `Library Rain` ranked first for the Chill Lofi profile because it matched both categorical preferences and had almost exactly the requested energy level. `Storm Runner` ranked first for the Deep Intense Rock profile because its genre, mood, energy, tempo, and other numerical features closely matched the profile.

One interesting result was that `Gym Hero` appeared near the top of both the Happy Pop and Intense Rock profiles. For the Happy Pop profile, it received genre-match points and scored strongly on energy, valence, danceability, acousticness, and tempo even though its mood did not match. For the Intense Rock profile, it received the mood match and had numerical attributes close to the requested targets even though its genre was pop. This demonstrates that a song can rank highly through its combined weighted score without matching every feature.

### Conflicting Profile Analysis

The Conflicting High-Energy Lofi profile showed how categorical and numerical preferences can disagree. The genre and mood requested calm lofi music, while the energy, tempo, and danceability targets described intense workout music. `Midnight Coding` and `Library Rain` still ranked first because together, the genre and mood matches contributed 35 points. However, their energy and tempo scores were much lower than they were for the normal Chill Lofi profile.

`Gym Hero` appeared fourth because its numerical features matched the high-energy portion of the profile very well, but it received no genre or mood points and had low similarity for acousticness. This result shows that the recommender balances multiple preferences, but it also shows that the categorical weights can strongly influence the ranking even when the numerical preferences conflict.

### Scoring Experiment: Removing Mood

I temporarily removed the 20-point mood-match bonus and ran the same four user profiles again. This allowed me to examine how strongly the mood feature affected the ranking.

For the Happy Pop profile, `Gym Hero` moved from third place to second place because it had strong numerical similarity and did not lose any mood points, while `Rooftop Lights` dropped from second to third after losing its mood bonus.

For the Chill Lofi profile, `Focus Flow` moved from fourth place to second because it matched the lofi genre and was close to the numerical targets without depending on a mood match. `Midnight Coding` dropped from second to third after losing 20 mood points.

For the Deep Intense Rock profile, `Iron Verdict` moved above `Gym Hero` because `Gym Hero` lost its mood-match advantage. For the conflicting lofi profile, `Focus Flow` moved to first place because it kept its genre bonus and had stronger numerical similarity than the other lofi songs after the mood bonus was removed.

The experiment produced more varied recommendations, but some results felt less emotionally accurate because songs could closely match the numerical targets while expressing a different mood. I restored the mood feature because it provides useful emotional context, although its 20-point weight has a noticeable influence on the final rankings.

---

## 8. Future Work

A future version could use a much larger and more representative catalog.

It could recognize partial similarity between related genres such as `pop` and `indie pop` instead of treating them as completely different categories.

It could learn feature weights from real listening behavior such as likes, skips, replays, playlist additions, and listening time instead of relying on manually selected weights.

The system could also include diversity logic so that the top results do not contain too many songs from the same artist or genre.

---

## 9. Personal Reflection

This project helped me understand the general structure of a content-based recommender. I saw how song data and user preferences can be transformed into scores, how those scores can be used to rank songs, and how changing one weight can change the final recommendations. I also learned that a simple rule-based algorithm can produce results that feel personalized even though it is not actually learning from users.

AI tools helped me generate and modify much of the implementation, debug the package imports, and explain parts of the scoring logic. I still had to check the AI's work because it sometimes created inconsistencies. For example, I had to correct `hiphop` to `hip-hop`, ensure that the profile fields matched the scoring function, verify that the weights totaled 100 points, and confirm the results through tests and experiments.

However, I did not enjoy the implementation process very much because I relied heavily on AI and did not feel that I was learning how to write the Python code independently. I learned more about the architecture, evaluation process, feature weights, bias, and documentation than about Python syntax or implementing the system from scratch.

This experience showed me the difference between completing an AI-assisted engineering workflow and independently mastering the code. My next step would be to rebuild a much smaller recommender manually, using only a few songs and features, so I can understand and write each line myself before returning to a larger version.