# import streamlit as st

# def show_clothes_suggestion():
#     st.header("New Clothes Suggestions")
    
#     # Display multiple clothing suggestions
#     for i in range(3):  # Show 3 outfit suggestions
#         with st.container():
#             st.subheader(f"Outfit Suggestion {i+1}")
            
#             # Create columns for better layout
#             col1, col2 = st.columns([1, 2])
            
#             with col1:
#                 # Placeholder for clothing image
#                 st.image("https://placeholder.com/300x400", caption="Outfit Image")
            
#             with col2:
#                 # Clothing details
#                 st.markdown("### Item Details")
#                 st.write("**Brand:** [Brand Name]")
#                 st.write("**Price:** $XX.XX")
#                 st.write("**Recommended Size:** M")
#                 st.write("**Style:** Casual/Formal")
#                 st.write("**Color:** Navy Blue")
                
#                 # Product link
#                 st.markdown("[🛍️ Shop Now](https://example.com)")
                
#                 # Recommendation reason
#                 st.markdown("### Why we recommend this")
#                 st.write("Based on your style preferences and previous choices, " 
#                         "this outfit matches your preferred color palette and fit.")
            
#             st.divider()  # Add a visual separator between outfits


import streamlit as st

def show_clothes_suggestion():
    st.header("New Clothes Suggestions")
    
    # We have two sets of details to showcase:
    # 1) Porsche Jacket
    # 2) Supreme Jeans
    
    # We'll display 2 outfit suggestions (instead of 3)
    outfits = [
        {
            "image_url": "https://placeholder.com/300x400",
            "brand": "Porsche",
            "price": "$2,190",
            "recommended_size": "L",
            "style": "",  # User provided "Style:" with no specific descriptor
            "color": "Black and Yellow",
            "shop_link": "https://stockx.com/aime-leon-dore-x-porsche-993-turbo-leather-club-jacket-british-racing-green"
        },
        {
            "image_url": "https://placeholder.com/300x400",
            "brand": "Supreme",
            "price": "$210",
            "recommended_size": "L",
            "style": "Casual Jeans",
            "color": "Blue",
            "shop_link": "https://stockx.com/supreme-regular-jean-ss25-newspaper"
        }
    ]
    
    for i, outfit in enumerate(outfits, start=1):
        with st.container():
            st.subheader(f"Outfit Suggestion {i}")
            
            # Create columns for better layout
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Display the outfit image
                st.image(outfit["image_url"], caption="Outfit Image")
            
            with col2:
                # Clothing details
                st.markdown("### Item Details")
                st.write(f"**Brand:** {outfit['brand']}")
                st.write(f"**Price:** {outfit['price']}")
                st.write(f"**Recommended Size:** {outfit['recommended_size']}")
                st.write(f"**Style:** {outfit['style']}")
                st.write(f"**Color:** {outfit['color']}")
                
                # Product link
                st.markdown(f"[🛍️ Shop Now]({outfit['shop_link']})")
                
                # Recommendation reason
                st.markdown("### Why we recommend this")
                st.write(
                    "Based on your style preferences and previous choices, "
                    "this outfit matches your preferred color palette and fit."
                )
            
            st.divider()  # Add a visual separator between outfits
