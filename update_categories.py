import os
import django
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomproject.settings')
django.setup()

from core.models import Category, Product

def update_categories():
    print("Starting category update...")
    
    # 1. Define new clothing categories
    new_category_names = [
        "Men's Fashion",
        "Women's Fashion",
        "Accessories",
        "Shoes",
        "Kids",
        "Sportswear",
        "Outerwear",
        "Streetwear"
    ]

    # 2. Create new categories
    new_cats_objs = []
    for title in new_category_names:
        # We use get_or_create to avoid duplicates if run multiple times
        cat, created = Category.objects.get_or_create(title=title)
        if created:
            print(f"Created new category: {title}")
        new_cats_objs.append(cat)

    # 3. Reassign ALL products to new categories randomly
    # We do this BEFORE deleting old categories to avoid SET_NULL issues if we want to ensure they have a category
    products = Product.objects.all()
    print(f"Reassigning {products.count()} products to new categories...")
    
    for p in products:
        random_cat = random.choice(new_cats_objs)
        p.category = random_cat
        p.save()
        
    # 4. Delete old categories
    # Delete any category that is NOT in our new list
    old_cats = Category.objects.exclude(title__in=new_category_names)
    count = old_cats.count()
    if count > 0:
        print(f"Deleting {count} old categories...")
        old_cats.delete()
    else:
        print("No old categories to delete.")

    print("Category update complete!")

if __name__ == "__main__":
    update_categories()
