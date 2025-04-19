# 👗 Smart Closet: AI-Powered Wardrobe Organizer & Stylist

A Flutter mobile application that helps users manage their wardrobe and get personalized outfit suggestions.

## 📌 Project Scope

Smart Closet is an AI-powered app that helps users manage their wardrobe and get personalized outfit suggestions.

- Automatically detect and catalog clothing items from everyday photos
- Recommend daily outfits based on owned clothes, weather, and occasions
- Suggest new items to purchase that match the user's style and wardrobe gaps

The goal is to reduce decision fatigue, promote sustainable shopping, and boost confidence in personal style.

## 🛠️ Project Structure

```
lib/
├── main.dart              # Application entry point
├── screens/               # UI screens
│   ├── home_screen.dart        # Home screen with weather and daily suggestions
│   ├── wardrobe_screen.dart    # Wardrobe management screen
│   ├── outfit_screen.dart      # Outfit suggestions screen
│   └── profile_screen.dart     # User profile screen
├── models/                # Data models
│   ├── clothing_item.dart      # Clothing item model
│   └── outfit.dart             # Outfit model
├── services/              # Business logic
│   ├── wardrobe_service.dart   # Service for managing clothing items
│   └── outfit_service.dart     # Service for managing outfits
└── widgets/               # Reusable UI components
    ├── clothing_item_card.dart # Card to display clothing item
    └── outfit_card.dart        # Card to display outfit
```

## 🚀 Getting Started

### Prerequisites

- Flutter SDK: 3.0.0 or higher
- Dart SDK: 3.0.0 or higher

### Installation

1. Clone the repository
```
git clone https://github.com/your-username/smart_closet.git
```

2. Navigate to the project directory
```
cd smart_closet
```

3. Install dependencies
```
flutter pub get
```

4. Run the app
```
flutter run
```

## ✨ Features

- 📷 Auto-detect and catalog clothes from users' existing photo albums
- 👕 Recommend outfits based on wardrobe, weather, and occasion
- 🛍️ Suggest new purchases that match user style and fill wardrobe gaps

## 📱 Screens

- **Home**: Weather information and daily outfit suggestion
- **Wardrobe**: View and manage clothing items
- **Outfits**: Browse and generate outfit suggestions
- **Profile**: User profile and preferences

## 👥 Contact Information

**Client**: Tressi Tian
-  📧 Email: tressi@uw.edu
-  GitHub: [@tressitian](https://github.com/tressitian)

**Developer**: Yuzhe Zhang  
- 📧 Email: yuzhez23@uw.edu
- GitHub: [@zyzzzz-123](https://github.com/zyzzzz-123)  

## 📋 Development Progress

### Week 3 Updates (Current)
- ✅ Established the basic Flutter application framework
- ✅ Implemented bottom navigation with four main screens
- ✅ Created data models for clothing items and outfits
- ✅ Developed service classes for wardrobe and outfit management
- ✅ Built reusable UI components for displaying clothing items and outfits
- ✅ Successfully tested the app on iOS device

### To-Do
- [ ] Implement clothing detection model integration
- [ ] Add persistent storage for wardrobe items
- [ ] Integrate weather API
- [ ] Create AI-based outfit recommendation engine 