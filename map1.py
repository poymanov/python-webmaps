import folium

webmap = folium.Map(location=[38.931303, -77.049646], zoom_start=8, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='My Feature Group')

coordinates = [[38.931303, -77.049646], [38.992155, -80.247268]]

for coordinate in coordinates:
	fg.add_child(folium.Marker(location=coordinate, popup='My Marker', icon=folium.Icon(color='green')))

webmap.add_child(fg);
webmap.save('map1.html')