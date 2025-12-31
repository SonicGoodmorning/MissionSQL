## first time naming my py file main, i feel all business man rn anyways just disregard that.

# Simple parse of the 'games.json' file.
import os
import json
import sqlite3
from icecream import ic

def tables(cursor):
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
      appid TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      release_date TEXT,
      price REAL,
      positive INTEGER,
      negative INTEGER,
      metacritic_score INTEGER,
      peak_ccu INTEGER,
      required_age INTEGER,
      dlc_count INTEGER,
      achievements INTEGER,
      recommendations INTEGER,
      average_playtime INTEGER,
      median_playtime INTEGER
                 )                 
            ''')
  ## create table for genre
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS genres(
          appid TEXT,
          genre TEXT,
          PRIMARY KEY (appid, genre),
          FOREIGN KEY (appid) REFERENCES games(appid)
        )              
    ''')
  ## create table for devs
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS developers(
          appid TEXT,
          developer TEXT,
          PRIMARY KEY (appid, developer),
          FOREIGN KEY (appid) REFERENCES games(appid)
        )              
    ''')
  ## create table for publisher
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS publishers(
          appid TEXT,
          publisher TEXT,
          PRIMARY KEY (appid, publisher),
          FOREIGN KEY (appid) REFERENCES games(appid)
        )              
    ''')
  ## create table for categories
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
          appid TEXT,
          category TEXT,
          PRIMARY KEY (appid, category),
          FOREIGN KEY (appid) REFERENCES games(appid)
        )              
    ''')
  ## create table for platforms
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS platform_support(
          appid TEXT PRIMARY KEY,
          windows BOOLEAN,
          mac BOOLEAN,
          linux BOOLEAN,
          FOREIGN KEY (appid) REFERENCES games(appid)
        )              
    ''')
  ic("Tables Created")


def loadData(jsonPath='games.json'):
  dataset = {}
  if os.path.exists(jsonPath):
    with open(jsonPath, 'r', encoding='utf-8') as fin:
      text = fin.read()
      if len(text) > 0:
        dataset = json.loads(text)
  else:
    ic("kaboom, loadData dosent work.")
    ic("Run SteamDBInstall to fix.")
    ic("Likely missing file.")
    return



  
  connection = sqlite3.connect("MissionSQL.db")
  cursor = connection.cursor()
  #create tables
  tables(cursor)
  
  ## this was already in kaggle so I just grabbed it saves alot of time lol
  ## there is some extra data in here but for now I just want to get this working tonight
                                      ## and establish some relational data at the least.

  for app in dataset:
    appID = app                                         # AppID, unique identifier for each app (string).
    game = dataset[app]             

    name = game['name']                                 # Game name (string).
    releaseDate = game['release_date']                  # Release date (string).
    estimatedOwners = game['estimated_owners']          # Estimated owners (string, e.g.: "0 - 20000").
    peakCCU = game['peak_ccu']                          # Number of concurrent users, yesterday (int).
    required_age = game['required_age']                 # Age required to play, 0 if it is for all audiences (int).
    price = game['price']                               # Price in USD, 0.0 if its free (float).
    dlcCount = game['dlc_count']                        # Number of DLCs, 0 if you have none (int).
    longDesc = game['detailed_description']             # Detailed description of the game (string).
    shortDesc = game['short_description']               # Brief description of the game,
    languages = game['supported_languages']             # Comma-separated enumeration of supporting languages.
    fullAudioLanguages = game['full_audio_languages']   # Comma-separated enumeration of languages with audio support.
    reviews = game['reviews']                           #
    headerImage = game['header_image']                  # Header image URL in the store (string).
    website = game['website']                           # Game website (string).
    supportWeb = game['support_url']                    # Game support URL (string).
    supportEmail = game['support_email']                # Game support email (string).
    supportWindows = game['windows']                    # Does it support Windows? (bool).
    supportMac = game['mac']                            # Does it support Mac? (bool).
    supportLinux = game['linux']                        # Does it support Linux? (bool).
    metacriticScore = game['metacritic_score']          # Metacritic score, 0 if it has none (int).
    userScore = game['user_score']                      # Users score, 0 if it has none (int).
    positive = game['positive']                         # Positive votes (int).
    negative = game['negative']                         # Negative votes (int).
    scoreRank = game['score_rank']                      # Score rank of the game based on user reviews (string).
    achievements = game['achievements']                 # Number of achievements, 0 if it has none (int).
    recommens = game['recommendations']                 # User recommendations, 0 if it has none (int).
    averagePlaytime = game['average_playtime_forever']  # Average playtime since March 2009, in minutes (int).
    medianPlaytime = game['median_playtime_forever']    # Median playtime since March 2009, in minutes (int).
    cursor.execute('''
        INSERT OR IGNORE INTO games
          (appid, name, release_date, price, positive, negative, metacritic_score,
          peak_ccu, required_age, dlc_count, achievements, recommendations,
          average_playtime, median_playtime)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (appID, name, releaseDate, price, positive, negative, metacriticScore,
          peakCCU, required_age, dlcCount, achievements, recommens,
          averagePlaytime, medianPlaytime))
        ## this line cursor.ex is the one that actually inserts the data into tables.

    packages = game['packages']                         # Available packages.
    for pack in packages:           
      title = pack['title']                             # Package title (string).
      packDesc = pack['description']                    # Package description (string).

      subs = pack['subs']                               # Subpackages.
      for sub in subs:            
        text = sub['text']                              # Subpackage title (string).
        subDesc = sub['description']                    # Subpackage description (string).
        subPrice = sub['price']                         # Subpackage price in USD (float).

    developers = game['developers']                     # Game developers.
    for developer in developers:            
      developerName = developer                         # Developer name (string).

    publishers = game['publishers']                     # Game publishers.
    for publisher in publishers:            
      publisherName = publisher                         # Publisher name (string).

    categories = game['categories']                     # Game categories.
    for category in categories:           
      categoryName = category                           # Category name (string).

    genres = game['genres']                             # Game genres.
    for gender in genres:           
      genderName = gender                               # Gender name (string).
      cursor.execute('INSERT INTO genres (appid, genre) VALUES (?, ?)', (appID, genderName))

    tags = game['tags']                                 # Tags.
    for tag in tags:           
      tagKey = tag                                      # Tag key (string, int).

    ## developers
    for developer in developers:
        cursor.execute('INSERT OR IGNORE INTO developers (appid, developer) VALUES (?, ?)', 
                      (appID, developer))

    ## publishers  
    for publisher in publishers:
        cursor.execute('INSERT OR IGNORE INTO publishers (appid, publisher) VALUES (?, ?)', 
                      (appID, publisher))

    ## categories
    for category in categories:
        cursor.execute('INSERT OR IGNORE INTO categories (appid, category) VALUES (?, ?)', 
                      (appID, category))

    ## platform support
    cursor.execute('''
        INSERT OR IGNORE INTO platform_support (appid, windows, mac, linux)
        VALUES (?, ?, ?, ?)
    ''', (appID, supportWindows, supportMac, supportLinux))
    

  connection.commit() ## saves the changes made
  connection.close()
  print("Dataset was added to Database.")

if __name__ == "__main__":
  loadData()