Requirements: python3, axel under Linux distributions (E.g. $ "apt-get install python3 axel" on Debian)
As the description says, it downloads background pictures from Bing.com.
It is simple to run, just download the .py file and run it in Python 3 (E.g. $ "python3 Bing_Wallpaper_Downloader.py")

The script uses HTTPS connection, and download speed may differ from one location to another.
If there are problems with the modules (let's say some modules are missing, run $ "pip3 install os datetime re calendar urllib")

By default, batch-download feature is enabled and will download all 9 pictures displayed on Bing.com.
You can also comment and uncomment rows to enable user-specified-download feature, which prompts for the day offset.
(Open the file for more detailed information on this topic.)

Ehh... there's one last thing, the language code is currently set to "zh-CN", if you are want the pictures from other locations, 
change that to any of the following: 
(I got this from the Internet, and some may give you the same pictures.)
format: mkt=<Language Code>-<Country Code>
List of <Language Code>: https://www.w3schools.com/tags/ref_language_codes.asp
List of <Country Code>: https://www.w3schools.com/tags/ref_country_codes.asp
(E.g. English + UNITED KINGDOM = "mkt=en-GB") (E.g. Russian + RUSSIAN FEDERATION = "mkt=ru-RU")

If you want more information, feel free to contact me. Though I do not check them often.  :P
