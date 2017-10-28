import folium

m = folium.Map(
    location=[-0.94924 100.35427],
    zoom_start=10,
    )

folium.Marker(
    location=[-0.8970898,100.3664311],
    popup='Pasar Nanggalo
Surau Gadang, Nanggalo, Kota Padang, Sumatera Baratff',
    icon=folium.Icon(icon='info-sign')
).add_to(m)


