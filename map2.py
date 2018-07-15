import folium
import pandas

webmap = folium.Map(location=[39.656523, -113.065719], zoom_start=5, tiles='Mapbox Bright')

data = pandas.read_csv('files/volcanoes.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

fg = folium.FeatureGroup(name='My Feature Group')

for lt, ln, el in zip(lat, lon, elev):
	fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + ' m'))

webmap.add_child(fg)
webmap.save('map2.html')