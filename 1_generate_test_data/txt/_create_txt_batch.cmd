@echo off
set date_marker=%date:~-4%%date:~7,2%%date:~4,2%-%time:~0,2%%time:~3,2%%time:~6,2%
echo text_%date_marker%.txt > test_%date_marker%_cmd_.txt
echo done