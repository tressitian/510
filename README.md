# StyleFusion: Closet Assistant

A smart closet assistant web app built with Streamlit and Python, featuring AI-powered clothing analysis and outfit suggestions.

---

## 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key**
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```
   The app will be available at [http://localhost:8501](http://localhost:8501)

---

## 💡 Usage
- **Your Closet**: View, upload, and analyze your clothing items with AI.
- **Outfit Suggestions**: Get AI-powered outfit recommendations based on your preferences and weather.
- **New Clothes Purchase**: Explore suggestions for new clothing purchases.
- **Analyze**: Visualize your wardrobe usage and style trends.

---

## 📈 Progress
- [x] Streamlit UI with tab navigation
- [x] AI-powered clothing image analysis (OpenAI Vision)
- [x] Outfit suggestion logic
- [x] Weather integration (placeholder)
- [x] Wardrobe usage analytics
- [x] Responsive, modern UI
- [ ] User authentication (planned)
- [ ] Mobile optimization (planned)
- [ ] Enhanced purchase recommendations (planned)

---

## 🐞 Known Issues
- The AI analysis requires a valid OpenAI API key and internet connection.
- Some features (e.g., purchase suggestions, weather) use placeholder/demo data.
- Camera input may not work on all browsers/devices (Streamlit limitation).
- UI may require further optimization for mobile screens.

---

Feel free to open issues or contribute! 