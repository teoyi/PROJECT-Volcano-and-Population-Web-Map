import folium
import os
os.chdir('/Users/luke/Desktop/Python/GitClone/PROJECT-Volcano-and-Population-Web-Map/mapping')
print(os.getcwd())

### Making webmap in html
map = folium.Map(location = [44.104014,-121.292043], zoom_start = 7, tiles = 'Stamen Terrain')
map.save("map.html")
