#ifndef CPUINFO_H
#define CPUINFO_H

#include <QObject>

class cpuinfo : public QObject
{
    Q_OBJECT
public:
    explicit cpuinfo(QObject *parent = nullptr);

    static QString getCpuName();
};

#endif // CPUINFO_H
