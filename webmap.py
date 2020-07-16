import folium
import pandas as pd
import os

# print(os.getcwd())

### Reading volcano address txt
os.chdir('/Users/luke/Desktop/Python/GitClone/PROJECT-Volcano-and-Population-Web-Map/volcanoes')
v_data = pd.read_csv("Volcanoes.txt")
print(v_data)
# Selecting the informations to be used
geolat = list(v_data['LAT'])
geolon = list(v_data['LON'])
name = list(v_data['NAME'])
status = list(v_data['STATUS'])
elev = list(v_data['ELEV'])
type = list(v_data['TYPE'])


### Making webmap in html
os.chdir('/Users/luke/Desktop/Python/GitClone/PROJECT-Volcano-and-Population-Web-Map/mapping')
map = folium.Map(location = [44.104014,-121.292043], zoom_start = 7, tiles = 'Stamen Toner')

feature_group = folium.FeatureGroup("Locations")
for lat,lon,name,status,elev,type in zip(geolat,geolon,name,status,elev,type):

    html = f'''<b>{name}</b> <br>
    <br>
     Status: {status} <br>
     Type: {type} <br>
     Elevation: {elev} m<br>
     Latitude: {lat} <br>
     Longitude: {lon}'''

    iframe = folium.IFrame(html,
                           width = 260,
                           height = 150)

    popup = folium.Popup(iframe, max_width = 260)

    feature_group.add_child(folium.CircleMarker(location = [lat,lon],
    popup = popup,
    fill = True, fill_opacity = 0.7))

map.add_child(feature_group)
map.save("map.html")
