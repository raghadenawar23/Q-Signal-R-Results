<img width="538" height="97" alt="image" src="https://github.com/user-attachments/assets/69728074-ae78-469d-9ce0-f7e2ad2cbf71" />

<img width="1563" height="1250" alt="quantum_sphere_brp (1)" src="https://github.com/user-attachments/assets/0c531e73-484d-4e90-b2a8-d72a60e2d517" />


# Quantum and Classical Approaches to Emergency: Patient Transportation Routing

**Team:** RaceQ
**Event:** Alexandria Quantum Hackathon 2025  

---

## 📝 Overview

This project solves an **Emergency Patient Transportation Routing** challenge using both **classical** and **quantum** optimization techniques.

- **Classical Methods**  
  - Exact brute-force (3+2 split of patients)  
  - Heuristic: split → nearest insertion → 2-opt  

- **Quantum Methods**  
  - QUBO formulation → Ising model  
  - QAOA implementation with PennyLane (depth p=1,2)  

Distances are computed with **OpenRouteService (ORS)** for realistic road-network values.

---

## 📂 Project Structure

.
├── OptimizationProblemData.json # Input: hospital & patient coordinates
├── oeny_!.ipynb # Notebook: full pipeline (classical + quantum)
├── LICENSE # MIT License
├── README.md # Project documentation
└── cache/ # Local artifacts 

---

## ⚙️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/raghadenawar23/Q-Signal-R-Results.git
   cd Q-Signal-R-Results

   
Install requirements:

   pip install -r requirements.txt

Set your ORS API key:

export ORS_API_KEY="YOUR_KEY_HERE"   # Linux/macOS
setx ORS_API_KEY "YOUR_KEY_HERE"     # Windows PowerShell

🚀 How to Run
Open the notebook:

jupyter notebook oeny_!.ipynb
The notebook will:

Load coordinates from OptimizationProblemData.json

Build the ORS cost matrix

Run exact brute force and heuristic solvers

Run QAOA with PennyLane

Show results and visualizations

📊 Results
Exact (3+2 split)

Trip 1: H → DT → GR → R3_2 → H ≈ 28.70 km

Trip 2: H → IT → R2 → H ≈ 28.63 km

Total: 57.33 km

Heuristic

Same total: 57.33 km

QAOA (p=1,2)

Near-optimal routes: ~58–61 km

🧰 Tools & Libraries
Python 3.8+

OpenRouteService (openrouteservice)

Folium (map visualization)

NumPy, Pandas

PennyLane + PennyLane-Lightning

👥 Authors
Team RaceQ:
Abdelrahman Gabr
Menna Zaeid
Mohamed Adel
Omar Romman
Raghade Nawar
Paper : https://drive.google.com/file/d/18QuuAvdQeUdop6-0TtG4DWXal6F6G5Ng/view?usp=sharing


https://drive.google.com/file/d/18QuuAvdQeUdop6-0TtG4DWXal6F6G5Ng/view?usp=sharing
