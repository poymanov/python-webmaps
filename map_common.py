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

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon, elev):
	fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el) + ' m', 
		fill=True, fill_color=elevation_color_status(el), fill_opacity='0.7', color='grey'))

fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=(open('files/world.json', 'r', encoding='utf-8-sig')).read(),
	style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
	else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

webmap.add_child(fgv)
webmap.add_child(fgp)
webmap.add_child(folium.LayerControl())
webmap.save('map_common.html')