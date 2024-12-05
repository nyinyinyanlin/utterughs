from setuptools import setup, find_packages
from pathlib import Path

# Requirements
try:
  this_directory = Path(__file__).absolute().parent
  with open((this_directory / "requirements.txt"), encoding = "utf-8") as f:
    requirements = f.readlines()
  requirements = [line.strip() for line in requirements]
except FileNotFoundError:
  requirements = []
  
# Read README
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


# Metadata
setup(
  name = "UtterUghs",
  version = "0.1",
  author = "Nyi Nyi Nyan Lin",
  author_email = "nyinyinyanlin.mm@gmail.com",
  description = "Do you want a package to spit out utter ughs for you? Here you go!",
    long_description=long_description,
    long_description_content_type="text/markdown",
  license = "WTFPL",
  packages = find_packages(),
  install_requires = requirements
)