import 'package:flutter/material.dart';
import '../models/clothing_item.dart';

class ClothingItemCard extends StatelessWidget {
  final ClothingItem item;
  final VoidCallback? onTap;
  final VoidCallback? onDelete;
  
  const ClothingItemCard({
    super.key,
    required this.item,
    this.onTap,
    this.onDelete,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      clipBehavior: Clip.antiAlias,
      margin: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      child: InkWell(
        onTap: onTap,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Image Placeholder
            AspectRatio(
              aspectRatio: 1,
              child: _buildImageWidget(),
            ),
            
            // Info
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    item.name,
                    style: const TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 16,
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 4),
                  Row(
                    children: [
                      Icon(
                        Icons.circle,
                        size: 14,
                        color: _parseColor(item.color),
                      ),
                      const SizedBox(width: 4),
                      Text(
                        item.category,
                        style: TextStyle(color: Colors.grey[600]),
                      ),
                      const Spacer(),
                      if (onDelete != null)
                        IconButton(
                          icon: const Icon(Icons.delete_outline, size: 18),
                          onPressed: onDelete,
                          color: Colors.grey[600],
                          padding: EdgeInsets.zero,
                          constraints: const BoxConstraints(),
                        ),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
  
  // Build image widget or placeholder
  Widget _buildImageWidget() {
    // Use a placeholder for now
    return Container(
      color: Colors.grey[300],
      child: Center(
        child: Icon(
          _getCategoryIcon(),
          size: 40,
          color: Colors.grey[600],
        ),
      ),
    );
    
    // Original image loading code (commented out)
    /*
    return Image.network(
      item.imageUrl,
      fit: BoxFit.cover,
      errorBuilder: (context, error, stackTrace) {
        return Container(
          color: Colors.grey[300],
          child: const Center(
            child: Icon(
              Icons.image_not_supported,
              color: Colors.grey,
            ),
          ),
        );
      },
    );
    */
  }
  
  // Get icon based on clothing category
  IconData _getCategoryIcon() {
    switch (item.category.toLowerCase()) {
      case 'top':
      case 'shirt':
      case 'blouse':
        return Icons.accessibility;
      case 'bottom':
      case 'pants':
      case 'skirt':
        return Icons.airline_seat_legroom_normal;
      case 'dress':
        return Icons.woman;
      case 'outerwear':
      case 'jacket':
      case 'coat':
        return Icons.layers;
      case 'shoes':
        return Icons.directions_walk;
      case 'accessory':
      case 'accessories':
        return Icons.watch;
      default:
        return Icons.checkroom;
    }
  }
  
  // Parse color string to Color
  Color _parseColor(String colorName) {
    switch (colorName.toLowerCase()) {
      case 'red':
        return Colors.red;
      case 'blue':
        return Colors.blue;
      case 'green':
        return Colors.green;
      case 'yellow':
        return Colors.yellow;
      case 'orange':
        return Colors.orange;
      case 'purple':
        return Colors.purple;
      case 'pink':
        return Colors.pink;
      case 'brown':
        return Colors.brown;
      case 'grey':
      case 'gray':
        return Colors.grey;
      case 'black':
        return Colors.black;
      case 'white':
        return Colors.white;
      default:
        return Colors.blueGrey;
    }
  }
} 