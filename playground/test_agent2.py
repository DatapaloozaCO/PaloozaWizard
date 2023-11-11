from outputs.agent.rubmaps_cleveland_hot_stones_6 import rubmaps_cleveland_hot_stones_6
import json
website_name = "./rubmaps_cleveland_hot_stones.html"
with open(website_name, "r") as f:
    html_code = str(f.read())
data = rubmaps_cleveland_hot_stones_6(html_code)
with open("data.json", "w") as f:
    f.write(json.dumps(data, indent=4))