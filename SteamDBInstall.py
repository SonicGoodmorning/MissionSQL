import kagglehub
import os
import shutil

# Download latest version
def downloadDS():
    path = kagglehub.dataset_download("fronkongames/steam-games-dataset")
    jsonPath = os.path.join(path, 'games.json')
    
    ## shutil copies to the program directory so it actually works
    shutil.copy(jsonPath, 'games.json')
    print('Dataset Ready')
    return jsonPath

if __name__ == "__main__":
    downloadDS()
