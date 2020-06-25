# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:00:14 2019
code revision: added web browser viewing from within Spyder 9/5/19

@author: jg
"""


import pandas as pd
import folium
from docplex.mp.model import Model
from geopy.distance import great_circle



n = 15
packages = [i for i in range(1, n + 1)]
nodes = [0] + packages

arcs = [(i,j) for i in nodes for j in nodes if i != j]
geo_df = pd.read_csv('cvrp-anf-addresses.csv')


lats = geo_df['lat'].to_numpy()
lons = geo_df['lon'].to_numpy()
volume = geo_df['volumen'].to_numpy()
distance = {(i,j): great_circle((lats[i], lons[i]), (lats[j], lons[j])).meters for i, j in arcs}
weight = geo_df['peso'].to_numpy()
volume_max = 20
weight_max = 20

mdl = Model('CVRP Postal Service of Chile')

x = mdl.binary_var_dict(arcs, name='x')
u = mdl.continuous_var_dict(packages, name='u')
w = mdl.continuous_var_dict(packages, name='w')

mdl.minimize(mdl.sum(distance[(i, j)] * x[(i, j)] for i, j in arcs))

for h in packages:
    mdl.add_constraint(mdl.sum(x[(i,j)] for i,j in arcs if i==h)==1, ctname='out_%d'%h)

for h in packages:
    mdl.add_constraint(mdl.sum(x[(i,j)] for i,j in arcs if j==h)==1, ctname='in_%d'%h)
    

for i, j in arcs:
    if i!=0 and j!=0:
        mdl.add_indicator(x[(i,j)], u[i] + volume[j] == u[j])
        mdl.add_indicator(x[(i,j)], w[i] + weight[j] == w[j])
        
        
for i in packages:
    mdl.add_constraint(volume[i] <= u[i])
    mdl.add_constraint(u[i] <= volume_max)
    mdl.add_constraint(weight[i] <= w[i])
    mdl.add_constraint(w[i] <= weight_max)

mdl.parameters.timelimit = 60
mdl.parameters.mip.tolerances.mipgap = 0.1
mdl.parameters.mip.strategy.branch = 1
solucion = mdl.solve(log_output=True)

mdl.get_solve_status()

# Encontrar las rutas por separado
routes = []
for h in packages:
    if x[(0, h)].solution_value > 0.9:
        route_arches = [(0, h)]
        j = h
        while j!=0:
            i = j
            for k in nodes:
                if i!=k and x[(i, k)].solution_value > 0.9:
                    j = k
                    route_arches.append((i, j))
                    break
        routes.append(route_arches)
routes



map = folium.Map(location=[lats[0],lons[0]], zoom_start=12)
map.save('routingMap.html')
fg = folium.FeatureGroup(name='Directiones')

# Graficar el depot
fg.add_child(folium.Marker(location=[lats[0],lons[0]],
                           popup=folium.Popup('Depot'),
                           icon=folium.Icon(color='red', 
                                            icon_color='white')
                           ))

# Graficar los clientes

for index, row in geo_df.head().iterrows():   
    number = row['Nombre']
    lat    = row['lat']
    lon    = row['lon']
    fg.add_child(folium.Marker(location=[lat,lon],
                               popup=folium.Popup(number),
                               icon=folium.Icon(color='blue',
                                                icon_color='white')
                               ))

map.add_child(fg)

# Graficar las rutas por separado
k = 0
for route in routes:
    k = k + 1
    fg = folium.FeatureGroup(name='Route %d'%(k))
    for i, j in route:
        poly = folium.PolyLine(locations=[[lats[i],lons[i]],[lats[j],lons[j]]], weight=5)
        fg.add_child(poly)
    map.add_child(fg)

# Mostrar el mapa
map.add_child(folium.LayerControl())
map.save('routingMap.html')

# to display the html map in Chrome browser
import webbrowser
filepath = 'C:/Users/jg/Documents/SaintMaryCollege/Courses/OPS807/summer2019/PythonCodeOld/routingMap.html'
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
webCont = webbrowser.get('chrome')      #('chrome')
webCont.open('file://' + filepath, new = 1)