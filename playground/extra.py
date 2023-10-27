
load_html = load_html("./oulunlippo.html")
data = get_players(load_html)
import json
with open("data.json", "w") as f:
    f.write(json.dumps(data))