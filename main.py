
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

"""

import requests
import json


n = 0
while n < 200:
    url = "https://clarksonmsda.org/api/get_product.php?pid="
    url = url + str(n)
    r = requests.get(url)

    data = json.loads(r.text)
    if data['data'] is not None:
        # for k, v in data['data'].items():
        #     print("key:"+k+", value:"+str(v))
        dictionary = {
            "prod_id":      data['data']['prod_id'],
            "prod_sku":     data['data']['prod_sku'],
            "prod_cat":     data['data']['prod_cat'],
            "prod_name":    data['data']['prod_name']
        }
        outfilename = "./out/output_" + str(n).rjust(3, '0') + ".json"
        # print(dictionary)
        with open(outfilename, "w") as outfile:
            json.dump(dictionary, outfile)
    n += 1
