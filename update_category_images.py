import os
import shutil
import django
from pathlib import Path

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomproject.settings')
django.setup()

from core.models import Category

def update_category_images(images_folder):
    """
    Update category images from a folder.
    
    Expected filenames:
        mens_fashion.jpg
        womens_fashion.jpg
        accessories.jpg
        shoes.jpg
        kids.jpg
        sportswear.jpg
        outerwear.jpg
        streetwear.jpg
    """
    
    # Mapping of category titles to expected image filenames
    category_image_map = {
        "Men's Fashion": 'mens_fashion',
        "Women's Fashion": 'womens_fashion',
        "Accessories": 'accessories',
        "Shoes": 'shoes',
        "Kids": 'kids',
        "Sportswear": 'sportswear',
        "Outerwear": 'outerwear',
        "Streetwear": 'streetwear'
    }
    
    # Create category media directory
    media_root = Path('media/category')
    media_root.mkdir(parents=True, exist_ok=True)
    
    images_path = Path(images_folder)
    if not images_path.exists():
        print(f"❌ Error: Folder {images_folder} does not exist!")
        return
    
    updated_count = 0
    categories = Category.objects.all()
    
    for category in categories:
        image_basename = category_image_map.get(category.title)
        
        if not image_basename:
            print(f"⚠️  Unknown category: {category.title}")
            continue
        
        # Find the image file (support jpg, jpeg, png, webp)
        image_file = None
        for ext in ['.jpg', '.jpeg', '.png', '.webp']:
            potential_file = images_path / f"{image_basename}{ext}"
            if potential_file.exists():
                image_file = potential_file
                break
        
        if not image_file:
            print(f"⚠️  No image found for {category.title} ({image_basename})")
            continue
        
        # Copy to media directory
        dest_filename = f"{image_basename}{image_file.suffix}"
        dest_path = media_root / dest_filename
        shutil.copy2(image_file, dest_path)
        
        # Update category in database
        category.image = f"category/{dest_filename}"
        category.save()
        print(f"✅ Updated: {category.title} -> {dest_filename}")
        updated_count += 1
    
    print(f"\n✅ Successfully updated {updated_count} category images!")
    print("\n🔄 Please refresh your browser to see the changes.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        images_folder = sys.argv[1]
    else:
        images_folder = input("Enter the path to your category images folder: ")
    
    update_category_images(images_folder)
