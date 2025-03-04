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
selected_state = st.selectbox('Select a quantum state:', list(states.keys()) + ['Custom'])

# Display the selected state
st.write(f'Selected state: {selected_state}')

# Custom state input
if selected_state == 'Custom':
    st.write("Set your own α for the state |ψ⟩ = α|0⟩ + β|1⟩:")
    alpha_real = st.slider('Re(α)', -1.0, 1.0, 1.0, 0.01)
    alpha_imag = st.slider('Im(α)', -1.0, 1.0, 0.0, 0.01)

    # Combine real and imaginary parts to form α
    alpha = alpha_real + 1j * alpha_imag

    # Calculate |α|^2
    alpha_magnitude_squared = np.abs(alpha) ** 2

    # Ensure |α|^2 ≤ 1
    if alpha_magnitude_squared > 1:
        st.error("Invalid input: |α|^2 must be ≤ 1. Please adjust α.")
    else:
        # Choose to set either the real part or the imaginary part of β
        beta_choice = st.radio("Modify:", ["Set Re(β)", "Set Im(β)"])

        if beta_choice == "Set Re(β)":
            beta_real = st.slider('Re(β)', -1.0, 1.0, 1.0, 0.01)
            beta_magnitude_squared = 1 - alpha_magnitude_squared - beta_real**2
            
            # Calculate the imaginary part of β
            if beta_magnitude_squared >= 0:
                beta_imag = np.sqrt(beta_magnitude_squared)
            else:
                beta_imag = 0.0  # If invalid, set to zero
                st.error("Invalid β input. Adjust Re(β) or α.")

        else:  # Set Im(β)
            beta_imag = st.slider('Im(β)', -1.0, 1.0, 0.0, 0.01)
            beta_magnitude_squared = 1 - alpha_magnitude_squared - beta_imag**2
            
            # Calculate the real part of β
            if beta_magnitude_squared >= 0:
                beta_real = np.sqrt(beta_magnitude_squared)
            else:
                beta_real = 0.0  # If invalid, set to zero
                st.error("Invalid β input. Adjust Im(β) or α.")

        # Create the custom state vector
        custom_state = np.array([alpha, beta_real + 1j * beta_imag])

        # Display the custom state vector
        st.write("Custom state vector:")
        st.write(custom_state)

# Button to observe the state
if st.button('Observe State'):
    if selected_state == 'Custom':
        if 'custom_state' in locals():
            state_vector = custom_state
            result_index = observe_state(state_vector)
            result_state = "|0⟩" if result_index == 0 else "|1⟩"
            st.write(f'Observation result: {result_state} (from custom state)')
        else:
            st.error("Please provide valid α values.")
    else:
        state_vector = states[selected_state]
        result_index = observe_state(state_vector)
        st.write(f'Observation result: {list(states.keys())[result_index]}')