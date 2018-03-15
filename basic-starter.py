# Cell 1
import arcgis
from arcgis.gis import GIS
from IPython.display import display

# Cell 2
gis = GIS("https://ral.maps.arcgis.com", client_id='9VUcLzqiGGv4M1HS') # Use your own client ID
print("Successfully logged in as: " + gis.properties.user.username)
