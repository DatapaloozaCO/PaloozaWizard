from palooza_wizard.graph import PaloozaGraph
from palooza_wizard.algorithms.degree_importance import degree_importance, get_soup_nodes
from palooza_wizard.agent import get_agent_functions
import sys 
import requests
from bs4 import BeautifulSoup
import palooza_wizard.utils.files as files
import palooza_wizard.utils.process as process
import palooza_wizard.constants as ct

if __name__ == "__main__":

    
    website_name = "rubmaps"
    url = "https://www.rubmaps.ch/erotic-massage-chinese-goose-massage-cincinnati-oh-33075#rubmaps"
    soup = files.get_soup_from_url(url)
    soup = process.process_soup(soup)

    


  
    palooza_graph = PaloozaGraph()
    palooza_graph.get_graph(soup)
    print("Number of nodes: ", len(palooza_graph.G.nodes))
    print("Number of edges: ", len(palooza_graph.G.edges))

    min_depth = 1
    max_candidates = 5

    candidates = degree_importance(
        palooza_graph.G, 
        min_depth, 
        max_candidates
    )

    files.delete_all_files_in_folder(ct.IMPORTANCE_OUTPUT_FOLDER)

    get_soup_nodes(website_name, palooza_graph.G, soup, candidates)
    get_agent_functions()
    #url = "https://www.oulunlippo.fi/"
    #palooza_graph.get_soup(url)
    #palooza_graph.add_nodes()
    #sys.exit()

    #soup = soup.find("body")

    # Initialize global variables
    #G = nx.DiGraph()
    #colors = []
    #sizes = []
    #counter = 0
    #alpha = 10
    #labels = []

    #add_nodes(soup, "root")
    #G = nx.convert_node_labels_to_integers(G)

    #print("Number of nodes: ", len(G.nodes))
    #print("Number of edges: ", len(G.edges))