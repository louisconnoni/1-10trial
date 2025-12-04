
import random
import streamlit as st

st.set_page_config(page_title="Guess the Number (1–10)", page_icon="🎲")

st.title("🎲 Guess the Number (1–10)")

# Initialize the secret number in session_state so it persists across interactions
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)

# Optional: show instructions for beginners
with st.expander("How to play"):
    st.write("""
    I picked a secret number between **1 and 10**.
    Enter your guess below and click **Submit guess**.
    If you're right, you'll see **Correct!**.
    If you're wrong, you'll see **Incorrect** and the correct number.
    Use **New number** to pick a new secret number and play again.
    """)

# Guess input
guess = st.number_input(
    label="Enter your guess:",
    min_value=1,
    max_value=10,
    step=1,
    format="%d",
)

# Buttons
col1, col2 = st.columns(2)
with col1:
    submit = st.button("Submit guess", type="primary")
with col2:
    new_number = st.button("New number 🔄")

# Handle new number generation
if new_number:
    st.session_state.secret_number = random.randint(1, 10)
    st.success("New number picked! Try guessing again.")

# Handle guess submission
if submit:
    secret = st.session_state.secret_number
    if guess == secret:
        st.success(f"✅ Correct! The number was **{secret}**.")
