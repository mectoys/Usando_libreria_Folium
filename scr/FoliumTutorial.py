import os.path
import random
import folium
import numpy as np
import pandas as pd
from folium import plugins
from folium.plugins import Draw


def SaveLocation():
    dirname = os.path.dirname(__file__)
    dir = r"Mapas\foliumtutorial.html"
    savelocation = os.path.join(dirname, dir)
    return savelocation


# 1
def DisplayWebMapTiles():
    m = folium.Map()
    m.save(SaveLocation())


# 2
def DisplayWebMapName():
    number = random.randint(0, 3)
    Name_Tiles = ["Stamen Terrain", "Stamen Toner", "cartodb positron", "OpenStreetMap"]
    m = folium.Map(tiles="Stamen Terrain")
    m.save(SaveLocation())


# 3
# latitud y longitud
def DisplayGeolocation():
    m = folium.Map(location=(49.25, -123.12), tiles="cartodb positron")
    m.save(SaveLocation())


# 4
# Zoom
def DisplayMapWithZoom():
    m = folium.Map(location=(30, 10), zoom_start=5, tiles="cartodb positron")
    m.save(SaveLocation())


# 5
# GoeJsonLayer
def DisplayGeoJSONLayer():
    political_countries_url = (
        "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
    )
    m = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron")

    folium.GeoJson(political_countries_url).add_to(m)
    m.save(SaveLocation())


# 6
# marcadores
def DisplayMarkerLayer():
    m = folium.Map(location=(100, 10), zoom_start=2, tiles="cartodb positron")
    folium.Marker(location=[34.06, -118.25]).add_to(m)
    m.save(SaveLocation())


# 7
# Marcador con Icono
def DisplayMarkerWithIcon():
    # https://fontawesome.com/v4/icon/bandcamp
    m = folium.Map(location=(34.06, -110.25), zoom_start=8, tiles="cartodb positron")
    folium.Marker(location=[34.06, -118.25], icon=folium.Icon(icon="podcast", prefix='fa', color="red")).add_to(m)

    m.save(SaveLocation())


# 8
def AdCircleMarker():
    m = folium.Map(location=(34.06, -110.25), zoom_start=8, tiles="cartodb positron")
    folium.CircleMarker(
        location=[34.06, -118.25],
        radius=45,
        fill=True,
        color="blue",
        fill_color="red",
        fill_opacity=0.50,
        tooltip="Hola mapa"
    ).add_to(m)
    m.save(SaveLocation())


# 9
def AddServeralMarker():
    coords = pd.DataFrame({'lon': [34.06, 34.17, 34.42],
                           'lat': [-118.25, -118.40, -118.89]})

    m = folium.Map(location=[34.06, -118.25], zoom_start=8)

    for index, row in coords.iterrows():
        folium.Marker(location=[row['lon'], row['lat']]).add_to(m)
        m.save(SaveLocation())


# 10
def AddCircle():
    # Radio de 50 km
    m = folium.Map(location=[34.06, -118.25], zoom_start=8)
    folium.Circle(
        location=[34.06, -118.25],
        radius=60000,
        color="red",
        fill=True,
        fill_color="yellow").add_to(m)
    m.save(SaveLocation())


# 11
def AddRectagle():
    m = folium.Map(location=[34.06, -118.25], zoom_start=8)
    upper_left = [34.15, -118.44]
    upper_right = [34.15, -118.06]
    lower_right = [33.89, -118.06]
    lower_left = [33.89, -118.44]

    folium.Rectangle(
        bounds=[upper_left, upper_right, lower_right, lower_left],
        stroke=True,
        fill=True,
        color="blue",
        fill_color="#3388ff",
        fill_opaacity=0.8).add_to(m)
    m.save(SaveLocation())


# 12
def AddPopups():
    m = folium.Map(location=[34.06, -118.25], zoom_start=8)
    folium.CircleMarker(
        location=[34.06, -118.25],
        fill=True, popup="<h2>Estoy en los Angeles!</h2>").add_to(m)
    m.save(SaveLocation())


# 13
def AddLayers():
    m = folium.Map(location=[34.06, -118.25], zoom_start=8)

    folium.CircleMarker(
        location=[34.06, -118.35]).add_to(
        folium.FeatureGroup(name="Circle Marker").add_to(m))

    folium.Marker(location=[34.14, -118.35]).add_to(
        folium.FeatureGroup(name="Marker").add_to(m))

    folium.LayerControl().add_to(m)
    m.save(SaveLocation())


# 14
def AddPluginMiniMap():
    m = folium.Map(location=[34.06, -118.25], zoom_start=8)
    plugins.MiniMap().add_to(m)
    m.save(SaveLocation())


# 15
def AddPluginTerminator():
    m = folium.Map(location=[34.06, -118.25], zoom_start=8)
    plugins.Terminator().add_to(m)
    m.save(SaveLocation())


# 16
def AddPluginGeocoder():
    m = folium.Map(location=[34.06, -118.25], zoom_start=8)
    plugins.Geocoder().add_to(m)
    m.save(SaveLocation())


# 17
def AddPluginsClusterMarker():
    m = folium.Map(location=[34.06, -118.25], zoom_start=8)
    data = np.array([np.random.uniform(low=25, high=50, size=100),
                     np.random.uniform(low=-125, high=-70, size=100)]).T
    print(data)
    plugins.MarkerCluster(data).add_to(m)
    m.save(SaveLocation())


# 18
def AddpluginHeatmap():
    m = folium.Map(location=[34.06, -118.25], zoom_start=5)
    data = np.array([np.random.normal(35, 2, size=100),
                     np.random.normal(-80, 2, size=100)]).T

    print(data)
    plugins.HeatMap(data).add_to(m)
    m.save(SaveLocation())
#19
#No es plugin es parte de Folium permite agregar lineas poligono.
def AddPolyLiner():
    m = folium.Map(location=[34.06, -118.25], zoom_start=5)

    loc = [(40.720, -73.993),
           (40.721, -73.996)]
    folium.PolyLine(loc,
                    color='red',
                    weight=15,
                    opacity=0.8).add_to(m)

    m.save(SaveLocation())

#20
def DiplayFoliumDrawPlugin():
    m = folium.Map(location=[34.06, -118.25], zoom_start=5)
    draw = Draw(export=True)
    draw.add_to(m)
    m.save(SaveLocation())



if __name__ == '__main__':
    # DisplayWebMapTiles()
    # DisplayWebMapName()
    # DisplayGeolocation()
    # DisplayMapWithZoom()
    # DisplayGeoJSONLayer()
    # DisplayMarkerLayer()
    # DisplayMarkerWithIcon()
    # AdCircleMarker()
    # AddServeralMarker()
    # AddCircle()
    # AddRectagle()
    # AddPopups()
    # AddLayers()

    # AddPluginMiniMap()
    # AddPluginTerminator()
    # AddPluginGeocoder()
    # AddPluginsClusterMarker()
   # AddpluginHeatmap()
   # AddPolyLiner()
    DiplayFoliumDrawPlugin()