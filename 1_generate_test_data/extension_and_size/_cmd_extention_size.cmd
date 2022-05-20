@echo off
set /p extention=Enter extention:  
set /p size=Enter size(MB):  
set /a size_kb=%size%*1048576
set /a _rand=(%random%*1000/32768) + 1
set file="cmd_%_rand%_%size%_.%extention%"
fsutil file createnew %file% %size_kb%
