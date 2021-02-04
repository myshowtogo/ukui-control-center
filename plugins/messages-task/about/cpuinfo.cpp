#include <QFile>
#include <QDebug>

#include "cpuinfo.h"

cpuinfo::cpuinfo(QObject *parent) : QObject(parent)
{

}

QString cpuinfo::getCpuName()
{
    QString name = "";
#ifdef Q_OS_LINUX
    QFile file("/proc/cpuinfo");
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return "no cpuinfo";

    QString line = "N/A";
    QTextStream in(&file);
    line = in.readLine();
    while (!in.atEnd()) {
        line = in.readLine();
        if (line.contains("model name"))
            break;
    }
    //openEuler /proc/cpuinfo
    //model name	: Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
    name = QString(line).right(line.length() - (line.indexOf(":") + 2));
#elif defined(Q_OS_FREEBSD)

#endif
    return name;
}
