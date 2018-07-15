import folium
import pandas

webmap = folium.Map(location=[53.601353, -34.222003], zoom_start=2, tiles='Mapbox Bright')
webmap.add_child(folium.GeoJson(data=(open('files/world.json', 'r', encoding='utf-8-sig')).read()))

webmap.save('map3.html')