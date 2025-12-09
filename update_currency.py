import os
import re

def update_currency_in_templates():
    """Replace $ with KSh in all HTML templates"""
    print("Starting currency symbol update...")
    
    templates_dir = r"c:\Users\hp\PycharmProjects\django-ecommerce\templates"
    updated_count = 0
    
    # Walk through all files in templates directory
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                try:
                    # Read the file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Count occurrences before replacement
                    original_count = content.count('$')
                    
                    if original_count > 0:
                        # Replace $ with KSh
                        new_content = content.replace('$', 'KSh ')
                        
                        # Write back
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        print(f"  Updated {file}: {original_count} occurrences")
                        updated_count += 1
                
                except Exception as e:
                    print(f"  Error processing {file}: {e}")
    
    print(f"\nCurrency update complete! Updated {updated_count} files.")

if __name__ == "__main__":
    update_currency_in_templates()
