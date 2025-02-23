import streamlit as st
import saved_photos
import ai_suggestion
import clothes_suggestion
import analyze

st.title("StyleFusion: Closet assistant")

# Create tabs for navigation
tab1, tab2, tab3, tab4 = st.tabs(["Your Closet", "Outfit Suggestions", "New Clothes Purchase", "Analyze"])

# Display content based on selected tab
with tab1:
    saved_photos.show_saved_photos()
with tab2:
    ai_suggestion.show_ai_suggestion()
with tab3:
    clothes_suggestion.show_clothes_suggestion()
with tab4:
    analyze.show_analyze()