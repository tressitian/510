import 'package:flutter/material.dart';
import '../models/outfit.dart';

class OutfitCard extends StatelessWidget {
  final Outfit outfit;
  final VoidCallback? onTap;
  final VoidCallback? onFavorite;
  
  const OutfitCard({
    super.key,
    required this.outfit,
    this.onTap,
    this.onFavorite,
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
            // Image or Items Grid
            Stack(
              children: [
                // Use placeholder instead of actual images
                AspectRatio(
                  aspectRatio: 4/3,
                  child: Container(
                    color: Colors.grey[200],
                    child: Center(
                      child: Icon(
                        Icons.style,
                        size: 60,
                        color: Colors.grey[400],
                      ),
                    ),
                  ),
                ),
                
                // Favorite button
                Positioned(
                  top: 8,
                  right: 8,
                  child: InkWell(
                    onTap: onFavorite,
                    child: Container(
                      padding: const EdgeInsets.all(6),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.7),
                        shape: BoxShape.circle,
                      ),
                      child: Icon(
                        outfit.isFavorite 
                            ? Icons.favorite 
                            : Icons.favorite_border,
                        color: outfit.isFavorite 
                            ? Colors.red 
                            : Colors.grey,
                        size: 20,
                      ),
                    ),
                  ),
                ),
              ],
            ),
            
            // Info
            Padding(
              padding: const EdgeInsets.all(12.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    outfit.name,
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
                      const Icon(
                        Icons.event,
                        size: 14,
                        color: Colors.grey,
                      ),
                      const SizedBox(width: 4),
                      Text(
                        outfit.occasion,
                        style: TextStyle(color: Colors.grey[600]),
                      ),
                      const Spacer(),
                      Text(
                        '${outfit.items.length} items',
                        style: TextStyle(color: Colors.grey[600], fontSize: 12),
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
  
  // Old method (not used anymore, but kept for reference)
  Widget _buildItemsGrid() {
    return AspectRatio(
      aspectRatio: 4/3,
      child: outfit.items.isEmpty
          ? Container(
              color: Colors.grey[200],
              child: const Center(
                child: Text('No items'),
              ),
            )
          : Container(
              color: Colors.grey[200],
              child: const Center(
                child: Icon(
                  Icons.style,
                  size: 60,
                  color: Colors.grey,
                ),
              ),
            ),
    );
  }
} 