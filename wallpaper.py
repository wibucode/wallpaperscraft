import requests, os
from bs4 import BeautifulSoup as bs
global cari, page
def masal():
	cari = raw_input("\033[93mPilih Genre	: \033[97m")
	page = raw_input("\033[93mNo halaman	: \033[97m")
	os.system("clear")
	url = "https://wallpaperscraft.com/search/?order=&page="+page+"&query="+cari
	r = requests.get(url)
	soup = bs(r.text, "html.parser")
	div = soup.find_all(class_="wallpapers__image")
	for tag in div:
		link = tag.get("src")
		link = link.replace("_300x168.jpg", "_1280x720.jpg")
		name = link.replace("https://images.wallpaperscraft.com/image/", "")
		lis = name.replace("_1280x720.jpg", "")
		download = requests.get(link)
		f = open(name, "wb")
		f.write(download.content)
		f.close()
		print "\033[91mDownload\033[97m "+lis

pass
os.system("clear")
print """
\033[93mWallpaperScraft \033[97mMassal Downloader
-------------------------------------
Author	: WibuCode
Github	: https://github.com/wibucode

\033[93m[ All Genre ]\n
\033[93m[ ] \033[97m3D, 60 Favorites
\033[93m[A] \033[97mAbstract, Animals, Anime, Art\033[97m
\033[93m[B] \033[97mBlack\033[97m
\033[93m[C] \033[97mCars, City\033[97m
\033[93m[D] \033[97mDark\033[97m
\033[93m[F] \033[97mFantasy, Flowers, Food\033[97m
\033[93m[H] \033[97mHolidays\033[97m
\033[93m[L] \033[97mLove\033[97m
\033[93m[M] \033[97mMacro, Minimalism, Motorcycles, Music\033[97m
\033[93m[N] \033[97mNature\033[97m
\033[93m[O] \033[97mOther\033[97m
\033[93m[S] \033[97mSmilies, Space, Sport\033[97m
\033[93m[T] \033[97mTechnologies, Textures\033[97m
\033[93m[V] \033[97mVectors\033[97m
\033[93m[W] \033[97mWords\033[97m
"""
masal()

