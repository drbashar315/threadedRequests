
"""
Use the following endpoint:
https://clarksonmsda.org/api/get_product.php?pid=12
Create a Github repo called threadedRequests and a Python file called main.py.
Create a multi threaded script which
Iterates over pid 0-200 and fetches the json.  The requests.get call should be in its own thread.
Consider missing ids
Saves each product to a json text file named pid_xxxx.json .
Finally create a script called combine.py which iterates over the resulting json files and
 generates a single csv of all products with the following fields:

prod_id,prod_sku,prod_cat,prod_name

USING threading library muliple thread API calling
"""

import requests
import threading
import time
import json


def worker(tid, n):
    url = "https://clarksonmsda.org/api/get_product.php?pid="
    url = url + str(n)
    rq = requests.get(url)
    data = json.loads(rq.text)
    if data['data'] is not None:
        # for k, v in data['data'].items():
        #     print("key:"+k+", value:"+str(v))
        productdictionary = {
            "prod_id":      data['data']['prod_id'],
            "prod_sku":     data['data']['prod_sku'],
            "prod_cat":     data['data']['prod_cat'],
            "prod_name":    data['data']['prod_name']
        }
        outfilename = "./out/pid_" + str(n).rjust(4, '0') + ".json"
        # print(productdictionary)
        with open(outfilename, "w") as outfile:
            json.dump(productdictionary, outfile)


n = 0
tid = 0
tidlist = []  
start = time.time()
while tid < 200:
    # thread pool slot open -  create a new thread
    w = threading.Thread(name='tid_'+str(tid),
                         target=worker, args=(tid, n,))
    w.start()
    tidlist.append(w)
    tid += 1
    n += 1
# print(tidlist)

for t in tidlist:
    t.join()
print(tidlist)
print(time.time() - start)
