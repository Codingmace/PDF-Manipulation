#include "file1.h"
#include "file1plugin.h"

#include <QtPlugin>

File1Plugin::File1Plugin(QObject *parent)
    : QObject(parent)
{
    m_initialized = false;
}

void File1Plugin::initialize(QDesignerFormEditorInterface * /* core */)
{
    if (m_initialized)
        return;

    // Add extension registrations, etc. here

    m_initialized = true;
}

bool File1Plugin::isInitialized() const
{
    return m_initialized;
}

QWidget *File1Plugin::createWidget(QWidget *parent)
{
    return new File1(parent);
}

QString File1Plugin::name() const
{
    return QLatin1String("File1");
}

QString File1Plugin::group() const
{
    return QLatin1String("");
}

QIcon File1Plugin::icon() const
{
    return QIcon();
}

QString File1Plugin::toolTip() const
{
    return QLatin1String("");
}

QString File1Plugin::whatsThis() const
{
    return QLatin1String("");
}

bool File1Plugin::isContainer() const
{
    return false;
}

QString File1Plugin::domXml() const
{
    return QLatin1String("<widget class=\"File1\" name=\"file1\">\n</widget>\n");
}

QString File1Plugin::includeFile() const
{
    return QLatin1String("file1.h");
}
#if QT_VERSION < 0x050000
Q_EXPORT_PLUGIN2(file1plugin, File1Plugin)
#endif // QT_VERSION < 0x050000
