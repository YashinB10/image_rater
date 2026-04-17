#Data save

import json
import os

def save_results(file_path: str, images: list, ratings: list, stats: dict):
    if len(images) != len(ratings):
        raise ValueError("Images and ratings length mismatch")

    images_data = []

    for path, rating in zip(images, ratings):
        images_data.append({
            "path": path,
            "rating": rating
        })

    data = {
        "images": images_data,
        "stats": stats
    }

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print("Saving to:", os.path.abspath(file_path))
