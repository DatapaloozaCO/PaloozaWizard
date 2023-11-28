from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(
    os.path.join(here, "README.md"), encoding="utf-8"
) as fh:
    long_description = "\\n" + fh.read()

requirements = []
with open("requirements.txt") as f:
    requirements = f.readlines()

setup(
    name="palooza_wizard",
    version=1,  #'{{VERSION_PLACEHOLDER}}',
    description="Datapalooza Scraper Framework",
    url="https://github.com/DatapaloozaCO/datapalooza_scraper_framework",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    # install_requires=requirements,
    keywords=["scraper", "crawler"],
)
