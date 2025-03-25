# RacPy [В разработке]

Библиотека на языке Python, которая позволяет взаимодействовать с сервером администрирования 1С через утилиту RAC, предоставляя соответствующие сущности.

## Установка

```bash
pip install git+https://github.com/bqio/racpy.git
```

## TODO

- rule module
- profile module
- counter module
- limit module

## Сущности

### Клиент

Клиент необходим, чтобы указать путь до утилиты RAC и создать сессию подключения. Можно создавать сразу несколько клиентов для взаимодействия с разными утилитами RAC.

```python
from racpy import Client

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
linux_client = Client(rac_cli_path="/opt/1cv8/x86_64/<version>/rac")
```

### Сессия

Сессия необходима для создания уникального соединения с сервером администрирования и выполнения запросов. Можно создавать сразу несколько сессий для взаимодействия с разными серверами.

```python
from racpy import Client, Session

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="server", port=1545, client=client)
local_session = Session(host="localhost", port=1545, client=client)
```

### Агент

Класс агента предоставляет статические методы для взаимодействия с сервером администрирования в режиме агента кластера.

```python
from racpy import Client, Session, Agent

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получение версии агента
Agent.version(session=session)
```

### Администратор агента кластера

Класс администратора агента кластера предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления администраторами агента кластера.

```python
from racpy import Client, Session, AgentAdmin

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Создание нового администратора (без существующих в системе)
AgentAdmin.create(session=session, name="Admin")

# Получение списка администраторов (с указанием авторизации)
agent_admins = AgentAdmin.list(session=session, agent_user="Admin")

# Удаление ранее созданного администратора (с указанием авторизации)
AgentAdmin.remove(session=session, name="Admin", agent_user="Admin")
```

### Кластер

Класс кластера предоставляет статические методы для взаимодействия с сервером администрирования в режиме кластера.

```python
from racpy import Client, Session, Cluster

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

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
from racpy import Client, Session, Cluster, ClusterAdmin

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получение UUID первого кластера (.firstid() эквивалентен Cluster.first()["cluster"])
cluster_id = Cluster.firstid(session=session)

# Получение списка администраторов кластера
cluster_admins = ClusterAdmin.list(session=session, cluster_uuid=cluster_id)

# Создание нового администратора кластера
ClusterAdmin.create(session=session, cluster_uuid=cluster_id, name="Admin", pwd="Admin")

# Удаление администратора кластера (с указанием авторизации)
ClusterAdmin.remove(
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

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получение UUID первого кластера (.first() эквивалентен Cluster.list()[0])
cluster_id = Cluster.first(session=session)["cluster"]

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

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получение UUID первого кластера (.firstid() эквивалентен Cluster.first()["cluster"])
cluster_id = Cluster.firstid(session=session)

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

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получение UUID первого кластера
cluster_id = Cluster.firstid(session=session)

# Получение UUID первого рабочего сервера кластера
server_id = Server.firstid(session=session, cluster_uuid=cluster_id)

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

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получение необходимых UUID
cluster_id = Cluster.firstid(session=session)
server_id = Server.firstid(session=session, cluster_uuid=cluster_id)
process_id = Process.firstid(
    session=session, cluster_uuid=cluster_id, server_uuid=server_id
)
infobase_id = Infobase.firstid(session=session, cluster_uuid=cluster_id)

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

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получение необходимых UUID
cluster_id = Cluster.firstid(session=session)
infobase_id = Infobase.firstid(session=session, cluster_uuid=cluster_id)

# Получение активных сеансов в информационной базе
active_user_sessions = UserSession.list(
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

# Уничтожаем активный сеанс
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

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получение UUID первого кластера
cluster_id = Cluster.firstid(session=session)

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

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получение UUID первого кластера
cluster_id = Cluster.firstid(session=session)

# Получение списка сервисов
services = Service.list(session=session, cluster_uuid=cluster_id)
```

### Блокировки

Класс блокировок предоставляет статические методы для взаимодействия с сервером администрирования в режиме управления блокировками.

```python
from racpy import Client, Session, Cluster, Server, Process, Infobase, Connection, UserSession, Lock

client = Client(rac_cli_path="C:\\Program Files\\1cv8\\<version>\\bin\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получение необходимых UUID
cluster_id = Cluster.firstid(session=session)
server_id = Server.firstid(session=session, cluster_uuid=cluster_id)
process_id = Process.firstid(
    session=session, cluster_uuid=cluster_id, server_uuid=server_id
)
infobase_id = Infobase.firstid(session=session, cluster_uuid=cluster_id)
connection_id = Connection.firstid(
    session=session,
    cluster_uuid=cluster_id,
    process_uuid=process_id,
    infobase_uuid=infobase_id,
    infobase_user="admin",
    infobase_pwd="password",
)
user_session_id = UserSession.firstid(
    session=session, cluster_uuid=cluster_id, infobase_uuid=infobase_id
)

# Получение списка блокировок
locks = Lock.list(
    session=session,
    cluster_uuid=cluster_id,
    infobase_uuid=infobase_id,
    connection_uuid=connection_id,
    user_session_uuid=user_session_id,
)
```
