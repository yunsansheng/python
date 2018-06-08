@echo off 
adb pull /sdcard/temp.png screenshot
adb shell rm /sdcard/temp.png
exit