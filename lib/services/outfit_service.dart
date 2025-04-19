import '../models/outfit.dart';
import '../models/clothing_item.dart';
import 'wardrobe_service.dart';

class OutfitService {
  // Singleton pattern
  static final OutfitService _instance = OutfitService._internal();
  
  factory OutfitService() {
    return _instance;
  }
  
  OutfitService._internal();
  
  final WardrobeService _wardrobeService = WardrobeService();
  
  // Mock data for initial development
  List<Outfit> _outfits = [];
  
  // Get all outfits
  Future<List<Outfit>> getAllOutfits() async {
    // TODO: Replace with actual data fetching
    return Future.value(_outfits);
  }
  
  // Get outfit by ID
  Future<Outfit?> getOutfitById(String id) async {
    final index = _outfits.indexWhere((outfit) => outfit.id == id);
    if (index != -1) {
      return Future.value(_outfits[index]);
    }
    return Future.value(null);
  }
  
  // Save a new outfit
  Future<void> saveOutfit(Outfit outfit) async {
    // TODO: Implement proper storage
    _outfits.add(outfit);
    return Future.value();
  }
  
  // Delete an outfit
  Future<void> deleteOutfit(String id) async {
    // TODO: Implement proper storage
    _outfits.removeWhere((outfit) => outfit.id == id);
    return Future.value();
  }
  
  // Toggle favorite status
  Future<void> toggleFavorite(String id) async {
    final index = _outfits.indexWhere((outfit) => outfit.id == id);
    if (index != -1) {
      final outfit = _outfits[index];
      _outfits[index] = Outfit(
        id: outfit.id,
        name: outfit.name,
        items: outfit.items,
        createdAt: outfit.createdAt,
        occasion: outfit.occasion,
        imageUrl: outfit.imageUrl,
        isFavorite: !outfit.isFavorite,
      );
    }
    return Future.value();
  }
  
  // Generate outfit based on occasion and weather
  Future<Outfit> generateOutfit({
    required String occasion,
    String? weather,
  }) async {
    // TODO: Implement AI outfit generation
    // For now, just return a mock outfit
    
    final allItems = await _wardrobeService.getAllItems();
    
    // Simple mock implementation - pick one top and one bottom
    final topItems = allItems.where((item) => item.category == 'top').toList();
    final bottomItems = allItems.where((item) => item.category == 'bottom').toList();
    
    final selectedTop = topItems.isNotEmpty 
        ? topItems.first 
        : ClothingItem(
            id: 'mock-top',
            name: 'Mock Top',
            category: 'top',
            color: 'blue',
            imageUrl: 'assets/images/mock_top.png',
            dateAdded: DateTime.now(),
          );
    
    final selectedBottom = bottomItems.isNotEmpty 
        ? bottomItems.first 
        : ClothingItem(
            id: 'mock-bottom',
            name: 'Mock Bottom',
            category: 'bottom',
            color: 'black',
            imageUrl: 'assets/images/mock_bottom.png',
            dateAdded: DateTime.now(),
          );
    
    return Outfit(
      id: 'generated-${DateTime.now().millisecondsSinceEpoch}',
      name: 'Generated Outfit for $occasion',
      items: [selectedTop, selectedBottom],
      createdAt: DateTime.now(),
      occasion: occasion,
    );
  }
} 