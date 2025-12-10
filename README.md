# RacPy 8.3.27.1688

Библиотека на языке Python, которая позволяет взаимодействовать с сервером администрирования 1С через утилиту RAC, предоставляя соответствующие сущности.

## Установка

```bash
pip install git+https://github.com/bqio/racpy.git@8.3.27.1688
```

## TODO

- service-setting module
- binary-data-storage module

### Клиент

Клиент необходим, чтобы указать путь до утилиты RAC и создать сессию подключения. Можно создавать сразу несколько клиентов для взаимодействия с разными утилитами RAC.

```python
from racpy import Client

client = Client("C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
linux_client = Client("/opt/1cv8/x86_64/<version>/rac")
```

### Сессия

Сессия необходима для создания уникального соединения с сервером администрирования и выполнения запросов. Можно создавать сразу несколько сессий для взаимодействия с разными серверами.

```python
from racpy import Client, Session

client = Client("C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
# По умолчанию host=localhost, port=1545
localhost_session = Session(client)
# Произвольный хост
session = Session(client, "host")
# Произвольный хост и порт
local_session = Session(client, "host2", 1546)
```

В следующих примерах объявление клиента и сессии будет опускаться.

### Агент

Класс агента предоставляет статические методы для взаимодействия с сервером администрирования в режиме агента кластера.

```python
from racpy import Client, Session, Agent

...

# Получение версии агента
Agent.version(session=session)
```

### Администратор агента кластера

Класс администратора агента кластера предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления администраторами агента кластера.

```python
from racpy import Client, Session, Agent

...

# Создание нового администратора (без существующих в системе)
Agent.Admin.create(session=session, name="Admin")

# Получение списка администраторов (с указанием авторизации)
agent_admins = Agent.Admin.list(session=session, agent_user="Admin")

# Удаление ранее созданного администратора (с указанием авторизации)
Agent.Admin.remove(session=session, name="Admin", agent_user="Admin")
```

### Кластер

Класс кластера предоставляет статические методы для взаимодействия с сервером администрирования в режиме кластера.

```python
from racpy import Client, Session, Cluster

...

# Получение списка кластеров
cluster_list = Cluster.list(session=session)

# Создание нового кластера c возвратом его UUID
cluster_id = Cluster.create(session=session, host="Local Cluster", port=1541)

# Получение информации о ранее созданном кластере по его UUID
cluster_info = Cluster.info(session=session, cluster_uuid=cluster_id)

# Обновление информации кластера (в данном случае имени)
Cluster.update(
    session=session, cluster_uuid=cluster_id, name="Updated Local Cluster"
)

# Удаление кластера по его UUID
Cluster.remove(session=session, cluster_uuid=cluster_id)
```

### Администратор кластера

Класс администратора кластера предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления администраторами кластера.

```python
from racpy import Client, Session, Cluster

...

# Получение UUID первого кластера
cluster_id = Cluster.list(session=session)[0]["cluster"]

# Получение списка администраторов кластера
cluster_admins = Cluster.Admin.list(session=session, cluster_uuid=cluster_id)

# Создание нового администратора кластера
Cluster.Admin.create(session=session, cluster_uuid=cluster_id, name="Admin", pwd="Admin")

# Удаление администратора кластера (с указанием авторизации)
Cluster.Admin.remove(
    session=session,
    cluster_uuid=cluster_id,
    name="Admin",
    cluster_user="Admin",
    cluster_pwd="Admin",
)
```

### Информационная база

Класс информационной базы предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления информационнами базами.

```python
from racpy import Client, Session, Cluster, Infobase

...

# Получение UUID первого кластера
cluster_id = Cluster.list(session=session)[0]["cluster"]

# Получение списка информационных баз
infobases = Infobase.list(session=session, cluster_uuid=cluster_id)

# Создание новой информационной базы в кластере с возвратом её UUID
infobase_id = Infobase.create(
    session=session,
    cluster_uuid=cluster_id,
    name="Test IB",
    db_server="localhost",
    db_name="test_ib",
    locale="ru_RU",
    dbms="PostgreSQL",
    db_user="postgres",
    db_pwd="123",
)

# Получение полной информации информационной базы
infobase_info = Infobase.info(
    session=session, cluster_uuid=cluster_id, infobase_uuid=infobase_id
)

# Обновление информации информационной базы
Infobase.update(
    session=session,
    cluster_uuid=cluster_id,
    infobase_uuid=infobase_id,
    denied_message="Test",
)

# Удаление информационной базы
Infobase.remove(
    session=session,
    cluster_uuid=cluster_id,
    infobase_uuid=infobase_id,
    drop_database=True,
    clear_database=True,
)
```

### Рабочий сервер

Класс рабочего сервера предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления рабочими серверами кластера.

```python
from racpy import Client, Session, Cluster, Server

...

# Получение UUID первого кластера
cluster_id = Cluster.list(session=session)[0]["cluster"]

# Получение списока рабочих серверов кластера
servers = Server.list(session=session, cluster_uuid=cluster_id)

# Создание нового рабочего сервера и возвращение его UUID
server_id = Server.create(
    session=session,
    cluster_uuid=cluster_id,
    agent_host="host",
    agent_port=1541,
    port_range="1475:1476",
)

# Получение информации рабочего сервера
server_info = Server.info(
    session=session, cluster_uuid=cluster_id, server_uuid=server_id
)

# Обновление информации рабочего сервера
Server.update(
    session=session,
    cluster_uuid=cluster_id,
    server_uuid=server_id,
    connections_limit=512,
)

# Удаление рабочего сервера
Server.remove(session=session, cluster_uuid=cluster_id, server_uuid=server_id)
```

### Рабочий процесс

Класс рабочего процесса предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления рабочими процессами.

```python
from racpy import Client, Session, Cluster, Server, Process

...

# Получение UUID первого кластера
cluster_id = Cluster.list(session=session)[0]["cluster"]

# Получение UUID первого рабочего сервера кластера
server_id = Server.list(session=session, cluster_uuid=cluster_id)[0]["server"]

# Получение списка рабочих процессов
processes = Process.list(session=session, cluster_uuid=cluster_id, server_uuid=server_id)

# Получение информации рабочего процесса вместе с лицензиями
process_id = processes[0]["process"]
process_info = Process.info(
    session=session, cluster_uuid=cluster_id, process_uuid=process_id, licenses=True
)
```

### Соединения

Класс соединения предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления соединениями.

```python
from racpy import Client, Session, Cluster, Server, Infobase, Process, Connection

...

# Получение необходимых UUID
cluster_id = Cluster.list(session=session)[0]["cluster"]
server_id = Server.list(session=session, cluster_uuid=cluster_id)[0]["server"]
process_id = Process.list(
    session=session, cluster_uuid=cluster_id, server_uuid=server_id
)[0]["process"]
infobase_id = Infobase.list(session=session, cluster_uuid=cluster_id)[0]["infobase"]

# Получение списка соединений
connections = Connection.list(
    session=session,
    cluster_uuid=cluster_id,
    process_uuid=process_id,
    infobase_uuid=infobase_id,
)

# Получение информации соединения
connection_id = connections[0]["connection"]
connection_info = Connection.info(
    session=session, cluster_uuid=cluster_id, connection_uuid=connection_id
)

# Разрыв соединения
Connection.kill(
    session=session,
    cluster_uuid=cluster_id,
    process_uuid=process_id,
    connection_uuid=connection_id,
)
```

### Пользовательские сеансы

Класс пользовательских сеансов предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления активными пользовательскими сеансами.

```python
from racpy import Client, Session, Cluster, Infobase, UserSession

...

# Получение необходимых UUID
cluster_id = Cluster.list(session=session)[0]["cluster"]

# Получение активных сеансов сервера
active_user_sessions = UserSession.list(
    session=session, cluster_uuid=cluster_id
)

# Получение активных сеансов в информационной базе
infobase_id = Infobase.list(session=session, cluster_uuid=cluster_id)[0]["infobase"]
active_user_sessions_ib = UserSession.list(
    session=session, cluster_uuid=cluster_id, infobase_uuid=infobase_id
)

# Получение полной информации сеанса с указанием лицензий
user_session_id = active_user_sessions[0]["session"]
user_session_info = UserSession.info(
    session=session,
    cluster_uuid=cluster_id,
    user_session_uuid=user_session_id,
    licenses=True,
)

# Уничтожение активного сеанса
UserSession.kill(
    session=session,
    cluster_uuid=cluster_id,
    user_session_uuid=user_session_id,
    error_message="Bye",
)
```

### Менеджер кластера серверов

Класс менеджера кластера серверов предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления менеджерами кластера серверов.

```python
from racpy import Client, Session, Cluster, Manager

...

# Получение UUID первого кластера
cluster_id = Cluster.list(session=session)[0]["cluster"]

# Получение списка менеджеров
managers = Manager.list(session=session, cluster_uuid=cluster_id)

# Получение информации о менеджере по его UUID
manager_id = managers[0]["manager"]
manager_info = Manager.info(
    session=session, cluster_uuid=cluster_id, manager_uuid=manager_id
)
```

### Сервис менеджера кластера

Класс сервиса менеджера кластера предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления сервисами менеджера кластера.

```python
from racpy import Client, Session, Cluster, Service

...

# Получение UUID первого кластера
cluster_id = Cluster.list(session=session)[0]["cluster"]

# Получение списка сервисов
services = Service.list(session=session, cluster_uuid=cluster_id)
```

### Блокировки

Класс блокировок предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления блокировками.

```python
from racpy import Client, Session, Cluster, Server, Process, Infobase, Connection, UserSession, Lock

...

# Получение необходимых UUID
cluster_id = Cluster.list(session=session)[0]["cluster"]
server_id = Server.list(session=session, cluster_uuid=cluster_id)[0]["server"]
process_id = Process.list(
    session=session, cluster_uuid=cluster_id, server_uuid=server_id
)[0]["process"]
infobase_id = Infobase.list(session=session, cluster_uuid=cluster_id)[0]["infobase"]
connection_id = Connection.list(
    session=session,
    cluster_uuid=cluster_id,
    process_uuid=process_id,
    infobase_uuid=infobase_id,
    infobase_user="admin",
    infobase_pwd="password",
)[0]["connection"]
user_session_id = UserSession.list(
    session=session, cluster_uuid=cluster_id, infobase_uuid=infobase_id
)[0]["session"]

# Получение списка блокировок
locks = Lock.list(
    session=session,
    cluster_uuid=cluster_id,
    infobase_uuid=infobase_id,
    connection_uuid=connection_id,
    user_session_uuid=user_session_id,
)
```

### Счётчики потребления ресурсов

Данный класс предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления счётчиками потребления ресурсов.

```python
from racpy import Client, Session, Cluster, Counter

...

# Получение необходимых UUID
cluster_id = Cluster.list(session=session)[0]["cluster"]

# Получение списка счётчиков
counters = Counter.list(session=session, cluster_uuid=cluster_id)

# Создание или обновление счётчика
Counter.update(
    session=session,
    cluster_uuid=cluster_id,
    counter_name="test",
    collection_time=8,
    group="users",
    filter_type="all",
    filter="test",
    descr="test descr",
)

# Получение счётчика по имени
counter = Counter.info(session=session, cluster_uuid=cluster_id, counter_name="test")

# Очищение счётчика
Counter.clear(session=session, cluster_uuid=cluster_id, counter_name="test")

# Получение текущих значений счётчика
values = Counter.values(session=session, cluster_uuid=cluster_id, counter_name="test")

# Получение накопленных значений счётчика
accumulated_values = Counter.accumulated_values(
    session=session, cluster_uuid=cluster_id, counter_name="test"
)

# Удаление счётчика
Counter.remove(session=session, cluster_uuid=cluster_id, counter_name="test")
```

### Ограничения потребления ресурсов

Данный класс предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления ограничениями потребления ресурсов.

```python
from racpy import Client, Session, Cluster, Limit

...

# Получение необходимых UUID
cluster_id = Cluster.list(session=session)[0]["cluster"]

# Получение списка ограничений
limits = Limit.list(session=session, cluster_uuid=cluster_id)

# Создание или обновление ограничения
Limit.update(
    session=session,
    cluster_uuid=cluster_id,
    limit_name="test",
    action="set-low-priority-thread",
    counter_name="test",
)

# Получение ограничения по имени
limit = Limit.info(session=session, cluster_uuid=cluster_id, limit_name="test")

# Удаление ограничения
Limit.remove(session=session, cluster_uuid=cluster_id, limit_name="test")
```

### Требования назначения функциональности

Данный класс предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления требованиями назначения функциональности.

```python
from racpy import Client, Session, Cluster, Server, Rule

...

# Получение необходимых UUID
cluster_id = Cluster.list(session=session)[0]["cluster"]
server_id = Server.list(session=session, cluster_uuid=cluster_id)[0]["server"]

# Создание требования и возврат его UUID
rule_id = Rule.create(
    session=session, cluster_uuid=cluster_id, server_uuid=server_id, position=0
)

# Обновление требования
Rule.update(
    session=session,
    cluster_uuid=cluster_id,
    server_uuid=server_id,
    rule_uuid=rule_id,
    position=0,
    priority=1,
)

# Получение списка требований
Rule.list(session=session, cluster_uuid=cluster_id, server_uuid=server_id)

# Получение требования по UUID
Rule.info(
    session=session,
    cluster_uuid=cluster_id,
    server_uuid=server_id,
    rule_uuid=rule_id,
)

# Удаление требования
Rule.remove(
    session=session, cluster_uuid=cluster_id, server_uuid=server_id, rule_uuid=rule_id
)
```
