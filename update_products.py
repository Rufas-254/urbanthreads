import os
import django
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomproject.settings')
django.setup()

from core.models import Product

def update_products():
    print("Starting product update...")
    
    # Define clothing product names based on categories
    clothing_names = {
        "Men's Fashion": [
            "Classic Denim Jeans",
            "Cotton Polo Shirt",
            "Leather Belt",
            "Formal Dress Shirt",
            "Casual T-Shirt",
            "Chino Pants",
            "Slim Fit Blazer",
            "Graphic Tee",
        ],
        "Women's Fashion": [
            "Floral Midi Dress",
            "High-Waist Skinny Jeans",
            "Silk Blouse",
            "Knit Sweater",
            "Pencil Skirt",
            "Maxi Dress",
            "Leather Jacket",
            "Cardigan",
        ],
        "Accessories": [
            "Leather Wallet",
            "Sunglasses",
            "Canvas Tote Bag",
            "Silk Scarf",
            "Wrist Watch",
            "Beanie Hat",
            "Fashion Belt",
            "Crossbody Bag",
        ],
        "Shoes": [
            "Canvas Sneakers",
            "Leather Boots",
            "Running Shoes",
            "Formal Oxfords",
            "Sandals",
            "High Heels",
            "Loafers",
            "Ankle Boots",
        ],
        "Kids": [
            "Kids T-Shirt",
            "Kids Jeans",
            "Kids Sneakers",
            "Kids Hoodie",
            "Kids Dress",
            "Kids Shorts",
            "Kids Jacket",
            "Kids School Uniform",
        ],
        "Sportswear": [
            "Athletic Shorts",
            "Sports Bra",
            "Gym T-Shirt",
            "Yoga Pants",
            "Track Jacket",
            "Running Tights",
            "Training Hoodie",
            "Compression Shirt",
        ],
        "Outerwear": [
            "Winter Coat",
            "Puffer Jacket",
            "Trench Coat",
            "Bomber Jacket",
            "Windbreaker",
            "Raincoat",
            "Fleece Jacket",
            "Parka",
        ],
        "Streetwear": [
            "Oversized Hoodie",
            "Distressed Jeans",
            "Graphic Sweatshirt",
            "Cargo Pants",
            "Bucket Hat",
            "Chain Necklace",
            "Dad Sneakers",
            "Vintage Tee",
        ]
    }

    # Get all products
    products = Product.objects.all()
    print(f"Updating {products.count()} products...")
    
    # Track used names to avoid duplicates
    used_names = set()
    
    for product in products:
        # Get the category title
        category_title = product.category.title if product.category else "Men's Fashion"
        
        # Get available names for this category
        available_names = clothing_names.get(category_title, clothing_names["Men's Fashion"])
        
        # Filter out already used names
        unused_names = [name for name in available_names if name not in used_names]
        
        # If all names used, allow repeats with a number suffix
        if not unused_names:
            new_name = random.choice(available_names) + f" {random.randint(1, 99)}"
        else:
            new_name = random.choice(unused_names)
            used_names.add(new_name)
        
        old_name = product.title
        product.title = new_name
        product.save()
        print(f"  {old_name} -> {new_name}")
    
    print("Product update complete!")

if __name__ == "__main__":
    update_products()
