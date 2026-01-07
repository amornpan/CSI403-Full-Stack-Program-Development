@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ============================================
echo   LaTeX Lab Slides Builder (Beamer 16:9)
echo   CSI403 Full Stack Development
echo ============================================
echo.

:: Check if pdflatex exists
where pdflatex >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] pdflatex not found!
    echo Please install MiKTeX or TeX Live first.
    echo.
    echo Download MiKTeX: https://miktex.org/download
    pause
    exit /b 1
)

:: Create output directory
if not exist "pdf" mkdir pdf

:: Menu
echo Select option:
echo   [1] Build ALL labs (lab01-08)
echo   [2] Build individual lab
echo   [3] Build labs_all.tex (document version)
echo   [4] Clean auxiliary files
echo   [0] Exit
echo.
set /p choice="Enter choice (0-4): "

if "%choice%"=="1" goto build_all_labs
if "%choice%"=="2" goto build_individual
if "%choice%"=="3" goto build_document
if "%choice%"=="4" goto clean
if "%choice%"=="0" goto end
goto menu_error

:build_all_labs
echo.
echo [INFO] Building all lab slides...
echo.

for %%i in (1 2 3 4 5 6 7 8) do (
    echo Building lab0%%i.tex...
    pdflatex -interaction=nonstopmode lab0%%i.tex >nul 2>&1
    if exist lab0%%i.pdf (
        move /y lab0%%i.pdf pdf\ >nul
        echo   [OK] lab0%%i.pdf
    ) else (
        echo   [FAIL] lab0%%i.pdf
        pdflatex -interaction=nonstopmode lab0%%i.tex
    )
)

echo.
echo [SUCCESS] All slides built!
goto cleanup_aux

:build_individual
echo.
echo Select lab to build:
echo   [1] Lab 1 - Git + Python
echo   [2] Lab 2 - Docker + OpenSearch
echo   [3] Lab 3 - FastAPI
echo   [4] Lab 4 - OpenSearch Integration
echo   [5] Lab 5 - Embeddings
echo   [6] Lab 6 - RAG + LLM + Streamlit
echo   [7] Lab 7 - Docker Compose
echo   [8] Lab 8 - CI/CD + Testing
echo   [0] Back to main menu
echo.
set /p labnum="Enter lab number (0-8): "

if "%labnum%"=="0" goto end
if "%labnum%" gtr "8" goto invalid_lab
if "%labnum%" lss "1" goto invalid_lab

set labfile=lab0%labnum%.tex
echo.
echo [INFO] Building %labfile%...
pdflatex -interaction=nonstopmode %labfile%

set pdfname=lab0%labnum%.pdf
if exist %pdfname% (
    move /y %pdfname% pdf\ >nul
    echo.
    echo [SUCCESS] %pdfname% created in pdf folder!
) else (
    echo [ERROR] Failed to create PDF
)
goto cleanup_aux

:invalid_lab
echo [ERROR] Invalid lab number!
goto build_individual

:build_document
echo.
echo [INFO] Building labs_all.tex (document version)...
pdflatex -interaction=nonstopmode labs_all.tex
pdflatex -interaction=nonstopmode labs_all.tex
if exist labs_all.pdf (
    move /y labs_all.pdf pdf\ >nul
    echo [SUCCESS] labs_all.pdf created!
) else (
    echo [ERROR] Failed to create PDF
)
goto cleanup_aux

:clean
echo.
echo [INFO] Cleaning auxiliary files...
del /q *.aux *.log *.toc *.out *.fls *.fdb_latexmk *.synctex.gz *.nav *.snm *.vrb 2>nul
echo [SUCCESS] Cleaned!
goto end

:cleanup_aux
echo.
echo [INFO] Cleaning auxiliary files...
del /q *.aux *.log *.toc *.out *.fls *.fdb_latexmk *.synctex.gz *.nav *.snm *.vrb 2>nul
goto end

:menu_error
echo [ERROR] Invalid choice!
goto end

:end
echo.
echo ============================================
echo   Done! PDF files are in 'pdf' folder
echo ============================================
pause
