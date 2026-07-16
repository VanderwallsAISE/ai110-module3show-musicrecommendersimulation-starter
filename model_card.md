# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

## Limitations and Bias

The recommender uses a small and partially synthetic catalog of only 17 songs, so the available data strongly influences the results. It uses exact string matching, which treats related genres such as `pop` and `indie pop` as completely different. The system may create a filter bubble because it repeatedly rewards music that resembles the user's existing preferences. Its feature weights were manually chosen rather than learned from real listener behavior, so different weights could produce significantly different rankings. The system also does not use listening history, skips, likes, lyrics, cultural context, or feedback from real users.

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

Without the mood bonus, songs with similar energy, tempo, valence, danceability, and acousticness became more competitive even when their emotional label did not match the user. [Describe one or two actual ranking changes here.]

The experiment produced more varied recommendations, but some results felt less accurate because songs could closely match the numerical targets while expressing a different mood. I restored the mood feature because it provides useful emotional context, although its 20-point weight has a noticeable influence on the final rankings.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
