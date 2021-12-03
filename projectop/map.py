import pandas as pd
import geopandas
import folium

data = pd.read_csv (r"C:\Users\ronal\desktop\vaccinations.csv")

table = data['location']

print(table)

pd.set_option('display.max_columns', 14)
pd.set_option('display.width', 15)
pd.set_option('display.max_rows', 50000)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

table = world.merge(table, how='left', left_on=['name'], right_on=['location'])


the_map = folium.Map()

folium.Choropleth(
    geo_data=table,
    name='Folium Map',
    data=table,
    columns=['location', 'total_vaccinations'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Total vaccionations by Country'
).add_to(the_map)

the_map.save('test.html')
