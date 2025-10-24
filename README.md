# Python Games 

This repository contains three small Python projects:
- **Connect Four** — a classic game with a minimax AI.
- **Fast Finger** — a typing speed challenge in the terminal.
- **Geographic Distance Analysis** a toolkit for exploring distances between French towns and regions.

## Connect Four
A Python implementation of the classic *Connect Four* game, featuring:
- Minimax algorithm with alpha-beta pruning.
- Dynamic depth adjustment during the game.
- Play against the computer or watch two AIs compete.

---

## Fast Finger
A terminal-based typing speed game.  
Type random words as fast and accurately as possible!

**Main files:**
- `fastfinger.py` — game logic
- `input_space.py` — captures real-time keystrokes
- `words.txt` — French word list
- `nettoyage.py`, `tri_alpha.py` — utility scripts for word cleanup and sorting

---


## Notes
- The `keyboard` module may require administrator privileges on some systems.
- The games are designed for terminal use (no GUI).


---

### 3. **Geographic Distance Analysis (`distance.py`)**
A toolkit for exploring distances between French towns and regions using **Haversine’s formula** and **Folium** for map visualization.

#### Features
- Compute distance between two towns  
- Find all towns within a given radius  
- Find the *N* closest towns  
- Compare min/max distances between regions or departments  
- Automatically generates interactive HTML maps

#### Example
```python
# Example usage:
distance_comparative("Yvelines", "Doubs", "dep", min)
afficher_villes_dans_rayon("Chatou", 5)
create_map("La Celle-Saint-Cloud", 10)
```

The repository contains sample generated maps such as:
- `10 neighbors Chatou.html`
- `carte_villes_dans_rayon.html`
- `Vélizy-Villacoublay-Jallerange.html`

These can be opened directly in any web browser.

---
