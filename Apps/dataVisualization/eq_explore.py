from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('earthquake_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
# path = Path('earthquake_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, longs, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    long = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    longs.append(long)
    lats.append(lat)
    eq_titles.append(eq_title)

# print(mags[:10])
# print(longs[:5])
# print(lats[:5])

title = 'Global Earthquakes'
# color= (what values to use for the coloring.)
# color_continuous_scale= (which color scale to use)
# labels: color= what to label the color scale, default is 'Color'
# projection=  which map to use.
# hover= what to use for the hover title
fig = px.scatter_geo(lat=lats, lon=longs, size=mags, title=title,
                     color=mags, color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,)
fig.show()