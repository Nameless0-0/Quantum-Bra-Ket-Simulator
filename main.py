import streamlit as st
import numpy as np

# Function to simulate observation
def observe_state(state_vector):
    probabilities = np.abs(state_vector) ** 2
    return np.random.choice(len(state_vector), p=probabilities)

# Define the quantum states
states = {
    '|0⟩': np.array([1, 0]),
    '|1⟩': np.array([0, 1]),
    '|+⟩': np.array([1/np.sqrt(2), 1/np.sqrt(2)]),
    '|−⟩': np.array([1/np.sqrt(2), -1/np.sqrt(2)]),
}

# Streamlit app
st.title('Quantum Bra-Ket Simulator')

# User selects a quantum state
selected_state = st.selectbox('Select a quantum state:', list(states.keys()))

# Display the selected state
st.write(f'Selected state: {selected_state}')

# Button to observe the state
if st.button('Observe State'):
    state_vector = states[selected_state]
    result_index = observe_state(state_vector)
    result_state = list(states.keys())[result_index]
    st.write(f'Observation result: {result_state}')