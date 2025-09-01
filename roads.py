#!/usr/bin/env python3
# roads.py
# Solve ambulance VRP (1 ambulance, cap=3, 5 patients) on OSM roads.
# Usage:
#   python3 roads.py --json OptimizationProblemData.json

import argparse
import json
import math
import itertools as it
import sys
import networkx as nx
import osmnx as ox

# ----------------- Helpers -----------------
def rough_m_per_deg_lat(): return 111_320.0
def rough_m_per_deg_lon(lat): return 111_320.0 * math.cos(math.radians(lat))

def trip_cost(order, C):
    if not order: return 0.0
    total = C[0][order[0]]
    for a,b in zip(order, order[1:]):
        total += C[a][b]
    total += C[order[-1]][0]
    return total

def best_trip_for_set(S, C):
    best = (float("inf"), None)
    for perm in it.permutations(S):
        c = trip_cost(list(perm), C)
        if c < best[0]:
            best = (c, list(perm))
    return best

def build_graph(coords, margin_m):
    # compute bounding circle
    lats = [lat for lat, lon in coords]
    lons = [lon for lat, lon in coords]
    lat_c = sum(lats)/len(lats)
    lon_c = sum(lons)/len(lons)
    span_m = max(
        (max(lats)-min(lats))*rough_m_per_deg_lat(),
        (max(lons)-min(lons))*rough_m_per_deg_lon(lat_c)
    )
    dist_m = span_m/2 + margin_m
    if dist_m < 1500: dist_m = 1500

    print(f"→ Downloading OSM roads (radius ≈ {dist_m:.0f} m)")
    G = ox.graph_from_point((lat_c, lon_c), dist=dist_m, network_type="drive")

    # Force speeds to 80 km/h everywhere
    G = ox.add_edge_speeds(G, fallback=80)
    G = ox.add_edge_travel_times(G)

    # Keep only the largest strongly connected component (NetworkX version)
    largest_scc = max(nx.strongly_connected_components(G), key=len)
    G = G.subgraph(largest_scc).copy()

    return G

def build_cost_matrix(G, coords):
    node_ids = [ox.nearest_nodes(G, lon, lat) for lat,lon in coords]
    N = len(node_ids)
    dist_km = [[0.0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i==j: continue
            try:
                d_m = nx.shortest_path_length(G, node_ids[i], node_ids[j], weight="length")
                dist_km[i][j] = d_m/1000.0
            except nx.NetworkXNoPath:
                dist_km[i][j] = float("inf")
    return dist_km

def solve_classical(C, labels):
    P = [1,2,3,4,5]
    best = (float("inf"), None)
    for trip1 in it.combinations(P, 3):
        trip1 = tuple(sorted(trip1))
        trip2 = tuple(sorted(set(P)-set(trip1)))
        c1,o1 = best_trip_for_set(trip1,C)
        c2,o2 = best_trip_for_set(trip2,C)
        tot = c1+c2
        if tot < best[0]:
            best = (tot, ((o1,c1),(o2,c2)))
    total,( (o1,c1),(o2,c2) ) = best
    def fmt(order): return "H → " + " → ".join(labels[i] for i in order) + " → H"
    print("\n=== CLASSICAL OPTIMUM (distance km) ===")
    print(f"Trip 1: {fmt(o1)} | {c1:.2f} km")
    print(f"Trip 2: {fmt(o2)} | {c2:.2f} km")
    print(f"TOTAL = {total:.2f} km")

# ----------------- Main -----------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", required=True, help="Path to OptimizationProblemData.json")
    args = parser.parse_args()

    # load data
    data = json.load(open(args.json))
    H = data["locations"]["hospital"]["coordinates"]
    patients = data["locations"]["patients"]
    labels = ["H"]+[p["id"] for p in patients]
    coords = [(H["latitude"], H["longitude"])] + [
        (p["coordinates"]["latitude"], p["coordinates"]["longitude"]) for p in patients
    ]

    print("Loaded points:")
    for i,(lat,lon) in enumerate(coords):
        print(f" {i}: {labels[i]} lat={lat:.6f}, lon={lon:.6f}")

    # try different radii until graph works
    for margin in [3000,5000,8000,12000]:
        try:
            G = build_graph(coords, margin)
            C = build_cost_matrix(G, coords)
            if any(float("inf") in row for row in C):
                print(f"⚠️ Still unreachable with margin {margin}, trying bigger…")
                continue
            solve_classical(C, labels)
            break
        except Exception as e:
            print(f"⚠️ Failed with margin {margin}: {e}")
            continue
    else:
        print("❌ Could not build a connected graph even with large radius.")

if __name__=="__main__":
    main()
