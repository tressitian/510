import 'clothing_item.dart';

class Outfit {
  final String id;
  final String name;
  final List<ClothingItem> items;
  final DateTime createdAt;
  final String occasion;
  final String? imageUrl;
  final bool isFavorite;

  Outfit({
    required this.id,
    required this.name,
    required this.items,
    required this.createdAt,
    required this.occasion,
    this.imageUrl,
    this.isFavorite = false,
  });

  // TODO: Implement serialization methods (toJson, fromJson)
  
  // Factory method to create an Outfit from JSON
  factory Outfit.fromJson(Map<String, dynamic> json) {
    return Outfit(
      id: json['id'],
      name: json['name'],
      items: (json['items'] as List)
          .map((item) => ClothingItem.fromJson(item))
          .toList(),
      createdAt: DateTime.parse(json['createdAt']),
      occasion: json['occasion'],
      imageUrl: json['imageUrl'],
      isFavorite: json['isFavorite'] ?? false,
    );
  }

  // Method to convert Outfit to JSON
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'items': items.map((item) => item.toJson()).toList(),
      'createdAt': createdAt.toIso8601String(),
      'occasion': occasion,
      'imageUrl': imageUrl,
      'isFavorite': isFavorite,
    };
  }
} 