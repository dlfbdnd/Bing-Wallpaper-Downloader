#  !!!	Requirement: python3
#	Fully tested under Debian and Windows 10
User_Specified_Output_Folder = "BingWallpapers/"
#	Iterate through days
whatday = 0-int(input("Enter day offset (-1 for yesterday, 0 for today, etc. Between -7 to 1: "))
#	Import modules
import os,datetime,re,calendar,urllib.request,shutil
#	Print starting message
print("------Process Started------")
#	Function to find out "Month" and "Day" value
def findmonthday():
	global Year, Month, Day
	now = datetime.datetime.now()
	todaydate = datetime.date(now.year, now.month, now.day)
	DayDelta = datetime.timedelta(days=whatday)
	DayDate = str(todaydate - DayDelta)
	DayDateApply = re.split("-", DayDate)
	Year = DayDateApply[0]
	Month = int(DayDateApply[1])
	Month = str(calendar.month_abbr[(Month)])
	Day = DayDateApply[2]
	if len(Day) == 1:
		Day = "0" + Day
#	Import wallpaper url xml
urlBing = "https://www.bing.com/HPImageArchive.aspx?format=xml&idx=" + str(whatday) + "&n=1&mkt=zh-CN"
print("Getting URL")
responseBing = urllib.request.urlopen(urlBing)
dataBing = responseBing.read()
textBing = dataBing.decode('utf-8')
html = textBing
#	Extract wallpaper url (https)
a = html.find("<urlBase>")
b = html.find("</urlBase>")
Wallpaper = ""
for i in range(a+9,b):
	Wallpaper = Wallpaper+html[i]
WallpaperURL = "https://www.bing.com" + Wallpaper + "_1920x1200.jpg"
#	Download using shell
print("Downloading")
#	Try if it works (some only have 1920x1080 reso), if not, try the 1920x1080 reso version.
try:	
	FileName = re.split("/", Wallpaper)
	FileName = (FileName[-1] + "_1920x1200.jpg")
	urllib.request.urlretrieve(WallpaperURL, FileName)
except:
	try:
		findmonthday()
		print("Error: Bing.com may not have the 1920x1200 version of the picture on " + Month + "." + Day + ", trying fetching the 1920x1080 version")
		WallpaperURL = "https://www.bing.com" + Wallpaper + "_1920x1080.jpg"
		FileName = re.split("/", Wallpaper)
		FileName = (FileName[-1] + "_1920x1080.jpg")
		urllib.request.urlretrieve(WallpaperURL, FileName)
	except:
		print("File does not exist on Bing.com server, script is terminated")
		exit()
#os.system("axel " + WallpaperURL + "> /dev/null")
#	Rename to the date of the day
findmonthday()
ToFileName = (Month + Day + ".jpg")
shutil.move(FileName, ToFileName)
print("Renamed to: " + ToFileName)
#	Sort file into user specified folder (ends with "/")
print("Sorting file based on date")
NewDirectory = User_Specified_Output_Folder + Month + Year + "/"
if not os.path.exists(NewDirectory):
	os.makedirs(NewDirectory)
#	Try moving file, if exist, delete existing file then move
try:
	shutil.move(ToFileName, NewDirectory)
except:
	os.remove(NewDirectory + ToFileName)
	shutil.move(ToFileName, NewDirectory)
print("Done.")
