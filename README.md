# RacPy

Библиотека на языке Python, которая позволяет взаимодействовать с сервером администрирования 1С через утилиту RAC, предоставляя соответствующие сущности.

## Установка

```bash
# Установка master ветки репозитория
pip install git+https://github.com/bqio/racpy.git

# Установка определенной ветки репозитория
pip install git+https://github.com/bqio/racpy.git@8.3.27.1688
```

## API

https://bqio.github.io/racpy/

## Примеры

Получение списка кластеров.

```python
import racpy as rc

client = rc.Client("/opt/1cv8/x86_64/<version>/rac")
session = rc.Session(client)

print(rc.Cluster.list(session))
```

Получение списка информационных баз кластера.

```python
import racpy as rc

client = rc.Client("/opt/1cv8/x86_64/<version>/rac")
session = rc.Session(client)
cluster = rc.Cluster.list(session)[0]["cluster"]

print(rc.Infobase.Summary.list(session, cluster))
```

Создание информационной базы.

```python
import racpy as rc

client = rc.Client("/opt/1cv8/x86_64/<version>/rac")
session = rc.Session(client)
cluster = rc.Cluster.list(session)[0]["cluster"]

infobase = rc.Infobase.create(
    session, cluster, "Тестовая база", "PostgreSQL", "localhost", "TestIB", "ru_RU"
)

print(infobase)
```
