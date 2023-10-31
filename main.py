from palooza_wizard.graph import PaloozaGraph
import palooza_wizard.algorithms as wizard_algos
import palooza_wizard.utils as wizard_utils
from palooza_wizard.agent import get_agent_functions
import palooza_wizard.constants as ct

if __name__ == "__main__":

    # Clean all output folders
    #wizard_utils.clean_all_output_folders()

    website_name = "startupeable"
    url = "https://startupeable.com/glosario/que-es-una-startup/"
    soup = wizard_utils.download_or_load_soup(url, "startupeable.html", use_proxies=False)
    soup = wizard_utils.process_soup(soup)
    palooza_graph = PaloozaGraph()
    palooza_graph.get_graph(soup, labels_to_integers = False)
    min_depth = 0
    max_candidates = 10

    # Get candidates
    candidates = wizard_algos.degree_importance(
        palooza_graph.G, 
        palooza_graph.root,
        min_depth, 
        max_candidates
    )

    # Get soup nodes.
    wizard_utils.get_soup_nodes(
        website_name, 
        palooza_graph.G, 
        soup, 
        candidates, 
        verbose = True
    )
        
    # Using file: ./outputs/soups/base_soup.html
    # Using file: ./outputs/soups/base_soup.html
    #get_agent_functions()

