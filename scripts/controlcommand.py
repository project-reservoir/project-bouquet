from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'sunfid': '1',
	'valveid': '1',
    'twat': '4000',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
print(res['created'])

res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])

es.indices.refresh(index="test-index")