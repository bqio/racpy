from typing import List
from .command import Command, Arg
from ..session import Session
from ..handlers import to_list, to_dict
from ..utils import list_to_dc, to_dc
from ..schemas import ServerSchema


class Server:
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

    @staticmethod
    def create(
        session: Session,
        cluster_uuid: str,
        agent_host: str,
        agent_port: int,
        port_range: str,
        using: str = "main",
        dedicate_managers: str = "all",
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
    ) -> str:
        return session.exec(
            Command(
                Arg("server"),
                Arg("insert"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(agent_host, "--agent-host={}"),
                Arg(agent_port, "--agent-port={}"),
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
            ),
            to_dict,
        )["server"]

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> List[ServerSchema]:
        servers = session.exec(
            Command(
                Arg("server"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if servers is None or len(servers) == 0:
            return []
        return list_to_dc(servers, ServerSchema)

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ServerSchema | None:
        servers = Server.list(session, cluster_uuid, cluster_user, cluster_pwd)
        if len(servers) == 0:
            return None
        return servers[0]

    @staticmethod
    def firstid(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> str | None:
        server = Server.first(session, cluster_uuid, cluster_user, cluster_pwd)
        if server:
            return server.server
        return None

    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        server_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ServerSchema:
        server = session.exec(
            Command(
                Arg("server"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )
        return to_dc(server, ServerSchema)
