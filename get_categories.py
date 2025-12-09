import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomproject.settings')
django.setup()

from core.models import Category

def get_categories():
    """Get all categories"""
    categories = Category.objects.all()
    
    print(f"Total categories: {categories.count()}\n")
    print("Categories:")
    print("-" * 50)
    
    for c in categories:
        print(f"ID: {c.id:3d} | Title: {c.title:25s} | Image: {c.image}")
    
    return list(categories)

if __name__ == "__main__":
    categories = get_categories()
