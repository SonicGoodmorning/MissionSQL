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
