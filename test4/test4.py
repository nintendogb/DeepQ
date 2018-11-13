from flickrapi import FlickrAPI
from pprint import pprint
from datetime import date, timedelta

def listResultURL(res):
    photos = res['photos']['photo']
    picCount = len(photos)
    for i in range(picCount):
        item = photos[i]
        if 'url_o' in item:
            print(item['url_o'])
        else:
            print(item)
    print('')
    print('')
    print('')

#Det user_id by > https://www.webpagefx.com/tools/idgettr/
USER_LIST = ['143523379@N06', '10817753@N03' , '8893545@N06']
FLICKR_PUBLIC = 'PUBLIC'
FLICKR_SECRET = 'SECRET'
today = date.today().strftime('%Y-%m-%d %H:%M:%S')
twoDaysAgo = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')
flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
extras='url_o'


res = flickr.photos.search(text='Portrait', per_page=1000, extras=extras, min_upload_date = twoDaysAgo, max_upload_date = today)
print('Portry Result:')
listResultURL(res)


res = flickr.photos.search(text='Only one face', per_page=1000, extras=extras, min_upload_date = twoDaysAgo, max_upload_date = today)
print('Only one face Result:')
listResultURL(res)


for id in USER_LIST:
    print('ID is {}'.format(id))
    res = flickr.photos.search(user_id=id, per_page=10, extras=extras, min_upload_date = twoDaysAgo, max_upload_date = today)
    print('ID:{} Result:'.format(id))
    listResultURL(res)

res = flickr.photos.search(text='Full face picture', per_page=1000, extras=extras, min_upload_date = twoDaysAgo, max_upload_date = today)
print('Full face picture Result:')
listResultURL(res)