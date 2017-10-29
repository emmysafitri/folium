import folium

m = folium.Map(
    location=[-0.94924 100.35427],
    zoom_start=10,
    )
    
 folium.Marker(
    location=[-0.819430, 100.304417],
    popup='Padang Sarai',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
    
folium.Marker(
    location=[-0.834507, 100.338057],
    popup='Batipuh Panjang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.933774, 100.408908],
    popup='Pisang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.909745, 100.371485],
    popup='Tabing Banda Gadang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.891316, 100.408590],
    popup='Gn. Sarik',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.855194, 100.358253],
    popup='Koto Panjang Ikua Koto',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.906418, 100.359485],
    popup='Kp. Lapai',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.923667, 100.377036],
    popup='Ampang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.943807, 100.374209],
    popup='Sawahan Tim.',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.939567, 100.447006],
    popup='Kapala Koto',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.8970898,100.3664311],
    popup='Pasar Nanggalo
Surau Gadang, Nanggalo, Kota Padang, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.9920046,100.3807497],
    popup='Pasar Gaung
Teluk Bayur, South Padang, Padang City, West Sumatra', 
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.7724924,100.6402682],
    popup='Solok,
    Kota Padang, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.7724924,100.6402682],
    popup='Danau Singkarak,
    X Koto Singkarak, Solok, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    location=[-0.7724924,100.6402682],
    popup='Puncak Gagoan, Muara Pingai
   Junjung Sirih, Solok, Sumatera Barat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
