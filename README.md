# RacPy

Библиотека на языке Python, которая позволяет взаимодействовать с сервером администрирования 1С через утилиту RAC, предоставляя соответствующие сущности.

## Сущности

### Клиент

Клиент необходим, чтобы указать путь до утилиты RAC и создать сессию подключения.

```python
from racpy.client import Client

client = Client(rac_cli_path="C:\\rac.exe")
```

### Сессия

Сессия необходима для создания уникального соединения с сервером и выполнения запросов. Можно создавать сразу несколько сессий для взаимодействия с разными серверами.

```python
from racpy.client import Client
from racpy.session import Session

client = Client(rac_cli_path="C:\\rac.exe")
session = Session(host="server", port=1545, client=client)
local_session = Session(host="localhost", port=1545, client=client)
```

### Агент

Класс агента предоставляет статические методы для взаимодействия с сервером в режиме администрирования агента кластера.

```python
from racpy.client import Client
from racpy.session import Session
from racpy.cmd.agent import Agent

client = Client(rac_cli_path="C:\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

print(Agent.version(session=session))
# 8.3.24.1667
```

### Администратор агента кластера

Класс администратора агента кластера предоставляет статические методы для взаимодействия с сервером в режиме управления администраторами агента кластера.

```python
from racpy.client import Client
from racpy.session import Session
from racpy.cmd.agent import AgentAdmin

client = Client(rac_cli_path="C:\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Создание нового администратора (без существующих в системе)
AgentAdmin.create(session=session, name="Admin")

# Получение списка администраторов (с указанием авторизации)
agent_admins = AgentAdmin.list(session=session, agent_user="Admin")

# Удаление ранее созданного администратора (с указанием авторизации)
AgentAdmin.remove(session=session, name="Admin", agent_user="Admin")
```

### Кластер

Класс кластера предоставляет статические методы для взаимодействия с сервером в режиме администрирования кластеров.

```python
from racpy.client import Client
from racpy.session import Session
from racpy.cmd.cluster import Cluster

client = Client(rac_cli_path="C:\\rac.exe")
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

### Информационная база

Класс информационной базы предоставляет статические методы для взаимодействия с информационными базами.

```python
from racpy.client import Client
from racpy.session import Session
from racpy.cmd.cluster import Cluster
from racpy.cmd.infobase import Infobase

client = Client(rac_cli_path="C:\\rac.exe")
session = Session(host="localhost", port=1545, client=client)

# Получаем UUID первого кластера сервера
cluster_id = Cluster.list(session=session)[0]["cluster"]

# Создание новой информационной базы в кластере с возвратом её UUID
infobase_id = Infobase.create(
    session=session,
    cluster_uuid=cluster["cluster"],
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

# Получение списка информационных баз
infobases = Infobase.list(session=session, cluster_uuid=cluster_id)

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
