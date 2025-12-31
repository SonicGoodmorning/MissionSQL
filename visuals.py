import matplotlib.pyplot as plt
import seaborn as sb
from icecream import ic

def priceVqual(df):
    sb.set_theme(style='darkgrid')
    plt.figure(figsize=(12, 6))

    sb.regplot(data=df, x ='price', y = 'avg_reviews',
               line_kws={'color': 'red', 'alpha': 0.7},
               scatter_kws={'alpha': .5, 'color': 'teal'})
    plt.title("Does Higher Price mean a Better Game?", fontsize = 16, fontweight='bold')
    plt.xlabel('Price USD$', fontsize = 12)
    plt.ylabel('Avg Review Rating', fontsize=12)
    plt.tight_layout()
    plt.savefig('PricesVQuality', dpi = 300, bbox_inches='tight')
    ic("PriceVsQuality chart created")

def genre(df):
    sb.set_theme(style='darkgrid')
    plt.figure(figsize=(14, 8))
    topGenres = df.head(15)

    colors = sb.color_palette('viridis', len(topGenres))
    bars = plt.barh(topGenres['genre'], topGenres['review_ratio'], color=colors)

    plt.xlabel('Average Review Ratio', fontsize=12)
    plt.title('Top 15 Game Genres by Average Review Ratio', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('TopGenres.png', dpi=300, bbox_inches='tight')
    ic("Genre chart created")

def devQual(df):
    sb.set_theme(style='whitegrid')
    plt.figure(figsize=(14, 8))
    topDevs = df.head(20)

    colors = sb.color_palette('rocket', len(topDevs))
    bars = plt.barh(topDevs['developer'], topDevs['avg_positive_reviews'], color=colors)

    plt.xlabel('Average Positive Reviews', fontsize=12)
    plt.title('Top 20 Developers by Average Positive Reviews', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('TopDevelopers.png', dpi=300, bbox_inches='tight')
    ic("Developer chart created")

def platformData(df):
    sb.set_theme(style='whitegrid')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    col1 = sb.color_palette('coolwarm', len(df))
    ax1.bar(range(len(df)), df['avg_positive_reviews'], color=col1)
    ax1.set_xticks(range(len(df)))
    ax1.set_xticklabels(df['platform_support'], rotation=45, ha='right')
    ax1.set_ylabel('Average Positive Reviews', fontsize=12)
    ax1.set_title('Average Positive Reviews by Platform Support', fontsize=16, fontweight='bold')

    for i, row in df.iterrows():
        ax1.text(i, row['avg_positive_reviews'] + 50, f"{row['avg_positive_reviews']:.1f}", ha='center', fontsize=9)
    
    col2 = sb.color_palette('viridis', len(df))
    ax2.bar(range(len(df)), df['avg_price'], color=col2)
    ax2.set_xticks(range(len(df)))
    ax2.set_xticklabels(df['platform_support'], rotation=45, ha='right')
    ax2.set_ylabel('Average Price (USD$)', fontsize=12)
    ax2.set_title('Average Price by Platform Support', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.savefig('PlatformSupport.png', dpi=300, bbox_inches='tight')
    ic("Platform Support chart created")
