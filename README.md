Requirements: python3

As the description says, it downloads background pictures from Bing.com.
It is simple to use, just download the .py file and run it in Python 3 (E.g. $ "python3 Bing_Wallpaper_Downloader.py")
Once started, the singular version prompts for user input as day offset (to download the current Bing background, enter 0; for yesterday's, enter -1; range is between -7 and 1), while the batch version downloads all available pictures on the day from Bing.com.

The script uses HTTPS connection, and download speed may vary from one location to another.
If there are problems with the modules (let's say some modules are missing, run $ "pip3 install os datetime re calendar urllib")

Ehh... there's one last thing, the language code is currently set to "zh-CN", if you are want the pictures from other locations, 
change that to any of the following: 
(I got this from the Internet, and some may give you the same pictures.)
format: mkt=<Language Code>-<Country Code>
List of <Language Code>: https://www.w3schools.com/tags/ref_language_codes.asp
List of <Country Code>: https://www.w3schools.com/tags/ref_country_codes.asp
(E.g. English + UNITED KINGDOM = "mkt=en-GB") (E.g. Russian + RUSSIAN FEDERATION = "mkt=ru-RU")

If you have any questions or suggestions, please contact me through email.    :D
