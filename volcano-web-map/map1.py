import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

def color_producer(elevation):
  if elevation < 1000:
    return 'green'
  elif 1000 <= elevation < 3000:
    return 'orange'
  else:
    return 'red'

map = folium.Map(location=[38.58, -113], zoom_start=5, tiles='Stamen Terrain')

# feature group
fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el, name in zip(lat, lon, elev, name):
  html = f"Volcano name:<a href='https://www.google.com/search?q={name}' target='_blank'> {name}</a><br>Height: {int(el)}m"
  iframe = folium.IFrame(html=html, width=200, height=100)

  fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), 
  radius=6, weight=1, color='grey', fill_color=color_producer(el), fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: { 
  'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 
              'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 
              'red'
}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('Map1.html')