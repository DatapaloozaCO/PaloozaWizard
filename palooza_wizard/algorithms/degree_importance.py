import networkx as nx
from typing import List
import palooza_wizard.constants as ct
from bs4 import BeautifulSoup
import os
import joblib
import sys


def filter_candidates_by_containment(
    graph: nx.DiGraph, candidates: List[int]
):
    """Para todo g1, g2 e I, g1 no contiene a g2 ni g2 a g1"""
    inadmissable_nodes = []
    for candidate in candidates:
        if candidate in inadmissable_nodes:
            continue
        descendants = list(nx.descendants(graph, candidate))
        inadmissable_nodes = inadmissable_nodes + descendants
        yield candidate


def filter_candidates_by_depth(
    graph: nx.DiGraph, root, candidates: List[int], min_depth: int
):
    nodes_depth = nx.shortest_path_length(graph, root)
    for candidate in candidates:
        if nodes_depth[candidate] > min_depth:
            yield candidate


def filter_candidates(
    graph: nx.DiGraph,
    root: str,
    candidates: List[int],
    min_depth: int = 3,
):
    candidates = [
        x
        for x in filter_candidates_by_depth(
            graph, root, candidates, min_depth
        )
    ]
    candidates = [
        x for x in filter_candidates_by_containment(graph, candidates)
    ]
    return candidates


def degree_importance(
    graph: nx.DiGraph,
    root: str,
    min_depth: int,
    max_candidates: int,
    verbose: bool = False,
) -> List[int]:

    # Get degree of nodes.
    nodes_degree = list(graph.degree(graph.nodes()))

    # Sort nodes by degree.
    nodes_degree.sort(key=lambda z: z[1], reverse=True)

    nodes_degree = nodes_degree[:max_candidates]

    # for key, value in nodes_degree:
    #    print(f"{key}: {value}")

    # Get candidates of nodes.
    candidates = [x[0] for x in nodes_degree]

    # Filter candidates.
    candidates = filter_candidates(
        graph, root, candidates, min_depth=min_depth
    )

    if verbose:
        print("Candidates")
        print(candidates)

    # Return candidates.
    return candidates
