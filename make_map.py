import folium
import xyzservices.providers as xyz

# Create a map centered on a location (San Francisco in this example)
m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

# Add a marker
folium.Marker(
    location=[37.7749, -122.4194],
    popup="Hello, Folium!",
    tooltip="Click me!",
    tiles='OpenStreetMap'
).add_to(m)

# Add different tile layers (Esri canvas tiles don't require an API key)
folium.TileLayer(xyz.Esri.WorldGrayCanvas, name='Light Mode').add_to(m)
folium.TileLayer(xyz.Esri.WorldGrayCanvas(variant='Canvas/World_Dark_Gray_Base'),
  name='Dark Mode').add_to(m)


# Save the map to an HTML file
m.save("map.html")
print("Map created successfully! Open map.html in your browser to view it.")
