import pandas as pd
import numpy as np

# create an indeces list from 1 to 1000
idx_list = list(range(1,1001))
# assign the extent values
xmin, xmax, ymin, ymax = -119.5, -88.9, 34.8, 43.0
# create a random numpy list of longitudes within xmin <> xmax range
x_list = (xmax - xmin) * np.random.random(1000) + xmin
# create a random numpy list of latitudes within ymin <> ymax range
y_list = (ymax - ymin) * np.random.random(1000) + ymin

# create a dataframe with the index list and the two numpy arrays
random_pd = pd.DataFrame({'id':idx_list,'x':x_list,'y':y_list})
# store the file as csv
random_pd.to_csv('./xys.csv', index=False)
   
