import folium
import pandas

webmap = folium.Map(location=[53.601353, -34.222003], zoom_start=2, tiles='Mapbox Bright')
webmap.add_child(folium.GeoJson(data=(open('files/world.json', 'r', encoding='utf-8-sig')).read(),
	style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
	else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

webmap.save('map3.html')