import io
import bson                       # this is installed with the pymongo package
import matplotlib.pyplot as plt
from skimage.data import imread   # or, whatever image library you prefer
import multiprocessing as mp      # will come in handy due to the size of the data

import pandas as pd
import numpy as np

# Simple data processing

data = bson.decode_file_iter(open('input/train_example.bson', 'rb'))

# 82 products
# 100 images



prod_to_category = dict()

counter = 0
for c, d in enumerate(data):
    product_id = d['_id']
    category_id = d['category_id'] # This won't be in Test data
    prod_to_category[product_id] = category_id
    
    counter+=1
    print ( str(counter) + " pic: " + str( product_id) + " " + str(category_id) )
    c = 0
    for e, pic in enumerate(d['imgs']):
        picture = imread(io.BytesIO(pic['picture']))
        #print ( picture.shape )
        plt.imshow(picture)
        plt.savefig( str(product_id)+ "_"+ str(c) + ".png")
        #print (picture)
        c+=1
    print (c)
    #break
    
        # do something with the picture, etc

prod_to_category = pd.DataFrame.from_dict(prod_to_category, orient='index')
prod_to_category.index.name = '_id'
prod_to_category.rename(columns={0: 'category_id'}, inplace=True)

print( prod_to_category.head() )

#0 1 73 to 76

#1000010653	TELEPHONIE - GPS	ACCESSOIRE TELEPHONE	COQUE TELEPHONE - BUMPER TELEPHONE
#1000004079	INFORMATIQUE	CONNECTIQUE - ALIMENTATION	CHARGEUR - ADAPTATEUR SECTEUR - ALLUME CIGARE - SOLAIRE
#1000004141	INFORMATIQUE	PROTECTION - PERSONNALISATION - SUPPORT	COQUE - HOUSSE
#1000015539	BRICOLAGE - OUTILLAGE - QUINCAILLERIE	SECURITE MAISON	ALARME AUTONOME



#plt.imshow(picture)
          
