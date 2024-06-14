from PIL import Image
import cv2
import numpy as np

def resize_image(image_path, max_length):
    # Open the image file
    image = Image.open(image_path)

    # Get the dimensions of the image
    width, height = image.size
    # Calculate the aspect ratio
    aspect_ratio = width / height
    # Determine which side to resize
    if width > height:
        new_width = max_length
        new_height = int(max_length / aspect_ratio)
    else:
        new_height = max_length
        new_width = int(max_length * aspect_ratio)

    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

    return resized_image
	
def overlayImage(person_img_path, bg_img_path):
  person_img = Image.open(person_img_path).convert("RGB")
  bg_img = Image.open(bg_img_path)

  person_img = cv2.cvtColor(np.array(person_img), cv2.COLOR_BGR2RGB)
  person_img = Image.fromarray(person_img)

  pixels_img1 = person_img.load()
  pixels_img2 = bg_img.load()

  # Get y-coordinate where person should start to appear at the bottom of background
  start_y = person_img.height - bg_img.height
  start_x = (bg_img.width - person_img.width) // 2
  # Iterate over each pixel -------
  for x in range(person_img.width):
      for y in range(person_img.height):
          # If pixel in person_img is not black (0), paste corresponding pixel from bg_img
          if pixels_img1[x, y] != (0, 0, 0):
              #pixels_img2[x, y] = pixels_img1[x, y]
              #pixels_img2[x, y - start_y] = pixels_img1[x, y]
              pixels_img2[x + start_x, y - start_y] = pixels_img1[x, y]              
  return bg_img

