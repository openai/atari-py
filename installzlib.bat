@echo off

:: Configuration
set VERSION=1.2.11
set FILE=zlib-%VERSION%.zip
set DIR=zlib-%VERSION%
set URL=https://zlib.net/zlib%VERSION:.=%.zip

echo [0/6] Library(zlib==%VERSION%)

:: Ancient Windows don't support TLS 1.1 and 1.2, so we fall back to insecure download.
set Version=
for /f "skip=1" %%v in ('wmic os get version') do if not defined Version set Version=%%v
for /f "delims=. tokens=1-3" %%a in ("%Version%") do (
  set Version.Major=%%a
  set Version.Minor=%%b
  set Version.Build=%%c
)

SET ORIGIN=%cd%
call :joinpath "%ORIGIN%" "install.log"
SET LOG_FILE=%Result%

:: Cleaning up previous mess
del /Q %FILE% ! >nul 2>&1
rd /S /Q %DIR% >nul 2>&1
del /Q %LOG_FILE% ! >nul 2>&1
copy /y nul %LOG_FILE% >nul 2>&1

echo|set /p="[1/6] Downloading... "
echo Fetching %URL% >>%LOG_FILE% 2>&1
powershell -Command "(New-Object Net.WebClient).DownloadFile('%URL%', '%FILE%')" >>%LOG_FILE% 2>&1
if %ERRORLEVEL% NEQ 0 (echo FAILED. && echo Log can be found at %LOG_FILE%. && exit /B 1) else (echo done.)

echo|set /p="[2/6] Extracting... "
powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::ExtractToDirectory('%FILE%', '.'); }"
if %ERRORLEVEL% NEQ 0 (echo FAILED. && echo Log can be found at %LOG_FILE%. && exit /B 1) else (echo done.)

cd %DIR%

echo|set /p="[3/6] Fixing CMakeLists.txt... "
set OLDSTR=RUNTIME DESTINATION ""\${INSTALL_BIN_DIR}\""
set NEWSTR=RUNTIME DESTINATION ""bin\""
call :search_replace "%OLDSTR%" "%NEWSTR%"

set OLDSTR=ARCHIVE DESTINATION ""\${INSTALL_LIB_DIR}\""
set NEWSTR=ARCHIVE DESTINATION ""lib\""
call :search_replace "%OLDSTR%" "%NEWSTR%"

set OLDSTR=LIBRARY DESTINATION ""\${INSTALL_LIB_DIR}\""
set NEWSTR=LIBRARY DESTINATION ""lib\""
call :search_replace "%OLDSTR%" "%NEWSTR%"

set OLDSTR=DESTINATION ""\${INSTALL_INC_DIR}\""
set NEWSTR=DESTINATION ""include\""
call :search_replace "%OLDSTR%" "%NEWSTR%"
if %ERRORLEVEL% NEQ 0 (echo FAILED. && echo Log can be found at %LOG_FILE%. && exit /B 1) else (echo done.)

mkdir build && cd build

echo|set /p="[4/6] Configuring... "
cmake .. -G "NMake Makefiles" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="%programfiles%\zlib" >>%LOG_FILE% 2>&1
if %ERRORLEVEL% NEQ 0 (echo FAILED. && echo Log can be found at %LOG_FILE%. && exit /B 1) else (echo done.)

echo|set /p="[5/6] Compiling... "
nmake >>%LOG_FILE% 2>&1
if %ERRORLEVEL% NEQ 0 (echo FAILED. && echo Log can be found at %LOG_FILE%. && exit /B 1) else (echo done.)

echo|set /p="[6/6] Installing... "
nmake install >>%LOG_FILE% 2>&1
set PATH=%PATH%;%programfiles%\zlib\bin
if %ERRORLEVEL% NEQ 0 (echo FAILED. && echo Log can be found at %LOG_FILE%. && exit /B 1) else (echo done.)

cd %ORIGIN% >nul 2>&1
del /Q %FILE% >nul 2>&1
rd /S /Q %DIR% >nul 2>&1

echo Details can be found at %LOG_FILE%.

@echo on
@goto :eof

:joinpath
set Path1=%~1
set Path2=%~2
if {%Path1:~-1,1%}=={\} (set Result=%Path1%%Path2%) else (set Result=%Path1%\%Path2%)
goto :eof

:search_replace
set OLDSTR=%~1
set NEWSTR=%~2
set CMD="(gc CMakeLists.txt) -replace '%OLDSTR%', '%NEWSTR%' | Out-File -encoding ASCII CMakeLists.txt"
powershell -Command %CMD%  >>%LOG_FILE% 2>&1
