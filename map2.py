import folium
import pandas

def elevation_color_status(elevation):
	if elevation < 1000:
		return 'green'
	elif 1000 <= elevation < 3000:
		return 'orange'
	else:
		return 'red'

webmap = folium.Map(location=[39.656523, -113.065719], zoom_start=5, tiles='Mapbox Bright')

data = pandas.read_csv('files/volcanoes.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

fg = folium.FeatureGroup(name='My Feature Group')

for lt, ln, el in zip(lat, lon, elev):
	fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el) + ' m', 
		fill=True, fill_color=elevation_color_status(el), fill_opacity='0.7', color='grey'))

webmap.add_child(fg)
webmap.save('map2.html')