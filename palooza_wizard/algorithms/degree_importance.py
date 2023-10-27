import networkx as nx
from typing import List
import palooza_wizard.constants as ct
from bs4 import BeautifulSoup
import os 

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
        candidates: List[int], 
        min_depth: int
    ):
    nodes_depth = nx.shortest_path_length(graph, 0) 
    for candidate in candidates: 
        if nodes_depth[candidate] > min_depth:
          yield candidate

def filter_candidates(
        graph: nx.DiGraph, 
        candidates: List[int], 
        min_depth: int = 3
    ):
    candidates = [x for x in filter_candidates_by_depth(graph, candidates, min_depth)]
    candidates = [x for x in filter_candidates_by_containment(graph, candidates)]
    return candidates 

def degree_importance(
        graph: nx.DiGraph, 
        min_depth: int, 
        max_candidates: int
    ) -> List[int]:

    # Get degree of nodes. 
    nodes_degree = list(graph.degree(graph.nodes()))

    # Sort nodes by degree.
    nodes_degree.sort(key = lambda z: z[1], reverse=True)

    print(nodes_degree[:max_candidates])

    # Get candidates of nodes.
    candidates = [x[0] for x in nodes_degree]

    # Filter candidates.
    candidates = filter_candidates(graph, candidates, min_depth = min_depth)

    # Max candidates.
    candidates = candidates[:max_candidates]

    # Return candidates.
    return candidates

def get_soup_nodes(
        website_name: str,
        graph: nx.DiGraph, 
        soup: BeautifulSoup,
        candidates: List[int]
    ):
    # Get selectors. 
    selectors = nx.get_node_attributes(graph, ct.SELECTOR_LABEL)

    for candidate in candidates:
        selector = selectors[candidate]
        candidate_section = soup.find(
            selector['tag'], 
            attrs = {
                "id": selector['id'], 
                "class": selector['class']
            }
        )

        # nodo3 (no quedo dentro de los candidatos) => 5 hijos.
        # nodo => 30 hijos  selector['tag'] = div

        with open(f"{ct.IMPORTANCE_OUTPUT_FOLDER}/{website_name}_{candidate}.html", "w") as f:
            f.write(str(candidate_section))