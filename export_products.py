import os
import django
import json

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomproject.settings')
django.setup()

from core.models import Product

def export_products_json():
    """Export product data to JSON for image generation"""
    products = Product.objects.all().order_by('id')
    
    product_list = []
    for p in products:
        product_list.append({
            'id': p.id,
            'pid': p.pid,
            'title': p.title,
            'category': p.category.title if p.category else "Uncategorized"
        })
    
    output_path = 'products_for_images.json'
    with open(output_path, 'w') as f:
        json.dump(product_list, f, indent=2)
    
    print(f"Exported {len(product_list)} products to {output_path}")
    return product_list

if __name__ == "__main__":
    products = export_products_json()
    for p in products:
        print(f"{p['id']:3d}: {p['title']:30s} ({p['category']})")
