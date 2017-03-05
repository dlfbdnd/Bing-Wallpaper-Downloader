#  !!!	Requirements: python3, axel under Linux distributions (apt-get install python3 axel)
#	Fully tested under Debian.
User_Specified_Output_Folder = "~/Desktop/Bing\ Wallpapers/"
#	Prompt user input for offset, or automatically download all within reach; n is counter for auto-mode. If you want to prompt for offset, uncomment the row below (row 4) and comment row 5 to 8, then delete 1 indent starting from row 9.
#whatday = 0-int(input("Enter day offset (-1 for yesterday, 0 for today, etc. Between -7 to 1: "))
n = 0
for whatday in range(-7, 2):
	n += 1
	whatday = 0-int(whatday)
	#	Import modules
	import os,datetime,re,calendar,urllib.request
	#	Print starting message
	print("------Wallpaper " + str(n) + "/9 ------")
	#	Import wallpaper url xml
	urlBing = "https://www.bing.com/HPImageArchive.aspx?format=xml&idx=" + str(whatday) + "&n=1&mkt=zh-CN"
	print("Getting URL...")
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
	WallpaperURL = "https://www.bing.com" + Wallpaper + "_1920x1080.jpg"
	#	Download using shell
	print("Downloading...")
	os.system("axel " + WallpaperURL + "> /dev/null")
	#	Rename to the date of the day
	now = datetime.datetime.now()
	FileName = re.split("/", Wallpaper)
	FileName = (FileName[-1] + "_1920x1080.jpg")
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
	ToFileName = (Month + Day + ".jpg")
	os.system("mv " + FileName + " " + ToFileName)
	print("Renamed to: " + ToFileName)
	#	Sort file into user specified folder (ends with "/")
	print("Sorting file based on date...")
	os.system("mkdir -p " + User_Specified_Output_Folder + Month + "_" + Year + "/")
	os.system("mv " + ToFileName + " " + User_Specified_Output_Folder + Month + "_" + Year + "/")
	print("Done.")
