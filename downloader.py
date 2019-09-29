# download image

'''import requests

img_data = requests.get('https://miro.medium.com/max/3000/1*25Le7KoMK_z6BIaM8x74RA.png').content
with open('download.png', 'wb+') as f:
    f.write(img_data)

print('-----------done-----------')'''


# download youtube video
'''
import requests

img_data = requests.get('https://r1---sn-ci5gup-qxay.googlevideo.com/videoplayback?expire=1569794321&ei=sdSQXcH6IuuGz7sP_MC-mAw&ip=223.225.5.21&id=o-AOZC634xbbK4MX3VtZN0FtZsBa8QZqS18Xveq_oAtjwv&itag=22&source=youtube&requiressl=yes&mm=31%2C26&mn=sn-ci5gup-qxay%2Csn-cvh76ned&ms=au%2Conr&mv=m&mvi=0&pl=22&initcwndbps=117500&mime=video%2Fmp4&ratebypass=yes&dur=30.185&lmt=1471134525575106&mt=1569772643&fvip=1&fexp=23842630&c=WEB&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRgIhAMVfl5Zm9mY9SI7-ubpQGaGxi9l3t52BRHx9PLnDoMbqAiEAmUUEBwLGiBbtVcsDvZI6aX8vENSiUaUthnVd6qcLznU%3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHylml4wRQIhAL43EiYZmh6Q7f0CAiUndw_sqTvS-A06wYXRByvazyxuAiBcXEGuN0C8Hbjsj7l8y0FPFmasw-hVwOqE_HqRT7wIAQ%3D%3D').content
with open('download.mp4', 'wb+') as f:
    f.write(img_data)

print('-----------done-----------')
'''

# instagram image
'''
In instagaram I observed using ctrl+shift+i(inspect element) that images of various size are available at different link.
Simply grab the link of desired size image.
'''
import requests

img_data = requests.get('https://instagram.fdel1-4.fna.fbcdn.net/vp/0437481456ffff4576b3b4b8babaf27b/5E24179E/t51.2885-15/e35/p1080x1080/69401100_131789854824180_5881880053535315488_n.jpg?_nc_ht=instagram.fdel1-4.fna.fbcdn.net&amp;_nc_cat=100').content
with open('insta.jpg', 'wb+') as f:
    f.write(img_data)

print('-----------done-----------')