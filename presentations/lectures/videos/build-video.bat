@echo off
chcp 65001 >nul
echo ============================================
echo   Lecture Video Generator
echo   Full-Stack RAG with Local LLM
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
    echo Please create it first from C:\Users\Asus\test\video-generator:
    echo   conda env create -f environment.yml
    pause
    exit /b 1
)

:: Menu
echo Select option:
echo   [1] Build Week 01 video (Intro to RAG)
echo   [2] Build Week 02 video (Git + Python)
echo   [3] Build Week 03 video (Docker + OpenSearch)
echo   [4] Build Week 04 video (FastAPI)
echo   [5] Build Week 05 video (OpenSearch Integration)
echo   [6] Build Week 06 video (Embeddings)
echo   [7] Build Week 07 video (RAG + LLM + Streamlit)
echo   [8] Build Week 08 video (Docker Compose)
echo   [9] Build Week 09 video (CI/CD)
echo   [A] Build ALL lecture videos
echo   [0] Exit
echo.
set /p choice="Enter choice (0-9, A): "

if "%choice%"=="1" goto week1
if "%choice%"=="2" goto week2
if "%choice%"=="3" goto week3
if "%choice%"=="4" goto week4
if "%choice%"=="5" goto week5
if "%choice%"=="6" goto week6
if "%choice%"=="7" goto week7
if "%choice%"=="8" goto week8
if "%choice%"=="9" goto week9
if "%choice%"=="A" goto all
if "%choice%"=="a" goto all
if "%choice%"=="0" goto end
goto end

:week1
echo Building Week 01 video...
copy ..\week01\week01-intro-rag.pdf . >nul 2>&1
python video_week01.py
goto cleanup

:week2
echo Building Week 02 video...
copy ..\week02\week02-git-python.pdf . >nul 2>&1
python video_week02.py
goto cleanup

:week3
echo Building Week 03 video...
copy ..\week03\week03-docker-opensearch.pdf . >nul 2>&1
python video_week03.py
goto cleanup

:week4
echo Building Week 04 video...
copy ..\week04\week04-fastapi.pdf . >nul 2>&1
python video_week04.py
goto cleanup

:week5
echo Building Week 05 video...
copy ..\week05\week05-opensearch.pdf . >nul 2>&1
python video_week05.py
goto cleanup

:week6
echo Building Week 06 video...
copy ..\week06\week06-embeddings.pdf . >nul 2>&1
python video_week06.py
goto cleanup

:week7
echo Building Week 07 video...
copy ..\week07\week07-rag-llm-streamlit.pdf . >nul 2>&1
python video_week07.py
goto cleanup

:week8
echo Building Week 08 video...
copy ..\week08\week08-docker-compose.pdf . >nul 2>&1
python video_week08.py
goto cleanup

:week9
echo Building Week 09 video...
copy ..\week09\week09-cicd.pdf . >nul 2>&1
python video_week09.py
goto cleanup

:all
echo Building ALL lecture videos...
echo.

echo ========== Week 01 ==========
copy ..\week01\week01-intro-rag.pdf . >nul 2>&1
python video_week01.py

echo ========== Week 02 ==========
copy ..\week02\week02-git-python.pdf . >nul 2>&1
python video_week02.py

echo ========== Week 03 ==========
copy ..\week03\week03-docker-opensearch.pdf . >nul 2>&1
python video_week03.py

echo ========== Week 04 ==========
copy ..\week04\week04-fastapi.pdf . >nul 2>&1
python video_week04.py

echo ========== Week 05 ==========
copy ..\week05\week05-opensearch.pdf . >nul 2>&1
python video_week05.py

echo ========== Week 06 ==========
copy ..\week06\week06-embeddings.pdf . >nul 2>&1
python video_week06.py

echo ========== Week 07 ==========
copy ..\week07\week07-rag-llm-streamlit.pdf . >nul 2>&1
python video_week07.py

echo ========== Week 08 ==========
copy ..\week08\week08-docker-compose.pdf . >nul 2>&1
python video_week08.py

echo ========== Week 09 ==========
copy ..\week09\week09-cicd.pdf . >nul 2>&1
python video_week09.py

goto cleanup

:cleanup
echo.
echo Cleaning up...
del /q week*.pdf 2>nul
echo.
echo ============================================
echo   Done! Videos are in current folder
echo ============================================
echo.
dir *.mp4 2>nul
echo.

:end
pause
