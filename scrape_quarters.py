import requests
import re
import pandas as pd

URL = "https://afltables.com/afl/seas/2026.html"
HDR = {"User-Agent": "Mozilla/5.0 (Macintosh) AFL Pressure Analysis - Sai Surapaneni"}

print("Fetching AFL Tables 2026 season...")
r = requests.get(URL, headers=HDR)
print(f"Status: {r.status_code}")
if r.status_code != 200:
    print("Failed. Try again in a minute.")
    raise SystemExit(1)

text = r.text

# The real HTML pattern for each team line:
# <a href="../teams/XXX">Team Name</a></td><td...><tt> Q1g.Q1b Q2g.Q2b Q3g.Q3b Q4g.Q4b </tt></td><td...> total</td>
# with &nbsp; as spacing inside the <tt> block

TEAM_LINE = re.compile(
    r'<a href="\.\./teams/[^"]+">([^<]+)</a></td>'
    r'<td[^>]*><tt>(.*?)</tt></td>'
    r'<td[^>]*>\s*(\d+)</td>'
)

QUARTER_SCORES = re.compile(r'(\d+)\.(\d+)')

VENUE_PAT = re.compile(r'Venue:</b>\s*<a[^>]*>([^<]+)</a>')
ROUND_PAT = re.compile(r'<b>Round (\d+)')
FINAL_PAT = re.compile(r'<b>(Wildcard Final|Qualifying Final|Elimination Final|Semi Final|Preliminary Final|Grand Final)</')

lines = text.split("\n")
games = []
current_round = None
current_final_type = None
pending_home = None
pending_venue = ""

for line in lines:
    # Check round header
    rm = ROUND_PAT.search(line)
    if rm:
        current_round = int(rm.group(1))
        current_final_type = None
        continue
    
    # Check finals header
    fm = FINAL_PAT.search(line)
    if fm:
        current_final_type = fm.group(1)
        continue
    
    # Check for a team game line
    tm = TEAM_LINE.search(line)
    if not tm:
        continue
    
    team_name = tm.group(1).strip()
    quarter_str = tm.group(2)
    total = int(tm.group(3))
    
    # Extract the 4 quarter scores from the tt block
    quarters = QUARTER_SCORES.findall(quarter_str)
    if len(quarters) != 4:
        continue
    
    q1g, q1b = int(quarters[0][0]), int(quarters[0][1])
    q2g, q2b = int(quarters[1][0]), int(quarters[1][1])
    q3g, q3b = int(quarters[2][0]), int(quarters[2][1])
    q4g, q4b = int(quarters[3][0]), int(quarters[3][1])
    
    # Check for venue in this line
    vm = VENUE_PAT.search(line)
    if vm:
        pending_venue = vm.group(1)
    
    if pending_home is None:
        # Home team
        pending_home = {
            "team": team_name,
            "q1g": q1g, "q1b": q1b, "q2g": q2g, "q2b": q2b,
            "q3g": q3g, "q3b": q3b, "q4g": q4g, "q4b": q4b,
            "total": total, "venue": pending_venue,
            "round": current_round, "final_type": current_final_type,
        }
        pending_venue = ""
    else:
        # Away team: pair with pending home
        h = pending_home
        
        # Convert cumulative to per-quarter points
        h_q1 = h["q1g"]*6 + h["q1b"]
        h_q2 = (h["q2g"]*6 + h["q2b"]) - h_q1
        h_q3 = (h["q3g"]*6 + h["q3b"]) - (h["q2g"]*6 + h["q2b"])
        h_q4 = h["total"] - (h["q3g"]*6 + h["q3b"])
        
        a_q1 = q1g*6 + q1b
        a_q2 = (q2g*6 + q2b) - a_q1
        a_q3 = (q3g*6 + q3b) - (q2g*6 + q2b)
        a_q4 = total - (q3g*6 + q3b)
        
        game_type = h["final_type"] if h["final_type"] else "H&A"
        rnd = h["final_type"] if h["final_type"] else h["round"]
        
        games.append({
            "round": rnd, "game_type": game_type,
            "home_team": h["team"], "away_team": team_name,
            "venue": h["venue"],
            "h_q1": h_q1, "h_q2": h_q2, "h_q3": h_q3, "h_q4": h_q4,
            "a_q1": a_q1, "a_q2": a_q2, "a_q3": a_q3, "a_q4": a_q4,
            "h_total": h["total"], "a_total": total,
            "h_goals_q1": h["q1g"], "h_goals_q2": h["q2g"]-h["q1g"],
            "h_goals_q3": h["q3g"]-h["q2g"], "h_goals_q4": h["q4g"]-h["q3g"],
            "a_goals_q1": q1g, "a_goals_q2": q2g-q1g,
            "a_goals_q3": q3g-q2g, "a_goals_q4": q4g-q3g,
            "h_behinds_q1": h["q1b"], "h_behinds_q2": h["q2b"]-h["q1b"],
            "h_behinds_q3": h["q3b"]-h["q2b"], "h_behinds_q4": h["q4b"]-h["q3b"],
            "a_behinds_q1": q1b, "a_behinds_q2": q2b-q1b,
            "a_behinds_q3": q3b-q2b, "a_behinds_q4": q4b-q3b,
        })
        pending_home = None

df = pd.DataFrame(games)

print(f"\n{'='*50}")
print(f"QA REPORT - 2026 AFL Quarter-by-Quarter Data")
print(f"{'='*50}")
print(f"Total games scraped: {len(df)}")

if len(df) == 0:
    print("ERROR: No games found. The HTML structure may have changed.")
    raise SystemExit(1)

ha = df[df["game_type"] == "H&A"]
finals = df[df["game_type"] != "H&A"]
print(f"Home and away: {len(ha)}")
print(f"Finals: {len(finals)}")

if len(finals):
    print(f"\nFinals breakdown:")
    print(finals["game_type"].value_counts().to_string())

# Quarter reconciliation
df["h_check"] = df["h_q1"] + df["h_q2"] + df["h_q3"] + df["h_q4"]
df["a_check"] = df["a_q1"] + df["a_q2"] + df["a_q3"] + df["a_q4"]
bad = df[(df["h_check"] != df["h_total"]) | (df["a_check"] != df["a_total"])]
print(f"\nQuarter reconciliation errors: {len(bad)}")

# Grand Final
gf = df[df["game_type"] == "Grand Final"]
if len(gf):
    g = gf.iloc[0]
    print(f"\nGrand Final: {g['home_team']} {g['h_total']} vs {g['away_team']} {g['a_total']}")
    print(f"  {g['home_team']} by Q: {g['h_q1']}, {g['h_q2']}, {g['h_q3']}, {g['h_q4']}")
    print(f"  {g['away_team']} by Q: {g['a_q1']}, {g['a_q2']}, {g['a_q3']}, {g['a_q4']}")

df.drop(columns=["h_check", "a_check"], inplace=True)
df.to_csv("quarters_2026.csv", index=False)
print(f"\nSaved quarters_2026.csv ({len(df)} games, {len(df.columns)} columns)")
print("Done.")
