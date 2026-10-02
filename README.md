# AFL Pressure Analysis (2026)

Do finals change the game? A data-driven analysis of every 2026 AFL final, testing whether the teams that handle and apply pressure best are the ones that win in September.

Thesis: pressure is the difference between regular season and finals football. The teams that absorb it, apply it, and stay clean under it win premierships. Brisbane proved it, coming back from 10 points down at three-quarter time to win the Grand Final.

## What this project does

Scrapes the full 2026 AFL season (207 home-and-away games + 11 finals) from AFL Tables, extracts quarter-by-quarter scoring data, and runs 8 analyses plus a game-by-game finals breakdown to test whether pressure decides finals.

## The analyses

1. Scoring by quarter (finals vs regular season)
2. Goal accuracy under pressure (does kicking crack in finals?)
3. The decisive quarter (Q1 sets the tone, Q3 separates, Q4 decides the close ones)
4. Lead protection (87% of 3QT leaders hold on in regular season, only 82% in finals)
5. Pressure as a weapon (opponent suppression below season average)
6. Pressure Ratings (custom composite metric ranking every finals team)
7. Favourite vs underdog (55% favourite win rate, 45% upset rate)
8. Grand Final deep dive (Brisbane's Q4 comeback: 34 pts to 17)
9. Game-by-game finals breakdown (every final, every quarter, where pressure decided it)

## Key findings

- Q3 IS the premiership quarter: winners outscored opponents by +9.2 pts in Q3, nearly double any other quarter. But Q4 decides the close ones (both comebacks were Q4, including the Grand Final).
- Q1 sets the tone: 73% of finals winners won the first quarter.
- Lead protection drops from 87% to 82% in finals. Pressure creates comebacks.
- 45% upset rate: pressure is the great equaliser.
- Hawthorn beat Fremantle by 32 points at Perth Stadium. Fremantle scored 40 (season avg 99). Pressure destroyed the minor premier at home.
- Fremantle came back from 21 points down at 3QT against Sydney in the prelim, winning Q4 by 33. Sydney scored 1 point in Q4.
- Brisbane's Grand Final comeback: down 10 at 3QT, won Q4 by 17, won the flag by 7. Fremantle's accuracy collapsed to 29% in Q4 under pressure. Brisbane shot at 56%.
- Brisbane's path: lost to Sydney by 53, then beat Adelaide by 53, beat Hawthorn by 9, beat Fremantle by 7. The premier got better under more pressure.

## The Hawthorn-Fremantle story

The qualifying final at Perth Stadium is the clearest pressure case study in the series. Hawthorn applied relentless pressure from the first bounce. Fremantle were held to 9 points in Q1 (season avg per quarter: ~25). Their accuracy dropped to 33% (season avg: 53%). The minor premier, at home, couldn't get the ball out of their defensive half. Pressure didn't just beat them, it took away everything that made them good.

## Data

AFL Tables (afltables.com): quarter-by-quarter scores for all 218 games (207 H&A + 11 finals), scraped with Python.

## Tech

Python, pandas, requests, regex (HTML scraping)

## Files

- scrape_quarters.py: data pipeline (fetches + parses AFL Tables)
- quarters_2026.csv: 218 games, 31 columns, quarter-by-quarter
- pressure_analysis.py: all 8 aggregate analyses
- finals_breakdown.py: game-by-game finals pressure stories
- pressure_ratings.csv: custom pressure rating for every finals team

Built by Sai Surapaneni
