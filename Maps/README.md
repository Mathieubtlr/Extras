# Distance Analysis Between French Communes

This project allows you to **analyze distances between French towns** using their geographic coordinates.  
It includes tools to compute distances, visualize relationships on interactive maps, and explore administrative regions.
Written in **Python 3** for geographic data exploration and visualization.

---

## Features

- Compute distance between **two towns** using the **Haversine formula**  
- Find **all towns within a given radius**  
- Get the **N nearest towns** to a specific location  
- Generate **interactive HTML maps** with Folium  
- Compare **minimum or maximum distance** between two departments or regions  
- Perform **pattern-based searches** for towns (case-insensitive, accent-tolerant)  
- Remove columns or clean datasets with utility scripts  

---

## How It Works

### Data Source
The program reads from a CSV file named `communes.csv`, which contains:

| Column | Description |
|--------|--------------|
| latitude | Latitude of the commune |
| longitude | Longitude of the commune |
| commune_name | Name of the town |
| department_name | French department |
| region_name | French region |

Example structure:

```csv
latitude,longitude,commune_name,department_name,region_name
48.8566,2.3522,Paris,Paris,Île-de-France
47.2378,6.0241,Besançon,Doubs,Bourgogne-Franche-Comté
```

---

## Main Functions

### `haversine(A, B)`
Calculates the great-circle distance between two geographic points in **kilometers**.

### `distance(town_A, town_B)`
Returns the distance between two towns (string names).

### `distance_radius(town, radius)`
Returns all towns within a given radius (in km) around a specified town.

### `n_neighbors(town, N)`
Finds the **N closest neighboring towns**.

### `comparative_distance(name1, name2, dep_reg, min_max)`
Finds either the **minimum or maximum distance** between:
- two departments (`dep_reg="dep"`)  
- or two regions (`dep_reg="reg"`)

Example:
```python
comparative_distance("Yvelines", "Doubs", "dep", min)
```

### `create_map(town, N)`
Generates an **interactive map** showing the N nearest towns to the given town.

### `show_towns_within_radius(town, radius)`
Creates a **map with a circle** centered on the town, displaying all nearby communes within the radius.

### `targeted_search(pattern)`
Performs a **text-based search** (accent- and case-insensitive) across all commune names.

---

## Example Outputs

The program generates **HTML files** that can be opened in any browser, such as:
- `10 neighbors Chatou.html`
- `carte_villes_dans_rayon.html`
- `Vélizy-Villacoublay-Jallerange.html`

Each file displays interactive maps with markers and routes between communes.

---

## Utilities

### `remove_column.py`
Removes a column (e.g. `code_region`) from a CSV file and saves a cleaned copy:
```python
column_to_remove = "code_region"
```
Creates:
```
communes_modifie9.csv
```

---

## Requirements

```
numpy
folium
csv
webbrowser
```

Install dependencies:
```bash
pip install numpy folium
```

---

## Run Examples

```bash
python distance.py
```

Inside Python:
```python
create_map("La Celle-Saint-Cloud", 10)
show_towns_within_radius("Chatou", 5)
comparative_distance("Yvelines", "Doubs", "dep", min)
```

---

## Data Notes

- The main dataset `communes.csv` contains all French communes with geographic and administrative data.  
- The project supports large datasets (tens of thousands of communes).



