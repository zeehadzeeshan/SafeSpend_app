
import os
from PIL import Image

SOURCE = 'www/new_icon.png'
RES_DIR = 'android/app/src/main/res/'

# (Folder Name, Legacy Size, Adaptive Size)
DENSITIES = [
    ('mipmap-mdpi', 48, 108),
    ('mipmap-hdpi', 72, 162),
    ('mipmap-xhdpi', 96, 216),
    ('mipmap-xxhdpi', 144, 324),
    ('mipmap-xxxhdpi', 192, 432)
]

def generate_icons():
    if not os.path.exists(SOURCE):
        print(f"Error: {SOURCE} not found.")
        return

    print("Opening source icon...")
    img = Image.open(SOURCE).convert("RGBA")

    for folder, leg_size, adapt_size in DENSITIES:
        target_dir = os.path.join(RES_DIR, folder)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # 1. Legacy Icon (ic_launcher.png) - Full Fill
        # We assume the source icon is square and good to go.
        print(f"Generating legacy icon for {folder} ({leg_size}x{leg_size})...")
        leg_img = img.resize((leg_size, leg_size), Image.Resampling.LANCZOS)
        leg_img.save(os.path.join(target_dir, 'ic_launcher.png'))
        
        # 1.1 Legacy Round (ic_launcher_round.png)
        # For simple fix, we use the same square - Android usually masks it, 
        # but optimally this would be pre-masked. We'll just save the square one 
        # and let the system handle/mask it or usage.
        # However, to be cleaner, we overwrite it with the same legacy image.
        leg_img.save(os.path.join(target_dir, 'ic_launcher_round.png'))

        # 2. Adaptive Foreground (ic_launcher_foreground.png) - Centered & Padded
        print(f"Generating adaptive foreground for {folder} ({adapt_size}x{adapt_size})...")
        
        # Create transparent canvas
        canvas = Image.new("RGBA", (adapt_size, adapt_size), (0, 0, 0, 0))
        
        # Scale icon to ~66% of canvas
        # 72/108 = 0.666 
        icon_size = int(adapt_size * 0.70) # Using 70% to be safe but visible
        icon_resized = img.resize((icon_size, icon_size), Image.Resampling.LANCZOS)
        
        # Center position
        x = (adapt_size - icon_size) // 2
        y = (adapt_size - icon_size) // 2
        
        canvas.paste(icon_resized, (x, y), icon_resized)
        canvas.save(os.path.join(target_dir, 'ic_launcher_foreground.png'))

    print("Icon generation complete.")

if __name__ == '__main__':
    generate_icons()
