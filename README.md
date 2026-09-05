# Hybrid Helical-Capsule Microrobot for Targeted Renal Drug Delivery

A SolidWorks-designed microrobot concept developed to explore **magnetically guided, localized drug delivery for renal cell carcinoma applications**. The system integrates magnetic steering, helical propulsion, internal drug storage, and pH-responsive release within a compact hybrid architecture.

A Python navigation model complements the CAD design by simulating microrobot trajectories toward a target region and evaluating navigation performance through path and distance-to-target analysis.

---

## Microrobot Design

The microrobot uses a **hybrid helical-capsule architecture** that combines magnetic guidance, propulsion, payload storage, and controlled release within a single assembly.

| Component | Function |
|---|---|
| **Magnetic Head** | Provides the magnetically responsive region used for external guidance and directional control |
| **Helical Tail** | Supports rotational propulsion and forward translation through a fluid environment |
| **Outer Capsule** | Houses the drug-loaded core while incorporating openings for localized payload release |
| **Drug-Loaded Core** | Stores the therapeutic payload within the microrobot |
| **pH-Responsive Release Ports** | Enable stimulus-responsive release of the payload near the intended treatment region |

---

## CAD Development

The microrobot was modeled in **SolidWorks** as a multi-component assembly, with the geometry developed to integrate propulsion, magnetic guidance, payload storage, and release functionality within a compact design.

### Full Assembly

![Microrobot Assembly](images/microrobot-assembly.png)

### Exploded Assembly

![Exploded Microrobot](images/microrobot-exploded.png)

### Engineering Drawing

![Microrobot Drawing](images/microrobot-drawing.png)

---

## Navigation Simulation

A Python simulation was developed to evaluate the microrobot's ability to navigate from an initial position toward a defined target region.

The simulation:

- Calculates the direction of the target relative to the microrobot at each step
- Updates the microrobot's trajectory using controlled incremental movement
- Introduces positional disturbance to represent simplified navigation uncertainty
- Tracks the robot's position throughout the trajectory
- Measures the remaining distance to the target at every iteration
- Terminates once the microrobot reaches the target region

The model provides an initial framework for evaluating **trajectory convergence and navigation behavior** before introducing more advanced magnetic and fluid-dynamic effects.

---

## Simulation Results

### Navigation Trajectory

The trajectory plot visualizes the microrobot's movement from its initial position toward the target under simulated navigation disturbances.

![Microrobot Navigation Path](images/microrobot-path.png)

### Distance-to-Target Analysis

Distance-to-target analysis tracks navigation progress over time and provides a quantitative measure of convergence toward the target region.

![Distance to Target](images/distance-to-target.png)

---

## Engineering Scope

This project currently focuses on two linked areas:

**Mechanical Design**  
Development of a hybrid microrobot architecture integrating magnetic guidance, helical propulsion, drug storage, and pH-responsive release.

**Computational Navigation**  
Development of a Python-based model for simulating microrobot trajectories and evaluating movement toward a target region.

---

## Current Limitations

The current Python model is a simplified navigation simulation and does not yet explicitly solve the underlying magnetic or fluid mechanics.

Future iterations could incorporate:

- Magnetic force and torque
- Rotating magnetic-field control
- Fluid drag and background flow
- Renal vascular flow conditions
- 3D navigation
- Vessel geometry
- pH-triggered drug-release dynamics
- Repeated-trial navigation performance analysis

---

## Tools

- **SolidWorks** — component modelling, assembly design, and engineering drawings
- **Python** — navigation modelling and trajectory analysis
- **Matplotlib** — path and distance-to-target visualization
- **GitHub** — version control and project documentation
