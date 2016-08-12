@echo off

set BUILDDIR=build

@echo ............... INSTALLING THONNY ...................................
%BUILDDIR%\Scripts\pip install --pre --no-cache-dir thonny

@echo ............... CREATING INSTALLER ..........................
set /p VERSION=<%BUILDDIR%\Lib\site-packages\thonny\VERSION
"C:\Program Files (x86)\Inno Setup 5\iscc" /dAppVer=%VERSION% /dSourceFolder=build inno_setup.iss > installer_building.log


pause