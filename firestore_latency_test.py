import numpy as np
import os
import timer

from google.cloud import firestore
import google.oauth2.credentials

credentials = google.oauth2.credentials.Credentials(os.getenv('TOKEN'))
db = firestore.Client(credentials=credentials, project=os.getenv('PROJECT_ID'))

transaction = db.transaction()
city_ref = db.collection(u'cities').document(u'9nVWHXAvZtb0du50uVj5')

@firestore.transactional
def transactional_get(transaction, city_ref):
    city_ref.get(transaction=transaction)

def plain_get(city_ref):
    city_ref.get()

def perf_test():
  t = timer.Timer()
  limit = 100
  n = 0
  while n < limit:
    n += 1
    with t:
      transactional_get(transaction, city_ref)
  print('method,type,avg(ms),p99(ms)')
  print(f'get,transactional,{round(t.elapsed / limit * 1000)},{round(np.percentile(t.stages, 99) * 1000)}')

  t2 = timer.Timer()
  n = 0
  while n < limit:
    n += 1
    with t2:
      plain_get(city_ref)
  print(f'get,nontransactional,{round(t2.elapsed / limit * 1000)},{round(np.percentile(t2.stages, 99) * 1000)}')

perf_test()

