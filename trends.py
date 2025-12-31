import sqlite3
import pandas as pd
from icecream import ic
import visuals

def priceVqualData():
    connection = sqlite3.connect("MissionSQL.db") ## establish the connection to db

    query ='''
    SELECT price, AVG(positive) as avg_reviews, COUNT(*) as game_count
    FROM games
    WHERE price > 0
    GROUP BY price
    HAVING game_count > 5 
    ORDER BY price ASC
    '''

    ## excluding ftp games due to alot of them not being popular enough causing
    ## skewed results.
    ## gamecount > 5 is just to make this more simple and eliminate games
    ## that are inflated in price to avoid skewing the results.

    df = pd.read_sql_query(query, connection)
    ## Goes through each data point, and queries.
    connection.close()
    return df

def GenreData():
    ##Which genres have the best review ratings + price points
    connection = sqlite3.connect("MissionSQL.db")

    query ='''
    SELECT g.genre,
           COUNT(*) as game_count,
           AVG(gm.price) as avg_price,
           AVG(gm.positive) as avg_positive_reviews,
           AVG(gm.negative) as avg_negative_reviews,
           AVG(CAST(gm.positive AS FLOAT) / (gm.positive + gm.negative)) as review_ratio
    FROM genres g
    JOIN games gm ON g.appid = gm.appid
    WHERE gm.positive + gm.negative > 0
    GROUP BY g.genre
    HAVING game_count > 100
    ORDER BY review_ratio DESC
    '''
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df



def devQualData():
    ## Devs with the best average game quality 
    connection = sqlite3.connect("MissionSQL.db")

    query ='''
    SELECT d.developer,
           COUNT(*) as game_count,
           AVG(g.positive) as avg_positive_reviews,
           AVG(g.price) as avg_price,
           AVG(g.metacritic_score) as avg_metacritic
    FROM developers d
    JOIN games g ON d.appid = g.appid
    WHERE g.positive + g.negative > 100
    GROUP BY d.developer
    HAVING game_count >= 3
    ORDER BY avg_positive_reviews DESC
    LIMIT 20
    '''

    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

def platformData():
    ## How does platform avaliblity effect review performance
    connection = sqlite3.connect("MissionSQL.db")
    query ='''
    SELECT
        CASE
            WHEN p.windows AND p.mac AND p.linux THEN 'All Platforms'
            WHEN p.windows AND p.mac THEN 'Windows + Mac'
            WHEN p.windows AND p.linux THEN 'Windows + Linux'
            WHEN p.mac AND p.linux THEN 'Mac + Linux'
            WHEN p.windows THEN 'Windows Only'
            WHEN p.mac THEN 'Mac Only'
            WHEN p.linux THEN 'Linux Only'
        END as platform_support,
        COUNT(*) as game_count,
        AVG(g.positive) as avg_positive_reviews,
        AVG(g.price) as avg_price
    FROM platform_support p
    JOIN games g ON p.appid = g.appid
    WHERE g.positive + g.negative > 50
    GROUP BY platform_support
    ORDER BY avg_positive_reviews DESC
    '''
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

def correlation(df):

    correlation = df['price'].corr(df['avg_reviews'])
    ## calculate the correlation between the avg review and price
    ## basically finding out if higher price means better reviews.

    if correlation > .5:
        ic("Higher Priced games are rated higher.")
    elif correlation > .3:
        ic("Higher Prices have moderate effect on game ratings")
    elif correlation > .1:
        ic("Higher Prices help game ratings slightly")
    else:
        ic("No correlation found between price and quality of game")
    bestReviews = df.nlargest(10, 'avg_reviews')
    ic(bestReviews)
    ic(correlation)
    



def main():
    ## run all the funcs here
    PQdf = priceVqualData() # Price vs Quality DataFrame
    ic(PQdf.head()) # print head of dataframe
    correlation(PQdf)
    visuals.priceVqual(PQdf)

    GenreDf = GenreData() # Genre DataFrame
    ic(GenreDf.head()) # print head of dataframe

    DevDf = devQualData() # dev DataFrame
    ic(DevDf.head()) # print head of dataframe

    PlatformDf = platformData() # Platform DataFrame
    ic(PlatformDf) # print head of dataframe

if __name__ == "__main__":
    main()

    

