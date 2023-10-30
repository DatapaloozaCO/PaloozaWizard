import joblib
parents_name = joblib.load("parents_name.joblib")
example = parents_name[200].split("*")
#print(example)


def process_parent_name(element_path):
    path_info = {}

    element_path[0] = element_path[0].replace("root", "")
    depth = 0

    for edge in element_path:
        edge = edge.split("__")
        edge = [x for x in edge if x != '']
        if len(edge) == 0: 
            continue
        tag = edge[1]
        value = edge[0]
        path_info[depth] = (tag, value)
        depth += 1
    return path_info

path_info = process_parent_name(example)
for key, value in path_info.items(): 
    print(key, value)