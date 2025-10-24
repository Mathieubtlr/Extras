from math import radians, sin, cos, sqrt, atan2
import csv 
import numpy as np
import folium
import webbrowser
import unicodedata

csv_file = "communes.csv"  

data = {}

# Load the CSV file
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)  
    next(reader)
    for row in reader:
        data[row[2]] = []
        data[row[2]].append(float(row[0]))
        data[row[2]].append(float(row[1]))
        data[row[2]].append(row[3])
        data[row[2]].append(row[4])

# Haversine formula
def haversine(A, B):
    R = 6371  # Average radius of the Earth in km
    A_lat, A_long = map(radians, A)
    B_lat, B_long = map(radians, B)
    
    delta_lat = B_lat - A_lat
    delta_long = B_long - A_long

    a = sin(delta_lat / 2)**2 + cos(A_lat) * cos(B_lat) * sin(delta_long / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c  # Distance in kilometers


def distance(town_A, town_B):  # towns are strings
    A = (data[town_A][0], data[town_A][1])
    B = (data[town_B][0], data[town_B][1])
    return haversine(A, B)


def distance_radius(town, radius):  # returns all nearby towns within a given radius
    neighbors = []
    for x in data:
        if distance(town, x) <= radius and town != x:
            neighbors.append(x)
    return neighbors


def n_neighbors(town, N):  # find the N nearest towns
    distances = []

    for x in data:
        if town != x: 
            dist = distance(town, x)
            distances.append((x, dist))  

    distances.sort(key=lambda x: x[1])
    return [(x[0], round(x[1], 2)) for x in distances[:N]]


def show_route(town1, town2):
    lat1, lon1 = data[town1][:2]
    lat2, lon2 = data[town2][:2]

    # Create the map centered between the two towns
    center_lat = (lat1 + lat2) / 2
    center_lon = (lon1 + lon2) / 2
    m = folium.Map(location=[center_lat, center_lon], zoom_start=7)

    # Add markers
    folium.Marker([lat1, lon1], popup=town1, icon=folium.Icon(color="blue")).add_to(m)
    folium.Marker([lat2, lon2], popup=town2, icon=folium.Icon(color="red")).add_to(m)

    # Draw the route between towns
    folium.PolyLine([(lat1, lon1), (lat2, lon2)], color="blue", weight=2.5, opacity=1).add_to(m)
    
    filename = f"{town1}-{town2}.html"
    m.save(filename)
    webbrowser.open(filename)
    return


### __________________________________________________ ###
### Function 1 of 8
# min/max distance within the same department/region
# min/max distance between two departments/regions

def comparative_distance(name1, name2, dep_reg, min_max):  # dep_reg = "dep" or "reg", min_max = min or max
    if dep_reg == "dep":
        index = 2
    elif dep_reg == "reg":
        index = 3

    towns1 = [x for x in data if data[x][index] == name1]
    towns2 = [y for y in data if data[y][index] == name2]

    if not towns1 or not towns2:
        return None, "No town found in one of the regions"

    min_max_dist, min_max_pair = min_max(
        ((distance(x, y), (x, y)) for x in towns1 for y in towns2 if x != y),
        key=lambda t: t[0]
    )

    town1, town2 = min_max_pair
    show_route(town1, town2)

    return round(min_max_dist, 2), min_max_pair


def show_towns_within_radius(town, radius):
    # Get coordinates of the origin town
    lat_town, lon_town = data[town][:2]
    
    # Create a map centered on the origin town
    m = folium.Map(location=[lat_town, lon_town], zoom_start=10)

    # Add marker for origin
    folium.Marker([lat_town, lon_town], popup=town, icon=folium.Icon(color="blue")).add_to(m)

    # Draw circle representing radius
    folium.Circle(
        location=[lat_town, lon_town],
        radius=radius * 1000,  # Convert km to meters
        color="blue",
        fill=True,
        fill_opacity=0.2
    ).add_to(m)

    # Get nearby towns
    nearby_towns = distance_radius(town, radius)
    print(distance_radius(town, radius))

    # Add markers for nearby towns
    for town_name in nearby_towns:
        lat_v, lon_v = data[town_name][:2]
        folium.Marker([lat_v, lon_v], popup=town_name, icon=folium.Icon(color="red")).add_to(m)

    filename = "towns_within_radius.html"
    m.save(filename)
    webbrowser.open(filename)
    return


def create_map(town, N):
    town_location = data[town][:2]
    town_map = folium.Map(location=town_location, zoom_start=6)
    folium.Marker(town_location, popup=f"{town} (Origin)", icon=folium.Icon(color='red')).add_to(town_map)
    
    neighbors = n_neighbors(town, N)
    print(n_neighbors(town, N))
    for neighbor, dist in neighbors:
        loc = data[neighbor][:2]
        folium.Marker(loc, popup=f"{neighbor}: {dist} km", icon=folium.Icon(color='blue')).add_to(town_map)
        folium.PolyLine([town_location, loc], color='blue', weight=2.5, opacity=0.8).add_to(town_map)
    
    filename = f"{N} neighbors {town}.html"
    town_map.save(filename)
    webbrowser.open(filename)
    return


def show_regions():
    regions = set(data[town][3] for town in data)
    for region in sorted(regions):
        print(region)


def show_departments():
    departments = set(data[town][2] for town in data)
    for dep in sorted(departments):
        print(dep)


def show_towns():
    towns = set(data)
    for town in sorted(towns):
        print(town)


def show_departments_in_region(region):
    departments = set(data[town][2] for town in data if data[town][3] == region)
    for dep in sorted(departments):
        print(dep)


def show_towns_in_department(department):
    towns = {town for town in data if data[town][2] == department}
    for t in sorted(towns):
        print(t)


### Targeted search — returns towns if the pattern appears ###

# Function to remove accents
def remove_accents(text):
    """Remove accents and normalize text."""
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')


def targeted_search(pattern):
    normalized_pattern = remove_accents(pattern.lower())
    towns = {town for town in data if normalized_pattern in remove_accents(town.lower())}
    for town in sorted(towns):
        print(town)
