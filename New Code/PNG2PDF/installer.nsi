OutFile "PNG-to-PDF-INSTALLER.exe"

; The name of the installer
Name "Convert PNG to PDF"

; The default installation directory
InstallDir $PROGRAMFILES\PNGtoPDF

; The text to prompt the user to enter a directory
DirText "This will install Convert PNG to PDF on your computer. Choose a directory"

;--------------------------------

; The stuff to install
Section "" ;No components page, name is not important

; Set output path to the installation directory.
SetOutPath $INSTDIR

; Put file there
File ConvertPNGtoPDF.exe
WriteUninstaller "$INSTDIR\uninstall.exe"
CreateShortCut "$SMPROGRAMS\Convert PNG to PDF.lnk" "$INSTDIR\ConvertPNGtoPDF.exe"

SectionEnd ; end the section

Section "Uninstall"
Delete $INSTDIR\uninstaller.exe
Delete $INSTDIR\ConvertPNGtoPDF.exe
Delete "$SMPROGRAMS\Convert PNG to PDF.lnk"

SectionEnd