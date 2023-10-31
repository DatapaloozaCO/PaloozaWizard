from bs4 import BeautifulSoup
import os
import requests
from requests.auth import HTTPProxyAuth
import palooza_wizard.constants as ct
import shutil
from typing import List

def get_files_in_folder(folder_path: str, full_path: bool = True) -> List[str]:
    if not file_exists(folder_path):
        raise Exception("Folder not found")
    files = os.listdir(folder_path)
    if not full_path:
        return files
    files = [os.path.join(folder_path, file) for file in files]
    return files

def get_request_with_proxies(url: str, use_proxies: bool = True):
    if use_proxies:
        auth = HTTPProxyAuth(ct.PROXY_USERNAME, ct.PROXY_PASSWORD)
        data = requests.get(
            url = url, 
            proxies = ct.PROXIES, 
            auth = auth, 
            headers = {"User-Agent": ct.FAKE_USER_AGENT},
            timeout = ct.REQUEST_TIMEOUT
        )
    else:
        data = requests.get(
            url = url, 
            headers = {"User-Agent": ct.FAKE_USER_AGENT}, 
            timeout = ct.REQUEST_TIMEOUT
        )
    return data

def create_folder_if_not_exists(folder_path: str) -> bool:
    """This function check if a folder exists in a given path, otherwise, it creates the folder"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return True

def file_exists(file_path: str) -> bool:
    """This function check if a file exists in a given path"""
    return os.path.exists(file_path)

def get_html_from_file(file_path: str) -> str:
    """Load HTML file"""
    with open(file_path, "r") as f:
        html = f.read()
    return html

def get_soup_from_file(file_path: str) -> BeautifulSoup: 
    """Load HTML file and return a BeautifulSoup object"""
    html = get_html_from_file(file_path)
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_html_from_url(url: str, use_proxies: bool = True) -> str:
    """Download HTML file and return a string object"""
    data = get_request_with_proxies(url, use_proxies)
    return data.content

def get_soup_from_url(url: str, use_proxies: bool = True) -> BeautifulSoup:
    """Download HTML file and return a BeautifulSoup object using get_html_from_url function"""
    soup = get_html_from_url(url, use_proxies = use_proxies)
    soup = BeautifulSoup(soup, "html.parser")
    return soup

def save_html_to_file(html: str, file_path: str) -> None:
    """Save HTML string to a file"""
    with open(file_path, "w") as f:
        f.write(html)

def save_soup_to_file(soup: BeautifulSoup, file_path: str) -> None:
    """Save BeautifulSoup object to a file"""
    html = str(soup)
    save_html_to_file(html, file_path)

def download_or_load_soup(url: str, file_path: str, use_proxies: bool = True) -> BeautifulSoup:
    """Download HTML file or load HTML file"""
    if file_exists(file_path):
        soup = get_soup_from_file(file_path)
    else:
        soup = get_soup_from_url(url, use_proxies = use_proxies)
        save_soup_to_file(soup, file_path)
    return soup

def delete_all_files_in_folder(folder_path: str):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def clean_all_output_folders():
    for folder in ct.FOLDERS:
        delete_all_files_in_folder(folder)
