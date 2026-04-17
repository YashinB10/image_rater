#Main.Py

#Imports:
from PIL import Image
from image_loader import get_valid_images
from rating import get_rating
from stats import compute_stats
from storage import save_results
import os

#Main Script:
def main():
    while True:
        folder_path = input("Enter the folder path of your images: ")
        try:
            valid_images = get_valid_images(folder_path)
        except ValueError:
            print("Invalid folder path")
            continue
        if not valid_images:
            print("No valid images found")
            continue
        else:
            break
    
    ratings = []
    input(
    "Images will be shown one by one.\n"
    "Press Enter to rate each image (rating: 0–10).\n"
    "Press Enter to start..."
)
        
    rated_images = []
    for i, path in enumerate(valid_images):
        print(f"Image {i+1}/{len(valid_images)}")
        print(f"Path: {path}")
        try:
            with Image.open(path) as image:
                image.show()
        except Exception as e:
            print(f"Error opening image: {e}") 
            continue
        input("Press Enter to rate this image...")
        rating = get_rating()
        rated_images.append(path)
        ratings.append(rating)
        print("-" * 30)
    if not ratings:
        print("No ratings were collected")
        return
    stats = compute_stats(ratings)
    print("\nResults:")
    print(f"Mean: {stats['mean']}")
    print(f"Min: {stats['min']}")
    print(f"Max: {stats['max']}")
    print(f"Count: {stats['count']}")
    print("\nSaving results...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "results.json")

    save_results(file_path, rated_images, ratings, stats)

if __name__ == "__main__":
    main()

