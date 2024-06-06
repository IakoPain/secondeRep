import folium

macarte = folium.Map(location=[47.988992, 0.253102])
folium.Marker([47.9884, 0.2526], popup="Départ/Arrivée B0", icon=folium.Icon(color='red')).add_to(macarte)
folium.Marker([47.9891, 0.2519], popup="B1").add_to(macarte)
folium.Marker([47.9903, 0.2526], popup="B2").add_to(macarte)
folium.Marker([47.9911, 0.2537], popup="B3").add_to(macarte)
folium.Marker([47.9911, 0.2548], popup="B4").add_to(macarte)
folium.Marker([47.9914, 0.2563], popup="B5").add_to(macarte)
folium.Marker([47.9909, 0.2576], popup="B6").add_to(macarte)
folium.Marker([47.9899, 0.2586], popup="B7").add_to(macarte)
folium.Marker([47.9890, 0.2565], popup="B8").add_to(macarte)
folium.Marker([47.9897, 0.2548], popup="B9").add_to(macarte)
folium.Marker([47.9886, 0.2542], popup="B10").add_to(macarte)
folium.Marker([47.9878, 0.2534], popup="B11").add_to(macarte)
points = [
    (47.9884, 0.2526),
    (47.9891, 0.2519),
    (47.9903, 0.2526),
    (47.9911, 0.2537),
    (47.9911, 0.2548),
    (47.9914, 0.2563),
    (47.9909, 0.2576),
    (47.9899, 0.2586),
    (47.9890, 0.2565),
    (47.9897, 0.2548),
    (47.9886, 0.2542),
    (47.9878, 0.2534),
    (47.9884, 0.2526)
]

folium.PolyLine(points, color="blue", weight=2.5, opacity=0.8).add_to(macarte)
macarte.save("cartecource.html")