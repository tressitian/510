import streamlit as st

def show_clothes_suggestion():
    st.header("New Clothes Suggestions")
    
    # Display multiple clothing suggestions
    for i in range(3):  # Show 3 outfit suggestions
        with st.container():
            st.subheader(f"Outfit Suggestion {i+1}")
            
            # Create columns for better layout
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Placeholder for clothing image
                st.image("https://placeholder.com/300x400", caption="Outfit Image")
            
            with col2:
                # Clothing details
                st.markdown("### Item Details")
                st.write("**Brand:** [Brand Name]")
                st.write("**Price:** $XX.XX")
                st.write("**Recommended Size:** M")
                st.write("**Style:** Casual/Formal")
                st.write("**Color:** Navy Blue")
                
                # Product link
                st.markdown("[🛍️ Shop Now](https://example.com)")
                
                # Recommendation reason
                st.markdown("### Why we recommend this")
                st.write("Based on your style preferences and previous choices, " 
                        "this outfit matches your preferred color palette and fit.")
            
            st.divider()  # Add a visual separator between outfits


