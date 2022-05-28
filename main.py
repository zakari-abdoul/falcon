import json
import random
import falcon
from quotes import quotes


class QuotesRessource:
    def on_get(self,req,res):
        quote = {
            'quote': random.choice(quotes),
            'author':'the Buddha'
        }
        res.body = json.dumps(quote)

#create the falcon application
api = falcon.API()
api.add_route('/quote',QuotesRessource())