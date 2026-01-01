import os
import shutil
import random

# Config
SOURCE_DIR = "dataset"
DEST_DIR = "dataset_split"

SPLITS = {
    "train": 0.7,
    "val": 0.2,
    "test": 0.1
}

random.seed(42)

classes = ["drone", "bird", "balloon", "airplane"]

# Create splits directories
for split in SPLITS:
    for cls in classes:
        os.makedirs(os.path.join(DEST_DIR, split, cls), exist_ok=True)

for cls in classes:
    cls_path = os.path.join(SOURCE_DIR, cls)
    images = [
        f for f in os.listdir(cls_path)
        if os.path.isfile(os.path.join(cls_path, f))
        and f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
    random.shuffle(images)

    total = len(images)
    train_end = int(total * SPLITS["train"])
    val_end = train_end + int(total * SPLITS["val"])

    split_sets = {
        "train": images[:train_end],
        "val": images[train_end:val_end],
        "test": images[val_end:]
    }

    for split, imgs in split_sets.items():
        for img in imgs:
            src = os.path.join(cls_path, img)
            dst = os.path.join(DEST_DIR, split, cls, img)
            shutil.copy(src, dst)

print("Dataset split completed.")