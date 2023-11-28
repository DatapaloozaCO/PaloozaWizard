from palooza_wizard.graph import PaloozaGraph
import palooza_wizard.algorithms as wizard_algos
import palooza_wizard.utils as wizard_utils
import palooza_wizard.agent as agent
import palooza_wizard.constants as ct
from bs4 import BeautifulSoup

if __name__ == "__main__":

    # Clean all output folders
    wizard_utils.clean_all_output_folders()

    website_name = "rubmaps"
    
    #url = "https://www.rubmaps.ch/erotic-massage-hot-stones-spa-cleveland-oh-184586"
    #url = "https://www.amazon.com/Legend-Zelda-Breath-Wild-Nintendo-Switch/dp/B097B2YWFX/ref=sr_1_2?crid=AMBZI2YGNFC3&keywords=zelda%2Bvideo%2Bgame&qid=1698834691&sprefix=zelda%2Bvideogame%2Caps%2C241&sr=8-2&th=1"
    #url = "https://www.rubmaps.ch/erotic-massage-windsor-spa-chicago-il-190400#rubmaps"
    #soup = wizard_utils.download_or_load_soup(url, f"{website_name}.html", use_proxies=False)
    #soup = wizard_utils.process_soup(soup)

    
    #soup = soup.find(attrs={"id": "location-container"})
    #soup = BeautifulSoup(f"<body>{str(soup)}</body>")
    #soup = wizard_utils.process_soup(soup)
    with open("soup3.html", "r") as f:
        soup = BeautifulSoup(f.read())
    soup = wizard_utils.process_soup(soup)


    palooza_graph = PaloozaGraph()
    palooza_graph.get_graph(soup, labels_to_integers = False)
    min_depth = 0
    max_candidates = 20

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
        
    # Get agent functions.
    agent.get_agent_functions()

