@echo off
chcp 65001 >nul
echo ============================================
echo   Building ALL Lab Slides (Beamer 16:9)
echo   CSI403 Full Stack Development
echo ============================================
echo.

:: Check if pdflatex exists
where pdflatex >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] pdflatex not found!
    echo Please install MiKTeX first: https://miktex.org/download
    pause
    exit /b 1
)

:: Create output directory
if not exist "pdf" mkdir pdf

echo Building all 8 labs...
echo.

:: Build each lab
for %%i in (1 2 3 4 5 6 7 8) do (
    echo [%%i/8] Building lab0%%i.tex...
    pdflatex -interaction=nonstopmode lab0%%i.tex >nul 2>&1
    if exist lab0%%i.pdf (
        move /y lab0%%i.pdf pdf\ >nul
        echo       OK - lab0%%i.pdf
    ) else (
        echo       FAILED - lab0%%i.pdf
    )
)

:: Clean auxiliary files
echo.
echo Cleaning temporary files...
del /q *.aux *.log *.toc *.out *.nav *.snm *.vrb 2>nul

echo.
echo ============================================
echo   DONE! All PDFs are in 'pdf' folder
echo ============================================
echo.
dir pdf\*.pdf
echo.
pause
