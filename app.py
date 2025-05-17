import streamlit as st
import saved_photos
import ai_suggestion
import clothes_suggestion
import analyze

# Custom CSS: make content full width, not centered, and enlarge/bold tab font
st.markdown(
    """
    <style>
    .block-container {
        max-width: 100vw !important;
        padding-left: 2vw;
        padding-right: 2vw;
    }
    /* Enlarge and bold tab font */
    .stTabs [data-baseweb="tab"] {
        font-size: 1.25rem;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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