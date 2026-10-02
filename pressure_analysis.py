import pandas as pd
import numpy as np

df = pd.read_csv("quarters_2026.csv")
ha = df[df["game_type"] == "H&A"].copy()
finals = df[df["game_type"] != "H&A"].copy()

# Build team-game rows (each game seen from both sides)
def team_rows(data):
    home = data[["round","game_type","home_team","away_team","venue",
                 "h_q1","h_q2","h_q3","h_q4","a_q1","a_q2","a_q3","a_q4",
                 "h_total","a_total",
                 "h_goals_q1","h_goals_q2","h_goals_q3","h_goals_q4",
                 "a_goals_q1","a_goals_q2","a_goals_q3","a_goals_q4",
                 "h_behinds_q1","h_behinds_q2","h_behinds_q3","h_behinds_q4",
                 "a_behinds_q1","a_behinds_q2","a_behinds_q3","a_behinds_q4"]].copy()
    home.columns = ["round","game_type","team","opponent","venue",
                    "q1","q2","q3","q4","opp_q1","opp_q2","opp_q3","opp_q4",
                    "total","opp_total",
                    "goals_q1","goals_q2","goals_q3","goals_q4",
                    "opp_goals_q1","opp_goals_q2","opp_goals_q3","opp_goals_q4",
                    "behinds_q1","behinds_q2","behinds_q3","behinds_q4",
                    "opp_behinds_q1","opp_behinds_q2","opp_behinds_q3","opp_behinds_q4"]
    
    away = data[["round","game_type","away_team","home_team","venue",
                 "a_q1","a_q2","a_q3","a_q4","h_q1","h_q2","h_q3","h_q4",
                 "a_total","h_total",
                 "a_goals_q1","a_goals_q2","a_goals_q3","a_goals_q4",
                 "h_goals_q1","h_goals_q2","h_goals_q3","h_goals_q4",
                 "a_behinds_q1","a_behinds_q2","a_behinds_q3","a_behinds_q4",
                 "h_behinds_q1","h_behinds_q2","h_behinds_q3","h_behinds_q4"]].copy()
    away.columns = home.columns
    
    return pd.concat([home, away], ignore_index=True)

all_rows = team_rows(df)
ha_rows = team_rows(ha)
finals_rows = team_rows(finals)

print("=" * 70)
print("2026 AFL PRESSURE ANALYSIS")
print("Do finals change the game?")
print("=" * 70)

# ============================================================
# 1. SCORING BY QUARTER: finals vs regular season
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 1: Scoring by Quarter (Finals vs Regular Season)")
print("=" * 70)

for label, rows in [("Regular Season", ha_rows), ("Finals", finals_rows)]:
    q1 = rows["q1"].mean()
    q2 = rows["q2"].mean()
    q3 = rows["q3"].mean()
    q4 = rows["q4"].mean()
    total = rows["total"].mean()
    print(f"\n{label} (avg points per quarter per team):")
    print(f"  Q1: {q1:.1f}  Q2: {q2:.1f}  Q3: {q3:.1f}  Q4: {q4:.1f}  Total: {total:.1f}")

print("\nDrop-off (finals minus regular season):")
for q in ["q1","q2","q3","q4"]:
    diff = finals_rows[q].mean() - ha_rows[q].mean()
    print(f"  {q.upper()}: {diff:+.1f}")

# ============================================================
# 2. GOAL ACCURACY BY QUARTER (pressure proxy)
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 2: Goal Accuracy by Quarter (Pressure Proxy)")
print("=" * 70)
print("Accuracy = goals / (goals + behinds) ... does kicking crack under pressure?")

for label, rows in [("Regular Season", ha_rows), ("Finals", finals_rows)]:
    print(f"\n{label}:")
    for i in range(1, 5):
        g = rows[f"goals_q{i}"].sum()
        b = rows[f"behinds_q{i}"].sum()
        shots = g + b
        acc = g / shots * 100 if shots > 0 else 0
        print(f"  Q{i}: {acc:.1f}% ({g} goals from {shots} shots)")

# ============================================================
# 3. THE DECISIVE QUARTER
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 3: The Decisive Quarter")
print("=" * 70)
print("Which quarter did the winning team outscore most in finals?")

for label, data in [("Finals", finals), ("Regular Season", ha)]:
    q_wins = {1: 0, 2: 0, 3: 0, 4: 0}
    for _, g in data.iterrows():
        winner_is_home = g["h_total"] > g["a_total"]
        for q in range(1, 5):
            hq = g[f"h_q{q}"]
            aq = g[f"a_q{q}"]
            if winner_is_home and hq > aq:
                q_wins[q] += 1
            elif not winner_is_home and aq > hq:
                q_wins[q] += 1
    total_decided = sum(q_wins.values())
    print(f"\n{label}: Quarter won by the eventual winner:")
    for q in range(1, 5):
        pct = q_wins[q] / max(total_decided, 1) * 100
        print(f"  Q{q}: {q_wins[q]} times ({pct:.1f}%)")

# ============================================================
# 4. LEAD PROTECTION / COMEBACK (CORE)
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 4: Lead Protection Under Pressure (Core)")
print("=" * 70)
print("How often does the team leading at 3/4 time win?")

for label, data in [("Regular Season", ha), ("Finals", finals)]:
    leading_3qt = 0
    held_on = 0
    comeback = 0
    drawn_3qt = 0
    for _, g in data.iterrows():
        h_3qt = g["h_q1"] + g["h_q2"] + g["h_q3"]
        a_3qt = g["a_q1"] + g["a_q2"] + g["a_q3"]
        if h_3qt == a_3qt:
            drawn_3qt += 1
            continue
        leading_3qt += 1
        leader_is_home = h_3qt > a_3qt
        winner_is_home = g["h_total"] > g["a_total"]
        if leader_is_home == winner_is_home:
            held_on += 1
        else:
            comeback += 1
    pct = held_on / max(leading_3qt, 1) * 100
    print(f"\n{label}:")
    print(f"  Games with a leader at 3QT: {leading_3qt}")
    print(f"  Leader held on: {held_on} ({pct:.1f}%)")
    print(f"  Comeback wins: {comeback}")
    print(f"  Level at 3QT: {drawn_3qt}")

# The Grand Final: Brisbane came back
print("\nGrand Final spotlight:")
gf = finals[finals["game_type"] == "Grand Final"].iloc[0]
h3 = gf["h_q1"] + gf["h_q2"] + gf["h_q3"]
a3 = gf["a_q1"] + gf["a_q2"] + gf["a_q3"]
print(f"  3QT: {gf['home_team']} {h3} vs {gf['away_team']} {a3}")
print(f"  Final: {gf['home_team']} {gf['h_total']} vs {gf['away_team']} {gf['a_total']}")
leader = gf["home_team"] if h3 > a3 else gf["away_team"]
winner = gf["home_team"] if gf["h_total"] > gf["a_total"] else gf["away_team"]
if leader != winner:
    print(f"  COMEBACK: {winner} trailed by {abs(h3-a3)} at 3QT and won by {abs(gf['h_total']-gf['a_total'])}")
else:
    print(f"  {winner} led at 3QT and held on")

# ============================================================
# 5. FORCING OPPONENTS BELOW AVERAGE (Pressure as a weapon)
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 5: Pressure as a Weapon (Opponent Suppression)")
print("=" * 70)
print("How much did finals teams suppress their opponents below season average?")

# Get each team's regular season average
season_avg = ha_rows.groupby("team")["total"].mean()

# For each finals game, compare opponent's score to their season average
finals_suppress = []
for _, g in finals.iterrows():
    # Home team suppressing away team
    away_avg = season_avg.get(g["away_team"], 0)
    suppress_away = away_avg - g["a_total"]
    finals_suppress.append({"team": g["home_team"], "opponent": g["away_team"],
                           "opp_season_avg": round(away_avg,1), "opp_finals_score": g["a_total"],
                           "suppression": round(suppress_away,1), "game_type": g["game_type"]})
    # Away team suppressing home team
    home_avg = season_avg.get(g["home_team"], 0)
    suppress_home = home_avg - g["h_total"]
    finals_suppress.append({"team": g["away_team"], "opponent": g["home_team"],
                           "opp_season_avg": round(home_avg,1), "opp_finals_score": g["h_total"],
                           "suppression": round(suppress_home,1), "game_type": g["game_type"]})

sup_df = pd.DataFrame(finals_suppress)
team_suppress = sup_df.groupby("team")["suppression"].mean().sort_values(ascending=False)
print("\nAvg opponent suppression in finals (positive = held opponent below their average):")
for team, val in team_suppress.items():
    print(f"  {team:24s} {val:+.1f} pts")

# ============================================================
# 6. PRESSURE RATINGS (your own composite metric)
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 6: Pressure Ratings (Composite Metric)")
print("=" * 70)
print("Rating = weighted blend of: Q4 scoring margin, lead protection,")
print("         opponent suppression, and accuracy hold in finals.")

# Get finals team data
finals_teams = set(finals_rows["team"].unique())

pressure_ratings = []
for team in sorted(finals_teams):
    t_finals = finals_rows[finals_rows["team"] == team]
    t_season = ha_rows[ha_rows["team"] == team]
    
    if len(t_finals) == 0:
        continue
    
    # Component 1: Q4 margin in finals (positive = outscored in the clutch)
    q4_margin = (t_finals["q4"] - t_finals["opp_q4"]).mean()
    
    # Component 2: Overall finals margin
    finals_margin = (t_finals["total"] - t_finals["opp_total"]).mean()
    
    # Component 3: Opponent suppression (how much below avg they held opponents)
    team_sup = sup_df[sup_df["team"] == team]["suppression"].mean()
    
    # Component 4: Accuracy hold (finals accuracy minus season accuracy)
    season_goals = t_season[["goals_q1","goals_q2","goals_q3","goals_q4"]].sum().sum()
    season_behinds = t_season[["behinds_q1","behinds_q2","behinds_q3","behinds_q4"]].sum().sum()
    season_acc = season_goals / max(season_goals + season_behinds, 1)
    
    finals_goals = t_finals[["goals_q1","goals_q2","goals_q3","goals_q4"]].sum().sum()
    finals_behinds = t_finals[["behinds_q1","behinds_q2","behinds_q3","behinds_q4"]].sum().sum()
    finals_acc = finals_goals / max(finals_goals + finals_behinds, 1)
    
    acc_hold = (finals_acc - season_acc) * 100  # percentage point change
    
    # Composite: equal weight, standardised later
    pressure_ratings.append({
        "team": team,
        "finals_games": len(t_finals),
        "q4_margin": round(q4_margin, 1),
        "finals_margin": round(finals_margin, 1),
        "opp_suppression": round(team_sup, 1),
        "accuracy_hold": round(acc_hold, 1),
    })

pr_df = pd.DataFrame(pressure_ratings)

# Composite score (simple: normalise each component 0-100, average)
for col in ["q4_margin", "finals_margin", "opp_suppression", "accuracy_hold"]:
    mn, mx = pr_df[col].min(), pr_df[col].max()
    rng = mx - mn if mx != mn else 1
    pr_df[col + "_norm"] = (pr_df[col] - mn) / rng * 100

pr_df["pressure_rating"] = pr_df[["q4_margin_norm", "finals_margin_norm",
                                   "opp_suppression_norm", "accuracy_hold_norm"]].mean(axis=1)
pr_df = pr_df.sort_values("pressure_rating", ascending=False)

print("\nPressure Ratings (finals teams only):")
print(f"{'Team':24s} {'Games':>5s} {'Q4 Marg':>8s} {'Fin Marg':>9s} {'Suppress':>9s} {'Acc Hold':>9s} {'RATING':>8s}")
print("-" * 75)
for _, r in pr_df.iterrows():
    print(f"{r['team']:24s} {r['finals_games']:5.0f} {r['q4_margin']:+8.1f} {r['finals_margin']:+9.1f} "
          f"{r['opp_suppression']:+9.1f} {r['accuracy_hold']:+9.1f} {r['pressure_rating']:8.1f}")

# ============================================================
# 7. FAVOURITE vs UNDERDOG
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 7: Favourite vs Underdog in Finals")
print("=" * 70)
print("Did the higher-ranked team (by season avg margin) win?")

season_margin = ha_rows.groupby("team").apply(lambda x: (x["total"] - x["opp_total"]).mean())

fav_wins = 0
upsets = 0
for _, g in finals.iterrows():
    h_rating = season_margin.get(g["home_team"], 0)
    a_rating = season_margin.get(g["away_team"], 0)
    fav_is_home = h_rating >= a_rating
    winner_is_home = g["h_total"] > g["a_total"]
    
    fav = g["home_team"] if fav_is_home else g["away_team"]
    dog = g["away_team"] if fav_is_home else g["home_team"]
    fav_won = (fav_is_home == winner_is_home)
    
    result = "FAV" if fav_won else "UPSET"
    winner = g["home_team"] if winner_is_home else g["away_team"]
    margin = abs(g["h_total"] - g["a_total"])
    
    if g["h_total"] == g["a_total"]:
        result = "DRAW"
    elif fav_won:
        fav_wins += 1
    else:
        upsets += 1
    
    print(f"  {g['game_type']:22s} {fav:20s} vs {dog:20s} -> {result} ({winner} by {margin})")

total_decided = fav_wins + upsets
print(f"\nFavourite won: {fav_wins}/{total_decided} ({fav_wins/max(total_decided,1)*100:.0f}%)")
print(f"Upsets: {upsets}/{total_decided} ({upsets/max(total_decided,1)*100:.0f}%)")

# ============================================================
# 8. GRAND FINAL DEEP DIVE
# ============================================================
print("\n" + "=" * 70)
print("ANALYSIS 8: Grand Final Deep Dive")
print("=" * 70)

gf = finals[finals["game_type"] == "Grand Final"].iloc[0]
print(f"\n{gf['home_team']} vs {gf['away_team']}")
print(f"\nQuarter-by-quarter:")
print(f"{'':12s} {'Q1':>8s} {'Q2':>8s} {'Q3':>8s} {'Q4':>8s} {'Total':>8s}")
print(f"{gf['home_team']:12s} {gf['h_q1']:8d} {gf['h_q2']:8d} {gf['h_q3']:8d} {gf['h_q4']:8d} {gf['h_total']:8d}")
print(f"{gf['away_team']:12s} {gf['a_q1']:8d} {gf['a_q2']:8d} {gf['a_q3']:8d} {gf['a_q4']:8d} {gf['a_total']:8d}")

# Running margin
print(f"\nRunning margin (positive = {gf['home_team']} leads):")
cum_h, cum_a = 0, 0
for q in range(1, 5):
    cum_h += gf[f"h_q{q}"]
    cum_a += gf[f"a_q{q}"]
    margin = cum_h - cum_a
    leader = gf["home_team"] if margin > 0 else gf["away_team"]
    print(f"  End Q{q}: {leader} by {abs(margin)} pts ({cum_h} - {cum_a})")

# Accuracy comparison
print(f"\nGoal accuracy:")
for side, prefix in [(gf["home_team"], "h"), (gf["away_team"], "a")]:
    total_goals = sum(gf[f"{prefix}_goals_q{q}"] for q in range(1,5))
    total_behinds = sum(gf[f"{prefix}_behinds_q{q}"] for q in range(1,5))
    shots = total_goals + total_behinds
    acc = total_goals / max(shots, 1) * 100
    print(f"  {side}: {total_goals}.{total_behinds} ({acc:.1f}% accuracy)")

# Q4 spotlight
print(f"\nQ4 (the pressure quarter):")
print(f"  {gf['home_team']}: {gf['h_goals_q4']}.{gf['h_behinds_q4']} = {gf['h_q4']} pts")
print(f"  {gf['away_team']}: {gf['a_goals_q4']}.{gf['a_behinds_q4']} = {gf['a_q4']} pts")
q4_winner = gf["home_team"] if gf["h_q4"] > gf["a_q4"] else gf["away_team"]
print(f"  {q4_winner} won Q4 by {abs(gf['h_q4'] - gf['a_q4'])} pts")

# Brisbane's season avg vs GF
bris_season = ha_rows[ha_rows["team"] == "Brisbane Lions"]["total"].mean()
bris_gf = gf["a_total"]  # Brisbane was away
print(f"\nBrisbane Lions season avg: {bris_season:.1f}, GF score: {bris_gf}")
print(f"  {'Above' if bris_gf > bris_season else 'Below'} season average by {abs(bris_gf - bris_season):.1f} pts")

# ============================================================
# VERDICT
# ============================================================
print("\n" + "=" * 70)
print("VERDICT: Do the teams that handle pressure best really win?")
print("=" * 70)

top_rated = pr_df.iloc[0]
print(f"\nHighest Pressure Rating: {top_rated['team']} ({top_rated['pressure_rating']:.1f})")
print(f"2026 Premiers: Brisbane Lions")
print(f"\nBrisbane's Grand Final: came back from {abs(h3-a3)} points down at 3QT,")
print(f"won Q4 by {abs(gf['h_q4']-gf['a_q4'])} points, won the flag by {abs(gf['h_total']-gf['a_total'])}.")
print(f"\nThe data says: the team that handles pressure best in the biggest")
print(f"moment of the biggest game wins the premiership. Brisbane proved it.")

# Save all key outputs
pr_df.to_csv("pressure_ratings.csv", index=False)
print(f"\nSaved pressure_ratings.csv")
print("Analysis complete.")
