import gevent
import urllib.request
from gevent import monkey


monkey.patch_all()


def downloader(img_url, img_name):
    """download image"""
    req = urllib.request.urlopen(img_url)
    image_content = req.read()
    with open(img_name, "rb") as f:
        f.write(image_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "http://img5.imgtn.bdimg.com/it/u=4214941395,707510718&fm=26&gp=0.jpg", "1.jpg"),
        gevent.spawn(downloader, "http://img5.imgtn.bdimg.com/it/u=4214941395,707510718&fm=26&gp=0.jpg", "2.jpg")
    ])


if __name__ == "__main__":
    main()