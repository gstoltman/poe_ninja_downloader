import zipfile
import os

league_list = ['essence', 'breach', 'legacy', 'harbinger', 'abyss', 'bestiary', 'incursion', 'delve', 'betrayal', 'synthesis', 'legion', 'blight', 'metamorph', 'delirium', 'harvest', 'heist', 'ritual', 'ultimatum', 'expedition', 'scourge', 'archnemesis', 'sentinel', 'kalandra', 'sanctum']

# extracts all league data dumps into project

download_path = '/mnt/c/Users/Grant/Downloads'
extract_path = '/home/gstoltman/projects/scripts/poe_ninja_downloader/poe_ninja_downloader/exports'

for zip_folder in os.listdir(download_path):
    file_path = os.path.join(download_path, zip_folder)

    if zipfile.is_zipfile(file_path):
        
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)