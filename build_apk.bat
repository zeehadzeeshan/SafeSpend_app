@echo off
cd /d "%~dp0"
echo Working Directory: %CD%

echo.
echo --- Installing Dependencies ---
call npm install
if %ERRORLEVEL% NEQ 0 (
    echo [Error] npm install failed.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo --- Syncing Capacitor ---
call npx cap sync
if %ERRORLEVEL% NEQ 0 (
    echo [Error] Capacitor sync failed.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo --- Building APK (Release) ---
cd android
if %ERRORLEVEL% NEQ 0 (
    echo [Error] Could not find android directory.
    pause
    exit /b %ERRORLEVEL%
)

call .\gradlew.bat clean assembleRelease
if %ERRORLEVEL% NEQ 0 (
    echo [Error] Gradle build failed.
    cd ..
    pause
    exit /b %ERRORLEVEL%
)

cd ..
echo.
echo --- Build Successful! ---
echo APK Location: %~dp0android\app\build\outputs\apk\release\app-release-unsigned.apk
pause
