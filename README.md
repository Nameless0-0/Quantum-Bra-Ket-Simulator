# Quantum Bra-Ket Simulator

## Overview

The Quantum Bra-Ket Simulator is a web-based application built with Streamlit that allows users to explore quantum states and simulate observations based on user-defined parameters. Users can select predefined quantum states or input their own custom states, and the app will simulate the observation of these states.

## Features

- **Select from predefined quantum states**: 
  - |0⟩
  - |1⟩
  - |+⟩
  - |−⟩
  
- **Custom state input**: 
  - Users can define their own quantum state in the form |ψ⟩ = α|0⟩ + β|1⟩ by adjusting the real and imaginary parts of α and β.
  
- **Observation simulation**: 
  - The app simulates the observation of the selected or custom quantum state and displays the result.

## Requirements

To run this application, you need to have the following Python packages installed:

- `streamlit`
- `numpy`

You can install these packages using pip:

```bash
pip install streamlit numpy
```
## Getting Started

- **1. Clone the repository**
```bash
git clone <repository-url>
cd <repository-directory>
```

- **2. Run the Application: Execute the following command in your terminal:**
```bash
streamlit run main.py
```
- **3. Open your web browser.**
After running the command, a new tab will open in your web browser displaying the Quantum Bra-Ket Simulator.

## Usage Instructions

1. **Select a Quantum State**:
   - From the dropdown menu, choose one of the predefined quantum states: |0⟩, |1⟩, |+⟩, or |−⟩. Alternatively, select "Custom" to define your own quantum state.

2. **Custom State Input** (if "Custom" is selected):
   - Adjust the sliders for the real part (Re(α)) and imaginary part (Im(α)) of α. 
   - Choose to set either the real part or the imaginary part of β:
     - If you select "Set Re(β)", adjust the slider for Re(β).
     - If you select "Set Im(β)", adjust the slider for Im(β).
   - The app will automatically calculate the corresponding part to ensure that the normalization condition (|α|² + |β|² = 1) is satisfied.

3. **Simulate Observation**:
   - Click the "Observe State" button to simulate the observation of the selected or custom quantum state. The result will be displayed below the button, indicating the outcome of the measurement (either |0⟩ or |1⟩).


