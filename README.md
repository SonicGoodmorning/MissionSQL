# Steam Games Analysis

Data analysis project exploring pricing strategies and review patterns across 85,000+ Steam games using SQL and Python.

## Overview

This project analyzes the Steam games dataset to answer questions about game pricing, genre popularity, developer quality, and platform support. I built a normalized relational database and performed statistical analysis to uncover trends in the gaming industry.

## Key Findings

- **Price vs Quality**: Moderate positive correlation (r = 0.34) between game price and review ratings
- **Best Genres**: Indie and simulation genres show the highest review ratios
- **Platform Support**: Cross-platform games (Windows + Mac + Linux) receive 15% more positive reviews on average
- **Top Developers**: Analysis reveals which developers consistently produce highly-rated games

## Tech Stack

- **Python** - Data processing and analysis
- **SQLite** - Relational database with 6 normalized tables
- **Pandas** - Statistical analysis and data manipulation
- **Matplotlib & Seaborn** - Data visualization
- **Kaggle API** - Dataset acquisition

## Database Schema

The database uses a normalized relational structure:

- `games` - Core game information (price, reviews, metadata)
- `genres` - Game genre classifications (many-to-many)
- `developers` - Developer information (many-to-many)
- `publishers` - Publisher data (many-to-many)
- `categories` - Game categories (many-to-many)
- `platform_support` - OS compatibility (one-to-one)

## Project Structure

```
├── main.py              # Database creation and ETL pipeline
├── trends.py            # Statistical analysis queries
├── visuals.py           # Chart generation
├── SteamDBInstall.py    # Dataset download script
└── MissionSQL.db        # SQLite database (generated)
```

## Running the Project

1. Install dependencies:
```bash
pip install pandas matplotlib seaborn kagglehub icecream
```

2. Download the dataset:
```bash
python SteamDBInstall.py
```

3. Build the database:
```bash
python main.py
```

4. Run analysis and generate charts:
```bash
python trends.py
```

## Analyses Performed

### 1. Price vs Quality Analysis
Examines the relationship between game pricing and review scores. Filters out free-to-play games and outliers to get accurate correlation data.

### 2. Genre Analysis
Identifies which game genres receive the best reviews and analyzes average pricing by genre. Only includes genres with 100+ games for statistical significance.

### 3. Developer Analysis
Ranks top developers by average positive review count, filtering for developers with at least 3 published games and 100+ total reviews.

### 4. Platform Support Analysis
Compares review performance and pricing across different platform support combinations (Windows, Mac, Linux).

## Sample Visualizations

The project generates four high-quality charts:
- `PricesVQuality.png` - Price vs review quality scatter plot with regression line
- `TopGenres.png` - Top 15 genres by review ratio
- `TopDevelopers.png` - Top 20 developers by average reviews
- `PlatformSupport.png` - Platform support impact on reviews and pricing

## What I Learned

- Database normalization and foreign key relationships
- Complex SQL queries with joins and aggregations
- Statistical analysis with pandas
- Data visualization best practices
- Working with large datasets (85K+ records)

## Future Improvements

- Add time-series analysis for release date trends
- Implement achievement and DLC correlation analysis
- Create interactive dashboard with Streamlit
- Add more advanced statistical tests

## Dataset

Data sourced from [Steam Games Dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) on Kaggle.

---

**Note**: This project was built as part of my data analysis portfolio to demonstrate SQL, Python, and data visualization skills.
