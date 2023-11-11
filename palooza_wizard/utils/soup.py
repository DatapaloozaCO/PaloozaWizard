from bs4 import BeautifulSoup
from typing import List 
import palooza_wizard.constants as ct
import networkx as nx

def process_parent_name(element_path: str) -> dict:
    """This function maps a string element_path to a dictionary
    Input: nodo1__div__*__nodo2__div__*__nodo3__div__* 
    Output: {0: ('div', 'nodo1'), 1: ('div', 'nodo2'), 2: ('div', 'nodo3')}
    """
    path_info = {}
    element_path = element_path.replace("root", "").split("*")
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

def get_element_with_path(soup: BeautifulSoup, path: dict):
    """Based on a soup and a path to a important node, recursively 
    explore the soup to get the element.
    {0: ('body', '0'), 1: ('div', '1'), 2: ('div', '4')}
    #print(path)
    #print("This is a soup ", type(soup))
    """
    counter = 0
    for _, value in path.items():
        counter += 1 
        # Skip body tag.
        if counter == 1:
            continue
        soup = soup.findChildren(recursive=False)[int(value[1]) - 1]
    return soup
 
def get_soup_nodes(
        website_name: str,
        graph: nx.DiGraph, 
        soup: BeautifulSoup,
        candidates: List[int], 
        verbose: bool = False
    ):
    """Based on the computed candidates, get the soup of each one of them.
    Note that this method is agnostic to any node importance algorithm.
    """
    # Get selectors. 
    parents_name = nx.get_node_attributes(graph, "node_name")
    for key, value in parents_name.items():
        parents_name[key] = process_parent_name(value)

    # Get soups to process.
    counter = 0
    for candidate in candidates:
        candidate_path = parents_name[candidate]
        soup_candidate = get_element_with_path(soup, candidate_path)
        with open(
            f"{ct.IMPORTANCE_OUTPUT_FOLDER}/{website_name}_{counter + 1}.html",
            "w", 
            encoding="utf-8") as f:
             f.write(str(soup_candidate))
        counter += 1