# Import google_streetview for the api module
import google_streetview.api
long =
lat = 
coord = str(long) + "," + str(lat)
# Define parameters for street view api
params = [{
  'size': '600x300', # max 640x640 pixels
  #'location': '42.3577,-71.0693',
  'location': coord,
  'heading': '151.78',
  'pitch': '-0.76',
  'year': '2014',
  'key': 'INSERT_API_KEY'
}]

# Create a results object
results = google_streetview.api.results(params)

# Download images to directory 'downloads'
results.download_links('downloadsmap')
