import folium
import pandas

webmap = folium.Map(location=[39.656523, -113.065719], zoom_start=5, tiles='Mapbox Bright')

data = pandas.read_csv('files/volcanoes.txt')

lat = list(data['LAT'])
lon = list(data['LON'])

fg = folium.FeatureGroup(name='My Feature Group')

for lt, ln in zip(lat, lon):
	fg.add_child(folium.Marker(location=[lt, ln]))

webmap.add_child(fg)
webmap.save('map2.html')