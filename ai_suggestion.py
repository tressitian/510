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
        # Display outfit suggestions
        st.subheader("Recommended Outfits")
        
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
                "image": "outfit_images/outfit1.jpg",
                "items": [
                    "White crew neck t-shirt",
                    "Gray blazer",
                    "Dark wash jeans",
                    "White minimalist sneakers"
                ],
                "reason": "A modern take on casual wear that's perfect for various social settings. The blazer adds sophistication while the sneakers keep it contemporary."
            },
            {
                "title": "Casual Weekend",
                "image": "outfit_images/outfit1.jpg",
                "items": [
                    "Navy polo shirt",
                    "Beige chino shorts",
                    "Canvas sneakers",
                    "Leather watch"
                ],
                "reason": "Ideal for weekend activities while maintaining style. The polo adds a touch of refinement to a casual ensemble."
            }
        ]
        
        # Display outfits
        for col, outfit in zip([col1, col2, col3], outfits):
            with col:
                st.markdown(f"### {outfit['title']}")
                st.image(outfit['image'], caption=f"{outfit['title']} Preview")
                st.markdown("**Selected Items:**")
                items_list = "\n".join([f"- {item}" for item in outfit['items']])
                st.markdown(items_list)
                st.markdown("**Why this outfit:**")
                st.markdown(outfit['reason'])
