import folium
import webbrowser

macarte = folium.Map(location=[47.46043, -0.530806], zoom_start=20)
folium.Marker([47.467346, -0.524154], popup="Espace Anjou").add_to(macarte)
macarte.save("carte3.html")
webbrowser.open ("carte3.html")