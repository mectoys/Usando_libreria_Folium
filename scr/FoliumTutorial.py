import os.path
import random
import folium

#1
def SaveLocation():
    dirname = os.path.dirname(__file__)
    dir = r"Mapas\foliumtutorial.html"
    savelocation = os.path.join(dirname, dir)
    return savelocation

#2
def DisplayWebMapTiles():
    m = folium.Map()
    m.save(SaveLocation())

#3
def DisplayWebMapName():
    number = random.randint(0, 3)
    Name_Tiles = ["Stamen Terrain", "Stamen Toner", "cartodb positron", "OpenStreetMap"]
    m = folium.Map(tiles="Stamen Terrain")
    m.save(SaveLocation())
#4
#latitud y longitud
def DisplayGeolocation():
    m = folium.Map(location=(49.25, -123.12), tiles="cartodb positron")
    m.save(SaveLocation())
#5
#Zoom
def DisplayMapWithZoom():
    m = folium.Map(location=(30,10),zoom_start=5, tiles="cartodb positron")
    m.save(SaveLocation())
#6
#GoeJsonLayer
def DisplayGeoJSONLayer():
    political_countries_url = (
        "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
    )
    m = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron")

    folium.GeoJson(political_countries_url).add_to(m)
    m.save(SaveLocation())
#7
#marcadores
def DisplayMarkerLayer():
    m = folium.Map(location=(100, 10), zoom_start=2, tiles="cartodb positron")
    folium.Marker(location=[34.06,-118.25]).add_to(m)
    m.save(SaveLocation())
#8
#Marcador con Icono
def DisplayMarkerWithIcon():
    #https://fontawesome.com/v4/icon/bandcamp
    m = folium.Map(location=(34.06, -110.25), zoom_start=8, tiles="cartodb positron")
    folium.Marker(location=[34.06, -118.25],icon=folium.Icon(icon="podcast",prefix='fa',color="red")).add_to(m)

    m.save(SaveLocation())
#9
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

if __name__ == '__main__':
    # DisplayWebMapTiles()
    # DisplayWebMapName()
    #DisplayGeolocation()
    #DisplayMapWithZoom()
    #DisplayGeoJSONLayer()
    #DisplayMarkerLayer()
    #DisplayMarkerWithIcon()
    AdCircleMarker()
