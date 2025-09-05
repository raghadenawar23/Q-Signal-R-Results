# Q-Signal-R-Results

**Team:** Q-Signal  
**Group:** R-Results  
**Event:** Alexandria Quantum Hackathon 2025

---

## 📝 Overview

This repository hosts the full pipeline for solving the **Emergency Patient Transportation Routing** hackathon challenge. It includes both classical and quantum approaches:

- **Classical Optimization**  
  - Exact brute-force (3+2 patient splits)  
  - Heuristic: split + nearest insertion + 2-opt  

- **Quantum Approach**  
  - QUBO formulation and mapping to the Ising model  
  - QAOA implementation using PennyLane with depth \(p = 1\) and \(p = 2\)  

 OpenRouteService (ORS) is utilized for accurate road-network distance calculations and coordinate snapping.

---

##  Project Structure
├── OptimizationProblemData.json # Input: hospital & patient coordinates
├── Day_1_Classical.ipynb # Initial classical solver experiments
├── Hackathon_Routing_FinalClassic_Unrefactored.ipynb # Final classical pipeline
├── Hackathon_Routing_FinalClassic_Unrefactored_QUBO1.ipynb # Extended with QUBO and QAOA
├── roads.py # ORS initialization & cost matrix builder
├── README.md 
└── cache


---

##  Getting Started

### Prerequisites

- Python 3.8+  
- Recommended packages:
  ```bash
  pip install openrouteservice folium pandas pennylane pennylane-lightning numpy

How to Run

Place your ORS API key in roads.py or export it via:

export ORS_API_KEY="YOUR_API_KEY"


Execute the classical pipeline:

jupyter notebook Day_1_Classical.ipynb


For the full classical and quantum pipeline, run:

jupyter notebook Hackathon_Routing_FinalClassic_Unrefactored_QUBO1.ipynb


For reproducibility, ORS-snapped visuals and cost matrices are included or can be generated from these notebooks.

Results

Exact & Heuristic both achieved the optimum total distance: 57.33 km (trip split as H → DT → GR → R3_2 → H, and H → IT → R2 → H).

QAOA (depth 
𝑝
=
1
,
2
p=1,2) converged close to optimal energies; sampled routes were near-optimal (approx. 58–61 km).

Visualizations (to be added as figures) include:

Workflow diagram

Cost matrix heatmap

Exact vs. heuristic route overlays

QAOA convergence plots

Acknowledgments

Thanks to the organizers of the Alexandria Quantum Hackathon 2025.
Team Q-Signal, Group R-Results:
Abdelrahman Gabr, Menna Zaeid, Mohamed Adel, Omar Romman, Raghade Nawar

License

Distributed under MIT License.
See LICENSE
 for details (add if needed).

Contact

For questions or collaboration, contact:
Raghade Nawar – [GitHub profile]


---

### Why this structure works:
- **Clear overview**: immediately shows what the project is about.
- **Detailed project structure**: helps collaborators locate files quickly.
- **Running instructions**: makes it easy to reproduce work.
- **Results summary**: gives immediate insights into outcomes.
- **Acknowledgments and contact**: adds a professional touch.

Let me know if you'd like any tweaks or additions, like embedded badges, GIFs, or installation status!
::contentReference[oaicite:0]{index=0}


