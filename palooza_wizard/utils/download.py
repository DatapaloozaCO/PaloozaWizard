import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import Optional

def download_html(url: str, save_html: Optional[bool] = False, file_path: Optional[str] = None) -> BeautifulSoup:
    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser")
    if save_html:
        with open(file_path, "w") as f:
            f.write(str(soup))
    return soup