import streamlit as st
import requests
from datetime import datetime

def get_weather():
    # This is a placeholder for weather API integration
    # You can integrate with real weather API like OpenWeatherMap
    return {
        "temperature": "22°C",
        "condition": "Sunny",
        "humidity": "65%"
    }

def show_ai_suggestion():
    st.header("Outfit Suggestions")
    
    # Display current weather
    weather = get_weather()
    weather_col1, weather_col2, weather_col3 = st.columns(3)
    with weather_col1:
        st.metric("Temperature", weather["temperature"])
    with weather_col2:
        st.metric("Condition", weather["condition"])
    with weather_col3:
        st.metric("Humidity", weather["humidity"])
    
    # User input section
    st.subheader("What's your preference today?")
    user_preference = st.text_input(
        "Enter your requirements (e.g., casual meeting, outdoor activity, formal dinner)",
        placeholder="I need an outfit for..."
    )
    
    if user_preference:
        # Display outfit suggestions based on user input
        st.subheader("Suggestions based on your needs:")
        
        # Create three columns for outfit suggestions
        col1, col2, col3 = st.columns(3)
        
        # Outfit suggestions data
        outfits = [
            {
                "title": "Business Casual",
                "image": "outfit_images/outfit1.jpg",
                "items": [
                    "Light blue oxford shirt",
                    "Navy chinos",
                    "Brown leather loafers",
                    "Leather belt"
                ],
                "reason": "This combination strikes the perfect balance between professional and approachable. The oxford shirt keeps it business-appropriate while the chinos maintain comfort."
            },
            {
                "title": "Smart Casual",
                "image": "outfit_images/outfit2.jpeg",
                "items": [
                    "Gray hoodie",
                    "Khaki pants",
                    "White sneakers"
                ],
                "reason": "A comfortable yet put-together look that works for casual outings. The hoodie keeps it relaxed while the khaki pants add a touch of polish, and white sneakers complete this versatile everyday outfit."
            },
            {
                "title": "Casual Weekend",
                "image": "outfit_images/outfit3.jpg",
                "items": [
                    "Leather jacket",
                    "Denim jeans"
                ],
                "reason": "A classic combination that balances style with edge. The leather jacket adds a bold statement while the denim jeans provide versatility and comfort for any weekend activity."
            },
            {
                "title": "Casual Weekend",
                "image": "outfit_images/outfit4.jpg",
                "items": [
                    "FOG hoodie",
                    "Khaki pants",
                ],
                "reason": "A trendy streetwear ensemble that combines comfort with style. The FOG hoodie brings a premium casual element while the khaki pants elevate the look beyond basic loungewear."
            }
        ]
        
        # Display outfits
        for col, outfit in zip([col1, col2, col3], outfits):
            with col:
                st.markdown(f"### {outfit['title']}")
                st.image(outfit['image'])
                st.markdown("**Selected Items:**")
                items_list = "\n".join([f"- {item}" for item in outfit['items']])
                st.markdown(items_list)
                st.markdown("**Why this outfit:**")
                st.markdown(outfit['reason'])
    else:
        # Random Suggestions Section (only shown when no user input)
        st.subheader(" ")
        
        # # Create three columns for random outfit suggestions
        # rand_col1, rand_col2, rand_col3 = st.columns(3)
        
        # # Random outfit suggestions data
        # random_outfits = [
        #     {
        #         "title": "Trendy Casual",
        #         "image": "outfit_images/outfit1.jpg",
        #         "items": [
        #             "Oversized graphic tee",
        #             "High-waisted jeans",
        #             "White sneakers",
        #             "Statement necklace"
        #         ],
        #         "reason": "A contemporary casual look that's both comfortable and stylish."
        #     },
        #     {
        #         "title": "Sporty Chic",
        #         "image": "outfit_images/outfit2.jpeg",
        #         "items": [
        #             "Athletic jacket",
        #             "Fitted tank top",
        #             "Yoga pants",
        #             "Running shoes"
        #         ],
        #         "reason": "Perfect blend of athletic wear and street style."
        #     },
        #     {
        #         "title": "Weekend ",
        #         "image": "outfit_images/outfit3.jpg",
        #         "items": [
        #             "Floral sundress",
        #             "Denim jacket",
        #             "Sandals",
        #             "Straw hat"
        #         ],
        #         "reason": "Light and breezy outfit ideal for casual social occasions."
        #     }
        # ]
        
        # # Display random outfits
        # for col, outfit in zip([rand_col1, rand_col2, rand_col3], random_outfits):
        #     with col:
        #         st.markdown(f"### {outfit['title']}")
        #         st.image(outfit['image'])
        #         st.markdown("**Selected Items:**")
        #         items_list = "\n".join([f"- {item}" for item in outfit['items']])
        #         st.markdown(items_list)
        #         st.markdown("**Why this outfit:**")
        #         st.markdown(outfit['reason'])
