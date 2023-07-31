# download necessary zipped files from: 
# https://drive.google.com/file/d/1qMwLSuHDNqise0IDAUAaqMctRiUapg0Q/view?usp=drive_link

import zipfile, os, shutil, tqdm, logging
from typing import Iterable

def copy_folders(source_folders: Iterable[str], destination_folder: str, move: bool=False):
    for folder in source_folders:
        source_path = os.path.abspath(folder)
        destination_path = os.path.abspath(os.path.join(destination_folder, os.path.basename(folder)))
        if os.path.exists(os.path.join(destination_folder, folder)):
            logging.info(f"Folder '{folder}' already exists in  '{destination_folder}'")
            continue
        
        if not move:
            shutil.copytree(source_path, destination_path)
            logging.info(f"Folder '{source_path}' copied to '{destination_path}'")
        else:
            shutil.move(source_path, destination_path)
            logging.info(f"Folder '{source_path}' moved to '{destination_path}'")

def zip_folder(folder_path: str, output_zip_path: str):
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in tqdm.tqdm(os.walk(folder_path)):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

                
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="\n%(asctime)s - %(levelname)s - %(message)s")
    source_folders = [
        "flan-t5-base_finetuned_results",
        "flan-t5-small_finetuned_results",
        "alpaca-native_finetuned_results",
        "lora-flan-t5-base",
        "lora-flan-t5-small",
        "lora-alpaca-native",
    ]
    destination_folder = "LoRA_results_and_logs_folder"
    output_zip_file = "zipped_LoRA_results_and_logs_folder.zip"
    
    logging.info(f"copying / moving weights and logs folder to {destination_folder}")
    copy_folders(source_folders, destination_folder, move=False)
    
    logging.info(f"zipping {destination_folder} to {output_zip_file}")
    zip_folder(destination_folder, output_zip_file)