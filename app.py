import streamlit as st
import saved_photos
import ai_suggestion
import clothes_suggestion
import analyze

# Set up the app title
st.title("Webcam Photo Capture App")

# Navigation logic
page = st.session_state.get("page", "Saved Photos")

if st.button("Saved Photos"):
    page = "Saved Photos"
    st.session_state.page = page
elif st.button("AI Suggestion"):
    page = "AI Suggestion"
    st.session_state.page = page
elif st.button("Clothes Suggestion"):
    page = "Clothes Suggestion"
    st.session_state.page = page
elif st.button("Analyze"):
    page = "Analyze"
    st.session_state.page = page

# Display the selected page
if page == "Saved Photos":
    saved_photos.show_saved_photos()  # Call the function from saved_photos.py
elif page == "AI Suggestion":
    ai_suggestion.show_ai_suggestion()  # Call the function from ai_suggestion.py
elif page == "Clothes Suggestion":
    clothes_suggestion.show_clothes_suggestion()  # Call the function from clothes_suggestion.py
elif page == "Analyze":
    analyze.show_analyze()  # Call the function from analyze.py
