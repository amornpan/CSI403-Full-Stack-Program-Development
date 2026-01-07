@echo off
chcp 65001 >nul
echo ============================================
echo   Lab Video Generator
echo   Full-Stack RAG Course
echo ============================================
echo.

:: Check conda
where conda >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Conda not found!
    echo Please run from Anaconda Prompt
    pause
    exit /b 1
)

:: Activate environment
call conda activate video-generator
if %errorlevel% neq 0 (
    echo [ERROR] Cannot activate video-generator environment
    echo Please create it first:
    echo   conda env create -f environment.yml
    pause
    exit /b 1
)

:: Menu
echo Select option:
echo   [1] Build Lab 01 video
echo   [2] Build Lab 02 video
echo   [3] Build Lab 03 video
echo   [4] Build Lab 04 video
echo   [5] Build Lab 05 video
echo   [6] Build Lab 06 video
echo   [7] Build Lab 07 video
echo   [8] Build Lab 08 video
echo   [9] Build ALL lab videos
echo   [0] Exit
echo.
set /p choice="Enter choice (0-9): "

if "%choice%"=="1" goto lab1
if "%choice%"=="2" goto lab2
if "%choice%"=="3" goto lab3
if "%choice%"=="4" goto lab4
if "%choice%"=="5" goto lab5
if "%choice%"=="6" goto lab6
if "%choice%"=="7" goto lab7
if "%choice%"=="8" goto lab8
if "%choice%"=="9" goto all
if "%choice%"=="0" goto end
goto end

:lab1
echo Building Lab 01 video...
copy pdf\lab01.pdf . >nul 2>&1
python video_lab01.py
goto cleanup

:lab2
echo Building Lab 02 video...
copy pdf\lab02.pdf . >nul 2>&1
python video_lab02.py
goto cleanup

:lab3
echo Building Lab 03 video...
copy pdf\lab03.pdf . >nul 2>&1
python video_lab03.py
goto cleanup

:lab4
echo Building Lab 04 video...
copy pdf\lab04.pdf . >nul 2>&1
python video_lab04.py
goto cleanup

:lab5
echo Building Lab 05 video...
copy pdf\lab05.pdf . >nul 2>&1
python video_lab05.py
goto cleanup

:lab6
echo Building Lab 06 video...
copy pdf\lab06.pdf . >nul 2>&1
python video_lab06.py
goto cleanup

:lab7
echo Building Lab 07 video...
copy pdf\lab07.pdf . >nul 2>&1
python video_lab07.py
goto cleanup

:lab8
echo Building Lab 08 video...
copy pdf\lab08.pdf . >nul 2>&1
python video_lab08.py
goto cleanup

:all
echo Building ALL lab videos...
for %%i in (1 2 3 4 5 6 7 8) do (
    echo.
    echo ========== Lab 0%%i ==========
    copy pdf\lab0%%i.pdf . >nul 2>&1
    python video_lab0%%i.py
)
goto cleanup

:cleanup
echo.
echo Cleaning up...
del /q lab*.pdf 2>nul
if not exist "videos" mkdir videos
move /y *.mp4 videos\ >nul 2>&1
echo.
echo ============================================
echo   Done! Videos are in 'videos' folder
echo ============================================

:end
pause
