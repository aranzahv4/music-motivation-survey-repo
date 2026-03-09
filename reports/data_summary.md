# Column names: Questions

## Demographics

**'What is your gender identity? '**: `gender`

'How old are you? ': `age`

'What is/are your ethnicity/ies?': `ethnicity`

'What is/are your nationality/ ies?': `nationality`

'On a scale of 1-5, how introverted are you?\n(1 = introverted, 5 = extroverted)': `introversion_score`,

## Music Preferences

'What is your preferred music genre? (on a daily basis) ': `preferred_genre_daily`

'What is your preferred music genre to listen to at parties? ': `preferred_genre_parties`

'What are your top 5 songs before going out (this can be on your own or with others) (e.g., pregame, getting ready, etc.)? \n\n*Please specify song title and artist(s)!*': `top_5_songs_before_going_out`

'What emotions do you feel when listening to these top 5 songs?': `emotions_top_5_songs`

'Top 5 songs when hosting a party? If you have never hosted a party, please answer what you would put in your playlist!\n\n*Please specify song title and artist(s)!*': `top_5_songs_when_hosting_party`

'When you curate your party music playlist (even hypothetically), what is your intent for the party? For the people?': `party_playlist_intent`

## Party Experiences
Have you ever gone to a party sober? (if yes, explain your experience with it: what you liked what surprised you vs. going to a party not sober, etc.)': `party_experience_sober`

'On a scale of 1-5, how likely are you to pregame before a party/gathering?\n(1 = very unlikely, 5 = very likely)': 'pregame_likelihood_score'

'How many times have you gone to a gathering in the last 2 months?': `times_in_last_2_months`

'On a scale of 1-5, how likely are you to come up to a stranger at a party sober? \n(1 = very unlikely, 5 = very likely)': `likelihood_approach_stranger_score`

'On a scale of 1-5, how likely are you to sing along to a song at a party sober?\n(1 = very unlikely, 5 = very likely)': `likelihood_sing_along_score`

"On a scale of 1-5, how likely are you are you to start a conversation with someone you don't know at a party with NO music sober?\n(1 = very unlikely, 5 = very likely)": `likelihood_conversation_no_music_score`

"On a scale of 1-5, how likely are you to start a conversation with someone you don't know at a house party with LOUD music sober?": `likelihood_conversation_loud_music_score`

'Why do you go to parties?': `reason_for_going_to_parties`

'What do you like about the parties you have gone to so far? (music, environment, loudness, etc. ) ': `party_likes`

"What don't you like about parties? (music, environment, loudness, etc. ) ": `parties_dislikes`

## Interview Participation
'Are you willing to participate in a short (anonymous) interview about your party experiences? (If yes, input your email)': `interview_participation_email`

# Survey Analysis-Ready Data:

## Column Reference

### Demographics

| Column | Type | Description |
|--------|------|-------------|
| `participant_id` | int | Unique ID assigned to each respondent (1–40) |
| `Timestamp` | datetime | Date and time the survey was submitted |
| `gender` | str (categorical) | Standardized gender identity: `woman` (32), `man` (6), `non-binary` (1), `other/unclear` (1) |
| `age` | int | Respondent age. Range: 19–25, mean: 20.4, most respondents are 19 (n=13) or 20 (n=12) |
| `race_ethnicity` | str (categorical) | Derived grouping column: `asian` (20), `latine/hispanic` (16), `multiracial` (3), `other/unknown` (1) |
| `ethnicity` | str | Cleaned raw ethnicity response (lowercase, duplicates standardized) |
| `nationality` | str | Cleaned raw nationality response (lowercase, duplicates standardized) |
| `introversion_score` | int (1–5) | Self-reported introversion/extroversion. 1 = most introverted, 5 = most extroverted. Most respondents scored 3 (n=23); no one scored 1 |

---

### Music Preferences

| Column | Type | Description |
|--------|------|-------------|
| `preferred_genre_daily` | str | Raw multi-select response for daily music genre(s) |
| `preferred_genre_parties` | str | Raw multi-select response for party music genre(s) |
| `genre_daily_*` | int (0/1) | Binary indicator columns for each daily genre. 10 genres total: `hip_hop_and_randb` (31), `pop` (32), `electronic` (14), `metal_rock` (11), `jazz_classical` (9), `indie` (6), `country_folk` (2), `kpop` (2), `latin_reggaeton` (2), `other` (1) |
| `genre_party_*` | int (0/1) | Binary indicator columns for each party genre. 9 genres total: `pop` (35), `hip_hop_and_randb` (27), `electronic` (19), `jazz_classical` (4), `metal_rock` (4), `latin_reggaeton` (2), `country_folk` (1), `indie` (1), `kpop` (1) |
| `top_5_songs_before_going_out` | str (open-ended) | Up to 5 songs + artists the respondent listens to before going out |
| `emotions_top_5_songs` | str (open-ended) | Emotions felt when listening to their top 5 pregame songs |
| `top_5_songs_when_hosting_party` | str (open-ended) | Songs the respondent would play when hosting; 1 missing value (participant 15) |
| `party_playlist_intent` | str (open-ended) | What the respondent tries to achieve when curating a party playlist |

---

### Party Experiences

| Column | Type | Description |
|--------|------|-------------|
| `pregame_likelihood_score` | int (1–5) | Likelihood of pregaming before a party. Mean: 3.15 — fairly split, slight lean toward likely |
| `times_in_last_2_months` | int | Number of gatherings attended in the last 2 months. Range: 0–10, mean: 2.7; 9 respondents attended 0 gatherings |
| `likelihood_approach_stranger_score` | int (1–5) | Likelihood of approaching a stranger at a party sober. Mean: 2.62 — tends toward unlikely |
| `likelihood_sing_along_score` | int (1–5) | Likelihood of singing along to a song at a party sober. Mean: 3.92 — tends toward likely, highest of all social behavior scores |
| `likelihood_conversation_no_music_score` | int (1–5) | Likelihood of starting a conversation with a stranger at a party with NO music, sober. Mean: 2.25 — the lowest social behavior score |
| `likelihood_conversation_loud_music_score` | int (1–5) | Likelihood of starting a conversation with a stranger at a party with LOUD music, sober. Mean: 2.95 — slightly higher than the no music condition |
| `reason_for_going_to_parties` | str (open-ended) | Why the respondent goes to parties |
| `party_likes` | str (open-ended) | What the respondent likes about parties |
| `parties_dislikes` | str (open-ended) | What the respondent dislikes about parties |
| `party_experience_sober` | str (open-ended) | Description of sober party experience; 4 missing values (question was optional) |

---

### Interview Participation

| Column | Type | Description |
|--------|------|-------------|
| `interview_participation_email` | str | Email if willing to be interviewed; 7 missing values (question was optional) |