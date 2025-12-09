import os
import shutil
import django
from pathlib import Path

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomproject.settings')
django.setup()

from core.models import Product

def update_product_images_from_folder(images_folder):
    """
    Update product images from a folder of downloaded images.
    
    Expected folder structure:
    images_folder/
        chino_pants.jpg
        loafers.jpg
        raincoat.jpg
        etc.
    """
    
    # Mapping of product IDs to expected image filenames
    product_image_map = {
        1: 'chino_pants',
        2: 'leather_boots',
        3: 'running_tights',
        4: 'fashion_belt',
        5: 'classic_denim_jeans',
        6: 'kids_tshirt',
        7: 'kids_jeans',
        8: 'loafers',
        9: 'raincoat',
        10: 'silk_scarf',
        11: 'yoga_pants',
        12: 'high_heels',
        13: 'skinny_jeans',
        14: 'distressed_jeans',
        15: 'track_jacket',
        16: 'kids_jacket',
        17: 'crossbody_bag'
    }
    
    # Get the media directory for user uploads
    media_root = Path('media/user_1')
    media_root.mkdir(parents=True, exist_ok=True)
    
    images_path = Path(images_folder)
    if not images_path.exists():
        print(f"Error: Folder {images_folder} does not exist!")
        return
    
    updated_count = 0
    
    for product_id, image_basename in product_image_map.items():
        # Find the image file (support jpg, jpeg, png, webp)
        image_file = None
        for ext in ['.jpg', '.jpeg', '.png', '.webp']:
            potential_file = images_path / f"{image_basename}{ext}"
            if potential_file.exists():
                image_file = potential_file
                break
        
        if not image_file:
            print(f"⚠️  No image found for product ID {product_id} ({image_basename})")
            continue
        
        # Copy to media directory
        dest_filename = f"{image_basename}{image_file.suffix}"
        dest_path = media_root / dest_filename
        shutil.copy2(image_file, dest_path)
        
        # Update product in database
        try:
            product = Product.objects.get(id=product_id)
            product.image = f"user_1/{dest_filename}"
            product.save()
            print(f"✅ Updated: {product.title} -> {dest_filename}")
            updated_count += 1
        except Product.DoesNotExist:
            print(f"⚠️  Product ID {product_id} not found")
    
    print(f"\n✅ Successfully updated {updated_count} product images!")

if __name__ == "__main__":
    # INSTRUCTIONS:
    # 1. Download your product images
    # 2. Place them in a folder (e.g., C:\\Users\\hp\\Downloads\\product_images)
    # 3. Run this script with the folder path:
    
    import sys
    if len(sys.argv) > 1:
        images_folder = sys.argv[1]
    else:
        images_folder = input("Enter the path to your images folder: ")
    
    update_product_images_from_folder(images_folder)
