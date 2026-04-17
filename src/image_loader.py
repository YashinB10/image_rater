#Image Loader


import os


def is_valid_image(file_path: str) -> bool:
    if os.path.isfile(file_path):
       filename = os.path.basename(file_path)
       if filename.lower().endswith((".jpg", ".jpeg", ".png")):
           return True
       else:
           return False
    else:
        return False

def get_valid_images(folder_path: str) -> list:
    if not os.path.isdir(folder_path):
        raise ValueError("Invalid folder path")
    all_files = os.listdir(folder_path)
    valid_images = []
    for filename in all_files:
        full_path = os.path.join(folder_path, filename)
        if is_valid_image(full_path):
            valid_images.append(full_path)
    return valid_images
