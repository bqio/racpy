from typing import List
from .command import Command, Arg
from ..session import Session
from ..handlers import to_list, to_dict
from ..utils import list_to_dc, to_dc
from ..schemas import ServerSchema, PortRange
from ..enums import Using, DedicateManagers


class Server:
    """Режим администрирования рабочего сервера."""

    @staticmethod
    def info(
        session: Session,
        cluster: str,
        server: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ServerSchema:
        """
        Получение информации о рабочем сервере.

        Args:
            session (Session): Уникальная сессия подключения.
            cluster (str): Идентификатор кластера серверов.
            server (str): Идентификатор рабочего сервера кластера серверов.
            cluster_user (str | None): Имя администратора кластера.
            cluster_pwd (str | None): Пароль администратора кластера.

        Returns:
            ServerSchema: Рабочий сервер.
        """
        _server = session.exec(
            Command(
                Arg("server"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("info"),
                Arg(server, "--server={}"),
            ),
            to_dict,
        )
        return to_dc(_server, ServerSchema)

    @staticmethod
    def list(
        session: Session,
        cluster: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> List[ServerSchema]:
        """
        Получение списка информации о рабочих серверах.

        Args:
            session (Session): Уникальная сессия подключения.
            cluster (str): Идентификатор кластера серверов.
            cluster_user (str | None): Имя администратора кластера.
            cluster_pwd (str | None): Пароль администратора кластера.

        Returns:
            List[ServerSchema]: Список рабочих серверов.
        """
        servers = session.exec(
            Command(
                Arg("server"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("list"),
            ),
            to_list,
        )
        if servers is None or len(servers) == 0:
            return []
        return list_to_dc(servers, ServerSchema)

    @staticmethod
    def insert(
        session: Session,
        cluster: str,
        agent_host: str,
        agent_port: int,
        port_range: PortRange,
        name: str | None = None,
        using: Using = Using.MAIN,
        infobases_limit: int = 8,
        memory_limit: int | None = None,
        connections_limit: int = 256,
        cluster_port: int | None = None,
        dedicate_managers: DedicateManagers = DedicateManagers.ALL,
        safe_working_processess_memory_limit: int | None = None,
        safe_call_memory_limit: int | None = None,
        critical_total_memory: int | None = None,
        temporary_allowed_total_memory: int | None = None,
        temporary_allowed_total_memory_time_limit: int = 300,
        service_principal_name: str | None = None,
        speech_to_text_model_directory: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> str:
        return session.exec(
            Command(
                Arg("server"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("insert"),
                Arg(agent_host, "--agent-host={}"),
                Arg(agent_port, "--agent-port={}"),
                Arg(port_range, "--port-range={}"),
                Arg(name, "--name={}"),
                Arg(using, "--using={}"),
                Arg(infobases_limit, "--infobases-limit={}"),
                Arg(memory_limit, "--memory-limit={}"),
                Arg(connections_limit, "--connections-limit={}"),
                Arg(cluster_port, "--cluster-port={}"),
                Arg(dedicate_managers, "--dedicate-managers={}"),
                Arg(
                    safe_working_processess_memory_limit,
                    "--safe-working-processess-memory-limit={}",
                ),
                Arg(safe_call_memory_limit, "--safe-call-memory-limit={}"),
                Arg(critical_total_memory, "--critical-total-memory={}"),
                Arg(
                    temporary_allowed_total_memory,
                    "--temporary-allowed-total-memory={}",
                ),
                Arg(
                    temporary_allowed_total_memory_time_limit,
                    "--temporary-allowed-total-memory-time-limit={}",
                ),
                Arg(service_principal_name, "--service-principal-name={}"),
                Arg(
                    speech_to_text_model_directory,
                    "--speech-to-text-model-directory={}",
                ),
            ),
            to_dict,
        )["server"]

    @staticmethod
    def update(
        session: Session,
        cluster_uuid: str,
        server_uuid: str,
        using: str | None = None,
        dedicate_managers: str | None = None,
        port_range: str | None = None,
        name: str | None = None,
        infobases_limit: int | None = None,
        memory_limit: int | None = None,
        connections_limit: int | None = None,
        cluster_port: int | None = None,
        safe_working_processess_memory_limit: int | None = None,
        safe_call_memory_limit: int | None = None,
        critical_total_memory: int | None = None,
        temporary_allowed_total_memory: int | None = None,
        temporary_allowed_total_memory_time_limit: int | None = None,
        service_principal_name: str | None = None,
        speech_to_text_model_directory: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("server"),
                Arg("update"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Arg(using, "--using={}"),
                Arg(dedicate_managers, "--dedicate-managers={}"),
                Arg(port_range, "--port-range={}"),
                Arg(name, "--name={}"),
                Arg(infobases_limit, "--infobases-limit={}"),
                Arg(memory_limit, "--memory-limit={}"),
                Arg(connections_limit, "--connections-limit={}"),
                Arg(cluster_port, "--cluster-port={}"),
                Arg(
                    safe_working_processess_memory_limit,
                    "--safe-working-processess-memory-limit={}",
                ),
                Arg(safe_call_memory_limit, "--safe-call-memory-limit={}"),
                Arg(critical_total_memory, "--critical-total-memory={}"),
                Arg(
                    temporary_allowed_total_memory,
                    "--temporary-allowed-total-memory={}",
                ),
                Arg(
                    temporary_allowed_total_memory_time_limit,
                    "--temporary-allowed-total-memory-time-limit={}",
                ),
                Arg(service_principal_name, "--service-principal-name={}"),
                Arg(
                    speech_to_text_model_directory,
                    "--speech-to-text-model-directory={}",
                ),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )

    @staticmethod
    def remove(
        session: Session,
        cluster_uuid: str,
        server_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("server"),
                Arg("remove"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )
