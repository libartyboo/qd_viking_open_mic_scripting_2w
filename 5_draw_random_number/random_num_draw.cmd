@echo off
:: EXECUTE BATCH FILE AND GET THE NUMBER

:: Following are the steps to execute a batch file:
::    Step 1 − Open the command prompt (cmd.exe)
::    Step 2 − Go to the location where the .cmd file is stored (use 'cd' command)
::				example:
::				> cd Desktop\files
::    Step 3 − Write the name of the file and press the Enter button to execute the batch file

set /a RAND_NUM=(%random%*1000/32768)+1
echo %RAND_NUM%