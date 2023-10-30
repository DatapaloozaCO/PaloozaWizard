# Import libraries
from bs4 import BeautifulSoup
import networkx as nx
import requests
import random
from typing import List
import palooza_wizard.constants as ct

class PaloozaGraph:
    def __init__(self) -> None:
        # Initialize global variables
        self.G = nx.DiGraph()
        self.colors = []
        self.sizes = []
        self.counter = 0
        self.labels = []
        self.root = "root__1__body__*"

    # Get colors
    def get_color(self, soup: BeautifulSoup) -> None:
        if soup.get("class") != None:
            if "escortsModels" in soup.get("class"):
                self.colors.append("red")
                self.sizes.append(50)
            elif "vipEscortsArea" in soup.get("class"):
                self.colors.append("red")
                self.sizes.append(50)
            elif "vipListing" in soup.get("class"):
                self.colors.append("blue")
                self.sizes.append(50)
            else:
                self.colors.append("gray")
                self.sizes.append(1)
        else:
            self.colors.append("gray")
            self.sizes.append(1)

    # Get node name
    def get_node_name(
            self,
            soup: BeautifulSoup,
            parent_name: str,
            index: int
        ) -> None:
        self.get_color(soup)
        node_name = f"{parent_name}__{index}__{str(soup.name)}__*"
        return node_name

    # Get node properties
    def get_node_properties(self, soup: BeautifulSoup, parent_name: str, node_name: str) -> dict:
        properties = {
            "tag": soup.name, # h1, h2, p, ..., 
            "parent_name": parent_name,
            "node_name": node_name,
            "number": self.counter,
            "class": soup.get("class"), # ['a', 'b']
            "id": soup.get("id"),       #
            ct.SELECTOR_LABEL: {
                "tag": soup.name,
                "class": soup.get("class"),
                "id": soup.get("id")
            }
        }
        return properties

    # Add nodes to the graph
    def add_nodes(self, soup: BeautifulSoup, parent_name: str = "", index: int = 1, depth: int = 0):

        if soup is None:
            return

        if soup.name:

            # Define node's name.
            node_name = self.get_node_name(soup, parent_name, index)

            # Add node to the graph.
            properties = self.get_node_properties(soup, parent_name, node_name)
            self.G.add_node(node_name, **properties)
            self.counter += 1

            # Add edge to the graph.
            if parent_name != ct.ROOT_LABEL:
                self.G.add_edge(parent_name, node_name)

            # Get children
            children = soup.findChildren(recursive=False)

            # While there is just one children, keep going down
            #while len(children) == 1:
            #    children = children[0]
            #    children = children.findChildren(recursive=False)

            # Add children only if there is more than 1 children
            #if len(children) > 1:
            for i in range(len(children)):
                self.add_nodes(children[i], node_name, i + 1, depth + 1)

    def get_graph(self, soup: BeautifulSoup, labels_to_integers: bool = True):
        self.add_nodes(soup, ct.ROOT_LABEL)
        if labels_to_integers:
            self.G = nx.convert_node_labels_to_integers(self.G)
            self.root = 0