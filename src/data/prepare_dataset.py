import os
import shutil
import pandas as pd

def prepare_folder_structure(label_csv_path, image_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(label_csv_path)

    for _, row in df.iterrows():
        image_id = row['id']
        label = row['label']
        src = os.path.join(image_dir, f"{image_id}.png")
        dst_dir = os.path.join(output_dir, label)
        dst = os.path.join(dst_dir, f"{image_id}.png")
        
        os.makedirs(dst_dir, exist_ok=True)
        
        try:
            shutil.copy(src, dst)
        except FileNotFoundError:
            print(f"⚠️ Missing image: {src}")

    print("✅ Done organizing images by class.")

if __name__ == "__main__":
    label_csv_path = "data/raw/trainLabels.csv"
    image_dir = "data/processed/train"
    output_dir = "data/processed/train_split"
    
    prepare_folder_structure(label_csv_path, image_dir, output_dir)

