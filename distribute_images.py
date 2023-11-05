import shutil
import os
from PIL import Image

LABELERS = ["Francine", "James", "Ryan", "Brittany", "Katie"]
INPUT_DIR = 'input_images'
OUTPUT_DIR = 'images_to_label'
IMAGE_CATEGORY = 'google_0'
CURRENT_DIR = os.getcwd()

def move_images():
    input_path = os.path.join(CURRENT_DIR, INPUT_DIR)
    images_list = os.listdir(input_path)

    output_dirs = [os.path.join(CURRENT_DIR, OUTPUT_DIR, labeler, IMAGE_CATEGORY) for labeler in LABELERS]
    num_groups = len(LABELERS)

    for path_i in range(len(images_list)):
        original_path = os.path.join(input_path, images_list[path_i])
        image = Image.open(original_path)

        # Convert to jpg and change file name to index
        filename = str(path_i) + ".jpg"
        new_path = os.path.join(input_path, filename)
        image.save(new_path)
        image.close()
        

        # Move image to labeler folder
        shutil.move(new_path, os.path.join(output_dirs[path_i % num_groups], filename))
        os.remove(original_path)


if __name__ == '__main__':
    move_images()