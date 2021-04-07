import requests

p = requests.get('https://avatars.mds.yandex.net/get-zen_gallery/3129491/pub_606c0fb67e1f3129bb854764_606c10034328d67e5f0e548e/scale_1200')
out = open('IMG\img.jpg', 'wb')
out.write(p.content)
out.close()