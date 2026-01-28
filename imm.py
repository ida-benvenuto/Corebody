from PIL import Image
import os

input_folder = "input_folder"
output_folder = "output"
final_size = (512, 512)

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith(".png"):
        img = Image.open(os.path.join(input_folder, file)).convert("RGBA")

        # Mantiene proporzioni
        img.thumbnail(final_size, Image.LANCZOS)

        # Crea canvas trasparente
        background = Image.new("RGBA", final_size, (0, 0, 0, 0))

        # Centra l'immagine
        x = (final_size[0] - img.size[0]) // 2
        y = (final_size[1] - img.size[1]) // 2

        background.paste(img, (x, y), img)

        background.save(os.path.join(output_folder, file))

print("Fatto!")
