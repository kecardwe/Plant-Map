(
    @echo off
    echo NetID/UserName
    whoami

    echo Hostname/SerialNumber
    hostname
    wmic bios get serialnumber

    wmic computersystem get manufacturer


    wmic computersystem get model

    echo IP Information
    ipconfig /all

    echo Tanium
    tasklist /fi "ImageName eq TaniumClient.exe" /fo csv 2>NUL | find /I "TaniumClient.exe">NUL
    if "%ERRORLEVEL%"=="0" echo Program is running
    echo ----------------------------------------------
)
>>output.txt

