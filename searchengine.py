import os
from googleapiclient.discovery import build

api_key = 'redacted'
cse_id = 'redacted'

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

if __name__ == '__main__':
    search = input("Search for something here: ")
    print()
    print("""
Results
==================================================================================================================================
""")
    print()
    results = google_search(search, api_key, cse_id)
    for result in results:
        print(result['title'])
        print(result['link'])
        print()
    print()
