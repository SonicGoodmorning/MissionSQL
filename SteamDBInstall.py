import kagglehub
import os

# Download latest version
def downloadDS():
    path = kagglehub.dataset_download("fronkongames/steam-games-dataset")

    jsonPath = os.path.join(path, 'games.json')

    print('Dataset Ready')
    return jsonPath

if __name__ == "__main__":
    downloadDS()
