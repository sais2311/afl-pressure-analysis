# AFL Pressure Analysis (2026)

Do finals change the game? A data-driven analysis of every 2026 AFL final, testing whether the teams that handle and apply pressure best are the ones that win in September.

**Thesis:** pressure is the difference between regular season and finals football. The teams that absorb it, apply it, and stay clean under it win premierships. Brisbane proved it, coming back from 10 points down at three quarter time to win the Grand Final.

## What this project does

Scrapes the full 2026 AFL season (207 home-and-away games + 11 finals) from AFL Tables, extracts quarter-by-quarter scoring data, and runs 8 analyses plus a game-by-game finals breakdown to test whether pressure decides finals.

## The analyses

1. Scoring by quarter (finals vs regular season)
2. Goal accuracy under pressure
3. The decisive quarter
4. Lead protection
5. Pressure as a weapon (opponent suppression)
6. Pressure Ratings (custom composite metric)
7. Favourite vs underdog
8. Grand Final deep dive
9. Game-by-game finals breakdown

---

## Detailed findings

### 1. Scoring by quarter: finals vs regular season

Regular season averages per team per quarter:
- Q1: 22.7 | Q2: 21.4 | Q3: 22.3 | Q4: 22.1 | Total: 88.5

Finals averages per team per quarter:
- Q1: 23.5 | Q2: 20.0 | Q3: 23.0 | Q4: 25.0 | Total: 91.5

The standout: Q4 scoring jumps +2.9 points per team in finals compared to regular season. The last quarter gets bigger, not smaller. Teams do not shut up shop in September, they go harder. Q2 actually drops by 1.4 points as teams tighten up after the opening burst and reassess at halftime. Overall scoring is slightly higher in finals (91.5 vs 88.5), which challenges the common belief that finals are low scoring grinds.

### 2. Goal accuracy under pressure

Pressure does not make both teams inaccurate. It makes the team absorbing pressure inaccurate. The team applying pressure stays clean. That asymmetry is the whole story.

Key examples from the 2026 finals:
- Hawthorn vs Fremantle (QF): Hawthorn 45% accuracy vs Fremantle 33%. Fremantle were getting the ball inside 50 but could not convert. Every shot was under duress, every kick was rushed.
- Grand Final: Brisbane 54% vs Fremantle 41%. In Q4 specifically, Brisbane shot at 56% while Fremantle collapsed to 29%.
- Sydney vs Fremantle (PF): Sydney's Q4 accuracy was 0%. Zero goals from one shot in the entire last quarter. Pressure cracked their kicking completely.
- Melbourne vs Carlton (WF): Melbourne shot at 35% for the game. 0 goals in Q4. Pressure took away a team that averaged 100 points per game.
- Adelaide vs Bulldogs (EF): Adelaide 70% accuracy vs Bulldogs 39%. The clearest accuracy gap of any final.

### 3. The decisive quarter

Times the eventual winner won each quarter across all 11 finals:
- Q1: 8 out of 11 (73%)
- Q2: 6 out of 11 (55%)
- Q3: 7 out of 11 (64%)
- Q4: 6 out of 11 (55%)

Average margin the winner had in each quarter:
- Q1: +5.1 pts
- Q2: +4.1 pts
- Q3: +9.2 pts (nearly double any other quarter)
- Q4: +5.0 pts

The real story is layered, not one dimensional.

**Q1 sets the tone.** 73% of finals winners won the first quarter. Fast starts matter more in September than at any other time of year. Coming out slow against a team that is prepared to apply pressure from the first bounce is a recipe for falling behind early and chasing the game under increasing pressure. Hawthorn proved this against Fremantle (28 to 9 in Q1), Sydney proved it against Brisbane (42 to 16 in Q1), and Brisbane proved it against Adelaide (42 to 15 in Q1).

**Q3 separates.** Winners outscored opponents by 9.2 points on average in Q3. This is where the better team puts the game away. The old footy saying about Q3 being the premiership quarter is backed by the data. Geelong's Q3 against Carlton (+26), Brisbane's Q3 against Hawthorn in the prelim (+34), and Adelaide's Q3 against the Bulldogs (+13) are the clearest examples.

**Q4 decides the close ones.** Both comebacks in the 2026 finals happened in Q4. When the game is still alive at three quarter time, the final quarter is where pressure breaks the loser. Fremantle came back from 21 down against Sydney by winning Q4 by 33. Brisbane came back from 10 down against Fremantle by winning Q4 by 17.

### 4. Lead protection under pressure

Regular season: 87.3% of teams leading at three quarter time held on to win.

Finals: 81.8% of teams leading at three quarter time held on (9 out of 11).

That 5% drop meant two comeback wins in the 2026 finals, including the Grand Final. In the regular season that same percentage difference is the gap between roughly 10 comebacks across a full season and 20. Finals pressure makes leads more fragile. The crowd, the stakes, the fatigue. A 10 point lead at three quarter time in Round 8 is safe. In a Grand Final it is not.

The two comebacks:
- Preliminary Final: Fremantle trailed Sydney by 21 at 3QT. Sydney scored 1 point in Q4 (0 goals 1 behind, 0% accuracy). Fremantle won Q4 by 33 and won by 12.
- Grand Final: Brisbane trailed Fremantle by 10 at 3QT. Brisbane scored 34 in Q4 (5.4), Fremantle managed 17 (2.5, 29% accuracy). Brisbane won by 7.

### 5. Pressure as a weapon: opponent suppression

How much did finals teams hold their opponents below their season average? This is the clearest measure of pressure as an active weapon, not just a byproduct of good defence.

Biggest suppressions in the 2026 finals:
- Hawthorn held Fremantle to 40 pts (season avg 99). A 59 point suppression. The single biggest suppression of any team in the finals.
- Carlton held Melbourne to 55 pts (season avg 100). A 45 point suppression. Melbourne managed zero goals in Q4.
- Fremantle held Sydney to 71 pts in the prelim (season avg 111). A 40 point suppression. Sydney scored 1 point in Q4.
- Sydney held Brisbane to 88 pts in the QF (season avg 109). A 21 point suppression.
- Adelaide held the Bulldogs to 68 pts (season avg 83). A 15 point suppression.
- Geelong held Carlton to 74 pts (season avg 87). A 13 point suppression.

The teams that won finals did not just outscore their opponents. They took away what made their opponents good. They forced them below their average, cracked their accuracy, and disrupted their game plan. Fremantle's 59 point drop from their season average is the most extreme example. Pressure did not just beat them. It made them unrecognisable.

### 6. Pressure Ratings: a custom composite metric

A composite metric ranking every finals team on how well they handled and applied pressure. Four components, equally weighted:

- Q4 margin in finals (positive means outscored opponents in the clutch)
- Overall finals margin
- Opponent suppression (how much they held opponents below season average)
- Accuracy hold (whether their accuracy held up in finals vs regular season)

Rankings:
1. Hawthorn: 87.8 (dominated Q4s, suppressed opponents the most, accuracy held up)
2. Brisbane Lions: 50.5 (Grand Final Q4 comeback was the standout moment)
3. Other finals teams fill the middle range
4. Melbourne: near the bottom (suppressed badly, 0 goals in Q4 vs Carlton)

Hawthorn topped the rating despite not winning the premiership. They were the best pressure team across the finals as a whole. They suppressed Fremantle by 59 points and maintained their accuracy under pressure. They only lost because Brisbane produced the best single quarter of the entire finals in the prelim Q3 (44 points to 10, a 34 point swing).

Brisbane rated lower overall because they got demolished by Sydney in the qualifying final (lost by 53). But their Grand Final Q4 is the single best pressure quarter of the finals: down 10, won by 17. The metric rewards consistency. Hawthorn were consistently elite. Brisbane had the highest peak but also the lowest valley.

### 7. Favourite vs underdog in finals

Using season average margin to determine the favourite for each final:

- Wildcard Final 1: Bulldogs beat Collingwood. UPSET.
- Wildcard Final 2: Carlton beat Melbourne. UPSET.
- Qualifying Final 1: Hawthorn beat Fremantle at Perth Stadium. UPSET.
- Qualifying Final 2: Sydney beat Brisbane. Favourite won.
- Elimination Final 1: Geelong beat Carlton. Favourite won.
- Elimination Final 2: Adelaide beat Bulldogs. Favourite won.
- Semi Final 1: Fremantle beat Geelong. UPSET.
- Semi Final 2: Brisbane beat Adelaide. Favourite won.
- Preliminary Final 1: Fremantle beat Sydney. UPSET.
- Preliminary Final 2: Brisbane beat Hawthorn. Favourite won.
- Grand Final: Brisbane beat Fremantle. Favourite won.

Result: favourites won 6 out of 11 (55%). Upsets: 5 out of 11 (45%).

Nearly half the finals were upsets. The better team based on season form lost almost as often as they won. The early rounds had the most upsets (3 of the first 4 finals were upsets). By the time you reach the prelims and Grand Final, the cream rises, but the path there is chaotic. Pressure is the equaliser. An underdog that applies more pressure than the favourite expected can win any single final.

### 8. Grand Final deep dive: Brisbane Lions 96 def. Fremantle 89

Quarter by quarter:
| Quarter | Fremantle | Brisbane | Margin |
|---------|-----------|----------|--------|
| Q1 | 22 | 23 | -1 |
| Q2 | 21 | 20 | +1 |
| Q3 | 29 | 19 | +10 |
| Q4 | 17 | 34 | -17 |
| Total | 89 | 96 | -7 |

Running margin: Brisbane by 1 at Q1, level at halftime, Fremantle by 10 at 3QT, Brisbane by 7 at the final siren.

Accuracy: Fremantle 12.17 (41.4%). Brisbane 14.12 (53.8%). In Q4: Fremantle 2.5 (28.6%). Brisbane 5.4 (55.6%).

Fremantle led by 10 at three quarter time. They had won Q3. They looked like premiers. Then Brisbane applied the most sustained pressure of the entire finals series. 5 goals 4 in Q4. Fremantle managed 2 goals 5. Fremantle had shots but they could not convert. Their Q4 accuracy dropped to 29%. Every kick was rushed. Every decision was a split second too slow. Brisbane were calmer, cleaner, more precise under the exact same pressure on the exact same stage.

Brisbane's path through the finals tells its own pressure story. They lost to Sydney by 53 points in the qualifying final. Most teams would be done after that. Instead they beat Adelaide by 53, beat Hawthorn by 9 in one of the best games of the year, then came back from 10 down to beat Fremantle in the Grand Final. They got better as the pressure got bigger. The team that nearly got knocked out in week one won the flag.

Brisbane's third straight premiership. The first club to do it since Brisbane themselves in 2001, 2002, 2003.

---

## Game-by-game finals highlights

**Wildcard Final 1: Western Bulldogs 96 def. Collingwood 93 (MCG)**
3 point thriller. Bulldogs led by 12 at 3QT. Collingwood stormed home with 37 in Q4 (6.1 at 85.7% accuracy) but fell 3 short. Upset. Decisive quarter: Q2 (Bulldogs won it by 9).

**Wildcard Final 2: Carlton 74 def. Melbourne 55 (MCG)**
Melbourne scored 27 in Q1 then 3 in Q4. Zero goals in the last quarter. Carlton came from 18 down to win by 19. Melbourne suppressed 45 below their season average (100 to 55). Upset. Away win.

**Qualifying Final 1: Hawthorn 72 def. Fremantle 40 (Perth Stadium)**
The pressure masterclass. Fremantle scored 9 in Q1 and 1 in Q2. Season average 99, held to 40. Accuracy 33%. The minor premier at home, completely dismantled. Upset. Away win. The clearest case study of pressure destroying a team's game plan.

**Qualifying Final 2: Sydney 141 def. Brisbane Lions 88 (SCG)**
Sydney's demolition. 42 in Q1. Led by 26 at quarter time and never looked back. Brisbane suppressed 21 below their average. Brisbane's worst performance and it nearly ended their season.

**Elimination Final 1: Geelong 107 def. Carlton 74 (MCG)**
Carlton led by 16 at quarter time. Then Geelong's Q3 happened: 39 to 13, a 26 point quarter. The premiership quarter in action. Decisive quarter: Q3.

**Elimination Final 2: Adelaide 90 def. Western Bulldogs 68 (Adelaide Oval)**
Adelaide's accuracy was the story: 70% compared to the Bulldogs' 39%. Pressure cracked the Bulldogs' kicking. Decisive quarter: Q3. Home advantage.

**Semi Final 1: Fremantle 120 def. Geelong 106 (Perth Stadium)**
Fremantle bounced back from the Hawthorn disaster. 38 in Q1 set the tone. Upset. Home advantage.

**Semi Final 2: Brisbane Lions 144 def. Adelaide 91 (Gabba)**
Brisbane's statement game. 42 in Q1, 144 total. Above their season average by 35 points. Home advantage.

**Preliminary Final 1: Fremantle 83 def. Sydney 71 (SCG)**
THE COMEBACK. Sydney led by 21 at 3QT. They scored 1 point in Q4. 0 goals 1 behind. 0% accuracy. Fremantle won Q4 by 33. Sydney suppressed 40 below their season average. Upset. Away win. The most dramatic quarter of the finals until the Grand Final.

**Preliminary Final 2: Brisbane Lions 131 def. Hawthorn 122 (MCG)**
One of the best games of the year. Hawthorn led by 14 at halftime. Brisbane's Q3 explosion: 44 to 10, a 34 point swing. The biggest single quarter margin of the entire finals. Hawthorn fought back with 45 in Q4 but Brisbane held on by 9. Away win.

**Grand Final: Brisbane Lions 96 def. Fremantle 89 (MCG)**
See the deep dive above. Down 10 at 3QT. Won Q4 by 17. Accuracy collapsed for Fremantle (29% in Q4). Brisbane's 3-peat.

---

## The verdict

Finals change the game. The data proves it across every measure.

Leads are less safe. Upsets happen nearly half the time. Accuracy collapses for teams under pressure while the team applying pressure stays clean. Q3 separates the contenders. Q4 decides the close ones. Fast starts matter more than at any other time of year.

The teams that win premierships are not always the most talented. They are the ones that handle pressure best when it matters most. They absorb it, stay clean under it, and apply it back harder.

Brisbane proved it in the Grand Final. Down 10 at three quarter time. Won Q4 by 17. Won the flag by 7. Their accuracy held while Fremantle's collapsed. Their composure held while Fremantle's cracked.

That is what pressure does. That is how finals are won.

---

## Data source

AFL Tables (afltables.com): quarter-by-quarter scores for all 218 games (207 H&A + 11 finals), scraped with Python.

## Tech

Python, pandas, requests, regex (HTML scraping)

## Files

- `scrape_quarters.py` — data pipeline (fetches and parses AFL Tables)
- `quarters_2026.csv` — 218 games, 31 columns, quarter-by-quarter
- `pressure_analysis.py` — all 8 aggregate analyses
- `finals_breakdown.py` — game-by-game finals pressure stories
- `pressure_ratings.csv` — custom pressure rating for every finals team

---

*Built by Sai Surapaneni*
