import sqlite3
import pandas as pd
from icecream import ic

def data():
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

def correlation(df):

    correlation = df['price'].corr(df['avg_reviews'])
    ## calculate the correlation between the avg review and price
    ## basically finding out if higher price means better reviews.

    if correlation > .5:
        ic("Higher Priced games are rated higher.")
    elif correlation > .1:
        ic("Higher Prices help game ratings slightly")
    else:
        ic("No correlation found between price and quality of game")
    ic(correlation)
    

df = data() # establish data frame through func
ic("Data Ready") 

ic(df.head()) # print out the head of df for simplicity.

correlation(df)