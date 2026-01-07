@echo off
echo Installing required MiKTeX packages...
echo.

mpm --install=fancyhdr
mpm --install=tcolorbox
mpm --install=enumitem
mpm --install=titlesec
mpm --install=booktabs
mpm --install=listings
mpm --install=xcolor
mpm --install=hyperref
mpm --install=environ
mpm --install=pgf
mpm --install=etoolbox

echo.
echo Done! Now run build-lab.bat
pause
