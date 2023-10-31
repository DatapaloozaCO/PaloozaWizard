from outputs.agent.startupeable_1 import function_1
from outputs.agent.startupeable_2 import function_2

with open("startupeable.html", "r") as f:
    html_code = str(f.read())
data1 = function_1(html_code)
#data2 = function_2(html_code)

print(data1)

