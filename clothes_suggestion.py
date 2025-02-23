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
    
    outfits = [
        {
            "image_url": "https://i.ebayimg.com/images/g/vGsAAOSwebVns3uy/s-l300.jpg",
            "brand": "Porsche",
            "price": "$2,190",
            "recommended_size": "L",
            "style": "",  # Provided "Style:" but no specific descriptor
            "color": "Black and Yellow",
            "shop_link": "https://stockx.com/aime-leon-dore-x-porsche-993-turbo-leather-club-jacket-british-racing-green"
        },
        {
            "image_url": "https://us.supreme.com/cdn/shop/files/P31_SS25_RegularJean_Newsprint01_Reshoot_360x.jpg?v=1738778018",
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
    
    # Add a "Generated Outcome" section
    st.subheader("Generated Outcome")
    st.write(
        "Here's a hypothetical look at how these two recommendations might come together. "
        "We combined the Porsche jacket with the Supreme jeans for a bold, stylish ensemble."
    )
    
    # Replace this placeholder with your actual image or a generated image
    st.image(
        "https://placeholder.com/400x600",
        caption="Sample outcome combining both recommendations"
    )
    
    # You could also add additional descriptive text about the final style
    st.write(
        "The sleek black and yellow accents on the jacket pair well with the "
        "blue newspaper print jeans, creating a unique streetwear statement."
    )
