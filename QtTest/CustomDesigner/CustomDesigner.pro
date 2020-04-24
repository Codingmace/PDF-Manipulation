CONFIG      += plugin debug_and_release
TARGET      = $$qtLibraryTarget(file1plugin)
TEMPLATE    = lib

HEADERS     = file1plugin.h
SOURCES     = file1plugin.cpp
RESOURCES   = icons.qrc
LIBS        += -L. 

greaterThan(QT_MAJOR_VERSION, 4) {
    QT += designer
} else {
    CONFIG += designer
}

target.path = $$[QT_INSTALL_PLUGINS]/designer
INSTALLS    += target

include(file1.pri)
