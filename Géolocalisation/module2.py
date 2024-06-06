import folium

macarte = folium.Map(location=[42.838019, -0.14027])
folium.Marker([42.85089, -0.139836], popup="Départ", icon=folium.Icon(color='green')).add_to(macarte)
folium.Marker([42.842588, -0.140455], popup="Pause déjeuner").add_to(macarte)
folium.Marker([42.83491, -0.140502], popup="Pause déjeuner").add_to(macarte)
folium.Marker([42.828154, -0.139286], popup="Pause les pieds dans l’eau").add_to(macarte)
folium.Marker([42.823732, -0.13782], popup="Arrivée", icon=folium.Icon(color='red')).add_to(macarte)
macarte.save("carterando.html")