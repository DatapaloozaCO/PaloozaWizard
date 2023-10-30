from palooza_wizard.graph import PaloozaGraph
from palooza_wizard.algorithms.degree_importance import degree_importance, get_soup_nodes
from palooza_wizard.agent import get_agent_functions
import palooza_wizard.utils.files as files
import palooza_wizard.utils.process as process
import palooza_wizard.constants as ct

if __name__ == "__main__":
    #website_name = "rubmaps"
    #url = "https://www.rubmaps.ch/erotic-massage-chinese-goose-massage-cincinnati-oh-33075#rubmaps"
    #url = "https://baldurconnect.com/"

    website_name = "citytourgirls"
    url = "https://www.citytourgirls.com/"
    soup = files.download_or_load_soup(url, "citytourgirls.html")
    soup = process.process_soup(soup)
    palooza_graph = PaloozaGraph()
    palooza_graph.get_graph(soup, labels_to_integers = False)
    min_depth = 0
    max_candidates = 10

    # Get candidates
    candidates = degree_importance(
        palooza_graph.G, 
        palooza_graph.root,
        min_depth, 
        max_candidates
    )
    
    # Clean importance folder.
    files.delete_all_files_in_folder(ct.IMPORTANCE_OUTPUT_FOLDER)

    # Clean soup folder.
    files.delete_all_files_in_folder(ct.SOUPS_OUTPUT_FOLDER)

    # Get soup nodes.
    get_soup_nodes(
        website_name, 
        palooza_graph.G, 
        soup, 
        candidates, 
        verbose = True
    )
    
    # Using file: ./outputs/soups/base_soup.html
    # Using file: ./outputs/soups/base_soup.html