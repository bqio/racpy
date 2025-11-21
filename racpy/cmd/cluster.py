from typing import List, Literal
from .command import Command, Arg
from ..session import Session
from ..handlers import to_list, to_dict
from ..utils import b2yn, list_to_dc, to_dc
from ..schemas import ClusterSchema, ClusterAdminSchema
from ..enums import AuthMethod, LoadBalancingMode, SecurityLevel


class Cluster:
    """Режим администрирования кластера серверов."""

    class Admin:
        """Управление администраторами кластера."""

        @staticmethod
        def list(
            session: Session,
            cluster: str,
            cluster_user: str | None = None,
            cluster_pwd: str | None = None,
        ) -> List[ClusterAdminSchema]:
            """
            Получение списка администраторов кластера.

            Args:
                session (Session): Уникальная сессия подключения.
                cluster (str): Идентификатор кластера серверов.
                cluster_user (str | None): Имя администратора кластера.
                cluster_pwd (str | None): Пароль администратора кластера.

            Returns:
                List[ClusterAdminSchema]: Список администраторов кластера.
            """
            admins = session.exec(
                Command(
                    Arg("cluster"),
                    Arg("admin"),
                    Arg(cluster, "--cluster={}"),
                    Arg(cluster_user, "--cluster-user={}"),
                    Arg(cluster_pwd, "--cluster-pwd={}"),
                    Arg("list"),
                ),
                to_list,
            )
            if admins is None or len(admins) == 0:
                return []
            return list_to_dc(admins, ClusterAdminSchema)

        @staticmethod
        def register(
            session: Session,
            cluster: str,
            name: str,
            auth: AuthMethod = AuthMethod.PWD,
            pwd: str | None = None,
            descr: str | None = None,
            os_user: str | None = None,
            agent_user: str | None = None,
            agent_pwd: str | None = None,
            cluster_user: str | None = None,
            cluster_pwd: str | None = None,
        ) -> None:
            """
            Добавление нового администратора кластера.

            Args:
                session (Session): Уникальная сессия подключения.
                cluster (str): Идентификатор кластера серверов.
                name (str): Имя администратора.
                auth (AuthMethod = AuthMethod.PWD): Способ аутентификации.
                    * `PWD` — аутентификация по паролю (поле `pwd` должно быть заполнено).
                    * `OS` — аутентификация через операционную систему (поле `pwd` игнорируется).
                pwd (str | None): Пароль администратора. Используется только если выбран способ аутентификации `PWD`.
                descr (str | None): Описание администратора.
                os_user (str | None): Имя пользователя операционной системы.
                agent_user (str | None): Имя администратора агента кластера.
                agent_pwd (str | None): Пароль администратора агента кластера.
                cluster_user (str | None): Имя администратора кластера.
                cluster_pwd (str | None): Пароль администратора кластера.
            """
            return session.exec(
                Command(
                    Arg("cluster"),
                    Arg("admin"),
                    Arg(cluster, "--cluster={}"),
                    Arg(cluster_user, "--cluster-user={}"),
                    Arg(cluster_pwd, "--cluster-pwd={}"),
                    Arg("register"),
                    Arg(name, "--name={}"),
                    Arg(pwd, "--pwd={}"),
                    Arg(descr, "--descr={}"),
                    Arg(auth, "--auth={}"),
                    Arg(os_user, "--os-user={}"),
                    Arg(agent_user, "--agent-user={}"),
                    Arg(agent_pwd, "--agent-pwd={}"),
                ),
            )

        @staticmethod
        def remove(
            session: Session,
            cluster: str,
            name: str,
            cluster_user: str | None = None,
            cluster_pwd: str | None = None,
        ) -> None:
            """
            Удаление администратора кластера.

            Args:
                session (Session): Уникальная сессия подключения.
                cluster (str): Идентификатор кластера серверов.
                name (str): Имя администратора.
                cluster_user (str | None): Имя администратора кластера.
                cluster_pwd (str | None): Пароль администратора кластера.
            """
            return session.exec(
                Command(
                    Arg("cluster"),
                    Arg("admin"),
                    Arg(cluster, "--cluster={}"),
                    Arg(cluster_user, "--cluster-user={}"),
                    Arg(cluster_pwd, "--cluster-pwd={}"),
                    Arg("remove"),
                    Arg(name, "--name={}"),
                ),
            )

    @staticmethod
    def info(session: Session, cluster: str) -> ClusterSchema:
        """
        Получение информации о кластере.

        Args:
            session (Session): Уникальная сессия подключения.
            cluster (str): Идентификатор кластера серверов.

        Returns:
            ClusterSchema: Кластер.
        """
        cluster = session.exec(
            Command(
                Arg("cluster"),
                Arg("info"),
                Arg(cluster, "--cluster={}"),
            ),
            to_dict,
        )
        return to_dc(cluster, ClusterSchema)

    @staticmethod
    def list(session: Session) -> List[ClusterSchema]:
        """
        Получение списка информации о кластерах.

        Args:
            session (Session): Уникальная сессия подключения.

        Returns:
            List[ClusterSchema]: Список кластеров.
        """
        clusters = session.exec(
            Command(
                Arg("cluster"),
                Arg("list"),
            ),
            to_list,
        )
        if clusters is None or len(clusters) == 0:
            return []
        return list_to_dc(clusters, ClusterSchema)

    @staticmethod
    def insert(
        session: Session,
        host: str,
        port: int,
        name: str | None = None,
        expiration_timeout: int = 60,
        lifetime_limit: int = 0,
        max_memory_size: int | None = None,
        max_memory_time_limit: int | None = None,
        security_level: SecurityLevel = SecurityLevel.DISABLED,
        session_fault_tolerance_level: int = 0,
        load_balancing_mode: LoadBalancingMode = LoadBalancingMode.PERFORMANCE,
        errors_count_threshold: int | None = None,
        kill_problem_processes: bool = True,
        kill_by_memory_with_dump: bool = False,
        agent_user: str | None = None,
        agent_pwd: str | None = None,
    ) -> str:
        """
        Регистрация нового кластера.

        Args:
            session (Session): Уникальная сессия подключения.
            host (str): Имя (или IP-адрес) компьютера, на котором расположен реестр кластера
                и процесс главного менеджера кластера.
            port (int): Основной порт основного менеджера.
            name (str | None): Имя (представление) кластера.
            expiration_timeout (int): Период принудительного завершения (в секундах).
            lifetime_limit (int): Период перезапуска рабочих процессов кластера (в секундах).
            max_memory_size (int | None): Максимальный объем виртуального адресного пространства
                (в килобайтах), занятого рабочим процессом.
            max_memory_time_limit (int | None): Максимальный период превышения критического объема
                памяти (в секундах).
            security_level (SecurityLevel = SecurityLevel.DISABLED): Уровень безопасности соединений.
                * `DISABLED` - уровень безопасности является самым низким и самым производительным.
                    Практически все данные передаются без использования шифрования.
                * `ONLY_CONNECTION` - использование данного уровня безопасности позволяет
                    частично защитить поток данных (только пароли) между клиентом и кластером серверов.
                * `ALWAYS` - использование данного уровня безопасности позволяет полностью защитить
                    весь поток данных (как пароли, так и непосредственно данные) между клиентом и кластером серверов.
            session_fault_tolerance_level (int): Уровень отказоустойчивости.
            load_balancing_mode (LoadBalancingMode = LoadBalancingMode.PERFORMANCE): Режим распределения нагрузки.
                * `PERFORMANCE` - выбирается список подходящих рабочих серверов, чья производительность
                    составляет не менее 75% от самого производительного сервера.
                * `MEMORY` - выбираются рабочие сервера, производительность которых составляет не менее 25%
                    от производительности самого производительного рабочего сервера.
            errors_count_threshold (int | None): Допустимое отклонение количества ошибок сервера (в процентах).
            kill_problem_processes (bool): Принудительно завершать проблемные процессы.
            kill_by_memory_with_dump (bool): Формировать дамп процесса при превышении максимального объема памяти.
            agent_user (str | None): Имя администратора агента кластера.
            agent_pwd (str | None): Пароль администратора агента кластера.

        Returns:
            str: Идентификатор кластера серверов.
        """
        return session.exec(
            Command(
                Arg("cluster"),
                Arg("insert"),
                Arg(host, "--host={}"),
                Arg(port, "--port={}"),
                Arg(name, "--name={}"),
                Arg(expiration_timeout, "--expiration-timeout={}"),
                Arg(lifetime_limit, "--lifetime-limit={}"),
                Arg(max_memory_size, "--max-memory-size={}"),
                Arg(max_memory_time_limit, "--max-memory-time-limit={}"),
                Arg(security_level, "--security-level={}"),
                Arg(
                    session_fault_tolerance_level, "--session-fault-tolerance-level={}"
                ),
                Arg(load_balancing_mode, "--load-balancing-mode={}"),
                Arg(errors_count_threshold, "--errors-count-threshold={}"),
                Arg(b2yn(kill_problem_processes), "--kill-problem-processes={}"),
                Arg(b2yn(kill_by_memory_with_dump), "--kill-by-memory-with-dump={}"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
            ),
            to_dict,
        )["cluster"]

    @staticmethod
    def update(
        session: Session,
        cluster: str,
        name: str | None = None,
        expiration_timeout: int | None = None,
        lifetime_limit: int | None = None,
        max_memory_size: int | None = None,
        max_memory_time_limit: int | None = None,
        security_level: SecurityLevel | None = None,
        session_fault_tolerance_level: int | None = None,
        load_balancing_mode: LoadBalancingMode | None = None,
        errors_count_threshold: int | None = None,
        kill_problem_processes: bool | None = None,
        kill_by_memory_with_dump: bool | None = None,
        agent_user: str | None = None,
        agent_pwd: str | None = None,
    ) -> None:
        """
        Обновление параметров кластера.

        Args:
            session (Session): Уникальная сессия подключения.
            cluster (str): Идентификатор кластера серверов.
            name (str | None): Имя (представление) кластера.
            expiration_timeout (int | None): Период принудительного завершения (в секундах).
            lifetime_limit (int | None): Период перезапуска рабочих процессов кластера (в секундах).
            max_memory_size (int | None): Максимальный объем виртуального адресного пространства (в килобайтах), занятого рабочим процессом.
            max_memory_time_limit (int | None): Максимальный период превышения критического объема памяти (в секундах).
            security_level (SecurityLevel): Уровень безопасности соединений.
                * `DISABLED` - уровень безопасности является самым низким и самым производительным.
                    Практически все данные передаются без использования шифрования.
                * `ONLY_CONNECTION` - использование данного уровня безопасности позволяет
                    частично защитить поток данных (только пароли) между клиентом и кластером серверов.
                * `ALWAYS` - использование данного уровня безопасности позволяет полностью защитить
                    весь поток данных (как пароли, так и непосредственно данные) между клиентом и кластером серверов.
            session_fault_tolerance_level (int | None): Уровень отказоустойчивости.
            load_balancing_mode (LoadBalancingMode): Режим распределения нагрузки.
                * `PERFORMANCE` - выбирается список подходящих рабочих серверов, чья производительность
                    составляет не менее 75% от самого производительного сервера.
                * `MEMORY` - выбираются рабочие сервера, производительность которых составляет не менее 25%
                    от производительности самого производительного рабочего сервера.
            errors_count_threshold (int | None): Допустимое отклонение количества ошибок сервера (в процентах).
            kill_problem_processes (bool | None): Принудительно завершать проблемные процессы.
            kill_by_memory_with_dump (bool | None): Формировать дамп процесса при превышении максимального объема памяти.
            agent_user (str | None): Имя администратора агента кластера.
            agent_pwd (str | None): Пароль администратора агента кластера.
        """
        return session.exec(
            Command(
                Arg("cluster"),
                Arg("update"),
                Arg(cluster, "--cluster={}"),
                Arg(name, "--name={}"),
                Arg(expiration_timeout, "--expiration-timeout={}"),
                Arg(lifetime_limit, "--lifetime-limit={}"),
                Arg(max_memory_size, "--max-memory-size={}"),
                Arg(max_memory_time_limit, "--max-memory-time-limit={}"),
                Arg(security_level, "--security-level={}"),
                Arg(
                    session_fault_tolerance_level, "--session-fault-tolerance-level={}"
                ),
                Arg(load_balancing_mode, "--load-balancing-mode={}"),
                Arg(errors_count_threshold, "--errors-count-threshold={}"),
                Arg(b2yn(kill_problem_processes), "--kill-problem-processes={}"),
                Arg(b2yn(kill_by_memory_with_dump), "--kill-by-memory-with-dump={}"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
            )
        )

    @staticmethod
    def remove(
        session: Session,
        cluster: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        """
        Удаление кластера.

        Args:
            session (Session): Уникальная сессия подключения.
            cluster (str): Идентификатор кластера серверов.
            cluster_user (str | None): Имя администратора кластера.
            cluster_pwd (str | None): Пароль администратора кластера.
        """
        return session.exec(
            Command(
                Arg("cluster"),
                Arg("remove"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )
