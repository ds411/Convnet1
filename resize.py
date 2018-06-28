import os
from PIL import Image

size = 100, 100

orig_dir = ['original_training_data/train/object', 'original_training_data/train/not_object', 
            'original_training_data/validation/object', 'original_training_data/validation/not_object', 
            'original_training_data/predict']
target_dir = ['training_data/train/object', 'training_data/train/not_object', 
              'training_data/validation/object', 'training_data/validation/not_object',
              'training_data/predict']

for d in range (0, len(orig_dir), 1):
    i = 0
    images = os.listdir(orig_dir[d])  
    for infile in images:
        outfile = str(i) + ".jpg"
        try:
            im = Image.open(orig_dir[d] + "/" + infile)
            im = im.resize(size, Image.NEAREST)
            im.save(target_dir[d] + "/" + outfile, "JPEG")
        except IOError:
            print("Cannot resize " + infile)
        i += 1