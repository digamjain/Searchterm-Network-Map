<h1 align="center">Searchterm Network Map</h1>

<p align="center">
  
  <a href="https://img.shields.io/github/pipenv/locked/python-version/digamjain/Searchterm-Network-Map">
    <img src="https://img.shields.io/github/pipenv/locked/python-version/digamjain/Searchterm-Network-Map" /></a>
    
  <a href="https://img.shields.io/github/pipenv/locked/dependency-version/digamjain/Searchterm-Network-Map/streamlit">
    <img src="https://img.shields.io/github/pipenv/locked/dependency-version/digamjain/Searchterm-Network-Map/streamlit" /></a>
  
  <a href="https://img.shields.io/github/languages/code-size/digamjain/Searchterm-Network-Map">
    <img src="https://img.shields.io/github/languages/code-size/digamjain/Searchterm-Network-Map" /></a>
  
  <a href="https://img.shields.io/github/license/digamjain/Searchterm-Network-Map">
    <img src="https://img.shields.io/github/license/digamjain/Searchterm-Network-Map" /></a>
 
 <a href="https://img.shields.io/github/issues/digamjain/Searchterm-Network-Map">
    <img src="https://img.shields.io/github/issues/digamjain/Searchterm-Network-Map" /></a>
  
  <a href="https://img.shields.io/github/contributors/digamjain/Searchterm-Network-Map">
    <img src="https://img.shields.io/github/contributors/digamjain/Searchterm-Network-Map" /></a>
  
 </p>

<p align="center"><img src="https://raw.githubusercontent.com/digamjain/Search-Term-NetworkTree/Staged_changes1/1editing.gif"></p>

**Searchterm Network Map** is a deployable webapp keyword mapper. <br>
It uses the search term entered to form a network map with the information available to it and is stored in its database.

## Tools & Frameworks
```
- Cockroach db - For cloud database support
- Streamlit - For easy to deploy webapp
- pyvis library - For network map
```

## Installation
```
- git clone https://github.com/digamjain/Searchterm-Network-Map
- cd Searchterm-Network-Map
- pip install -r requirements.txt
- update the networkmap/dbfetch.py file line number 8 for various required fields
- alternatively to the above step you can also create a file named secrets.toml under .streamlit in the current directory and fill in the necessary fields
- streamlit run run.py
```
### Installing in pipenv environment
```
 - git clone https://github.com/digamjain/Searchterm-Network-Map
 - cd Searchterm-Network-Map
 - pipenv shell
 - pipenv install
 - update the networkmap/dbfetch.py file line number 8 for various required fields
 - alternatively to the above step you can also create a file named secrets.toml under .streamlit in the current directory and fill in the necessary fields
 - streamlit run run.py
```
## Features
```
- Uses cloub database hence easily scalable even after continous deployment
- Interactive nodes and edges
- Nodes show neighbours information when mouse hovers over them
- Edges widths are accoding to its relationship strength with the nodes
- Map limited to 3 level relations though easily upgradable/downgradeable
- Easy to navigate the nodes
- Easy to use and understand webapp
- Generates output network map on an HTML file when deployed locally
- Generates data and relation strength in csv form when deployed locally
``` 
## Restraints
Currently the database only has 'car' information thus other searches won't return a network map.
