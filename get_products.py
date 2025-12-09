import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomproject.settings')
django.setup()

from core.models import Product

def get_product_info():
    """Get all product information for image generation"""
    products = Product.objects.all()
    
    print(f"Total products: {products.count()}\n")
    print("Product details:")
    print("-" * 80)
    
    product_data = []
    for p in products:
        category = p.category.title if p.category else "Uncategorized"
        product_data.append({
            'id': p.id,
            'pid': p.pid,
            'title': p.title,
            'category': category
        })
        print(f"ID: {p.id:3d} | PID: {p.pid:15s} | Category: {category:20s} | Title: {p.title}")
    
    return product_data

if __name__ == "__main__":
    products = get_product_info()
