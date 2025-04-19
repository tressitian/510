class ClothingItem {
  final String id;
  final String name;
  final String category;
  final String color;
  final String imageUrl;
  final List<String> tags;
  final DateTime dateAdded;
  
  ClothingItem({
    required this.id,
    required this.name,
    required this.category,
    required this.color,
    required this.imageUrl,
    this.tags = const [],
    required this.dateAdded,
  });
  
  // TODO: Implement serialization methods (toJson, fromJson)
  
  // Factory method to create a ClothingItem from JSON
  factory ClothingItem.fromJson(Map<String, dynamic> json) {
    return ClothingItem(
      id: json['id'],
      name: json['name'],
      category: json['category'],
      color: json['color'],
      imageUrl: json['imageUrl'],
      tags: List<String>.from(json['tags'] ?? []),
      dateAdded: DateTime.parse(json['dateAdded']),
    );
  }
  
  // Method to convert ClothingItem to JSON
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'category': category,
      'color': color,
      'imageUrl': imageUrl,
      'tags': tags,
      'dateAdded': dateAdded.toIso8601String(),
    };
  }
} 