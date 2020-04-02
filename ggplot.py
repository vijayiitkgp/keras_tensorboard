import ggplot
from ggplot import aes, meat, geom_line, stat_smooth

ggplot(aes(x='date', y='beef'), data=meat) +\
    geom_line() +\
    stat_smooth(colour='blue', span=0.2)
    
''' ggplot(diamonds, aes(x='carat', y='price', color='cut')) +\
    geom_point() +\
    scale_color_brewer(type='diverging', palette=4) +\
    xlab("Carats") + ylab("Price") + ggtitle("Diamonds")
    
ggplot(diamonds, aes(x='price', fill='cut')) +\
    geom_density(alpha=0.25) +\
    facet_wrap("clarity") '''