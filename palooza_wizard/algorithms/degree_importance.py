import networkx as nx
from typing import List
import palooza_wizard.constants as ct
from bs4 import BeautifulSoup
import os 
import joblib 
import sys 

def filter_candidates_by_containment(
        graph: nx.DiGraph, 
        candidates: List[int]
    ):
    """Para todo g1, g2 e I, g1 no contiene a g2 ni g2 a g1
    """
    inadmissable_nodes = []
    for candidate in candidates:
        if candidate in inadmissable_nodes:
          continue
        descendants = list(nx.descendants(graph, candidate))
        inadmissable_nodes = inadmissable_nodes + descendants
        yield candidate

def filter_candidates_by_depth(
        graph: nx.DiGraph, 
        root,
        candidates: List[int], 
        min_depth: int
    ):
    nodes_depth = nx.shortest_path_length(graph, root) 
    for candidate in candidates: 
        if nodes_depth[candidate] > min_depth:
          yield candidate

def filter_candidates(
        graph: nx.DiGraph, 
        root: str,
        candidates: List[int], 
        min_depth: int = 3
    ):
    candidates = [x for x in filter_candidates_by_depth(graph, root, candidates, min_depth)]
    candidates = [x for x in filter_candidates_by_containment(graph, candidates)]
    return candidates 

def degree_importance(
        graph: nx.DiGraph, 
        root: str, 
        min_depth: int, 
        max_candidates: int
    ) -> List[int]:

    # Get degree of nodes. 
    nodes_degree = list(graph.degree(graph.nodes()))

    # Sort nodes by degree.
    nodes_degree.sort(key = lambda z: z[1], reverse=True)

    nodes_degree = nodes_degree[:max_candidates]

    #for key, value in nodes_degree:
    #    print(f"{key}: {value}")

    # Get candidates of nodes.
    candidates = [x[0] for x in nodes_degree]

    # Filter candidates.
    candidates = filter_candidates(graph, root, candidates, min_depth = min_depth)

    #print("Candidates")
    #print(candidates)

    # Return candidates.
    return candidates

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
    # {0: ('body', '0'), 1: ('div', '1'), 2: ('div', '4')}
    #print(path)
    #print("This is a soup ", type(soup))
    values = list()
    counter = 0
    for key, value in path.items():
        counter += 1
        if counter == 1:

            continue
        soup = soup.findChildren(recursive=False)[int(value[1]) - 1]
    print(values)
    return soup
 
def get_soup_nodes(
        website_name: str,
        graph: nx.DiGraph, 
        soup: BeautifulSoup,
        candidates: List[int], 
        verbose: bool = False
    ):

    # Get selectors. 
    selectors = nx.get_node_attributes(graph, "selector")
    parents_name = nx.get_node_attributes(graph, "node_name")
    for key, value in parents_name.items():
        parents_name[key] = process_parent_name(value)

    print("Soup that we are going to pass: ", type(soup))
    print(f"Using file: {ct.SOUPS_OUTPUT_FOLDER}/base_soup.html")
    with open(f"{ct.SOUPS_OUTPUT_FOLDER}/base_soup.html", "w") as f:
        f.write(str(soup))

    print("Number of candidates: ", len(candidates))

    # Get soups to process.
    counter = 0
    for candidate in candidates:
        candidate_path = parents_name[candidate]
        print("---")
        counter+=1      
        print(f"counter: {counter}")
        print("Candidate: ", candidate)
        soup_candidate = get_element_with_path(soup, candidate_path)
        print("Selector: ", selectors[candidate])
        #print("Candidate path: ", candidate_path)
        #print("Content: ", soup_candidate.text.strip().replace(" ", ""))

        with open(f"{ct.IMPORTANCE_OUTPUT_FOLDER}/{website_name}_{candidate}.html", "w") as f:
             f.write(str(soup_candidate))