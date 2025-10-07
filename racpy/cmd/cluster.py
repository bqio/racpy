from .command import Command, Arg
from ..session import Session
from ..types import Entry, EntryUUID, ListOfEntry
from ..handlers import to_list, to_dict
from ..utils import b2yn


class Cluster:
    @staticmethod
    def create(
        session: Session,
        host: str,
        port: int,
        name: str | None = None,
        load_balancing_mode: str | None = None,
        security_level: int | None = None,
        kill_problem_processes: bool | None = None,
        kill_by_memory_with_dump: bool | None = None,
        expiration_timeout: int | None = None,
        lifetime_limit: int | None = None,
        max_memory_size: int | None = None,
        max_memory_time_limit: int | None = None,
        session_fault_tolerance_level: int | None = None,
        errors_count_threshold: int | None = None,
        agent_user: str | None = None,
        agent_pwd: str | None = None,
    ) -> EntryUUID:
        return session.exec(
            Command(
                Arg("cluster"),
                Arg("insert"),
                Arg(host, "--host={}"),
                Arg(port, "--port={}"),
                Arg(name, "--name={}"),
                Arg(load_balancing_mode, "--load-balancing-mode={}"),
                Arg(b2yn(kill_problem_processes), "--kill-problem-processes={}"),
                Arg(b2yn(kill_by_memory_with_dump), "--kill-by-memory-with-dump={}"),
                Arg(expiration_timeout, "--expiration-timeout={}"),
                Arg(lifetime_limit, "--lifetime-limit={}"),
                Arg(max_memory_size, "--max-memory-size={}"),
                Arg(max_memory_time_limit, "--max-memory-time-limit={}"),
                Arg(security_level, "--security-level={}"),
                Arg(
                    session_fault_tolerance_level, "--session-fault-tolerance-level={}"
                ),
                Arg(errors_count_threshold, "--errors-count-threshold={}"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
            ),
            to_dict,
        )["cluster"]

    @staticmethod
    def update(
        session: Session,
        cluster_uuid: EntryUUID,
        name: str | None = None,
        load_balancing_mode: str | None = None,
        kill_problem_processes: bool | None = None,
        kill_by_memory_with_dump: bool | None = None,
        expiration_timeout: int | None = None,
        lifetime_limit: int | None = None,
        max_memory_size: int | None = None,
        max_memory_time_limit: int | None = None,
        security_level: int | None = None,
        session_fault_tolerance_level: int | None = None,
        errors_count_threshold: int | None = None,
        agent_user: str | None = None,
        agent_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("cluster"),
                Arg("update"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(name, "--name={}"),
                Arg(load_balancing_mode, "--load-balancing-mode={}"),
                Arg(b2yn(kill_problem_processes), "--kill-problem-processes={}"),
                Arg(b2yn(kill_by_memory_with_dump), "--kill-by-memory-with-dump={}"),
                Arg(expiration_timeout, "--expiration-timeout={}"),
                Arg(lifetime_limit, "--lifetime-limit={}"),
                Arg(max_memory_size, "--max-memory-size={}"),
                Arg(max_memory_time_limit, "--max-memory-time-limit={}"),
                Arg(security_level, "--security-level={}"),
                Arg(
                    session_fault_tolerance_level, "--session-fault-tolerance-level={}"
                ),
                Arg(errors_count_threshold, "--errors-count-threshold={}"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
            ),
            None,
        )

    @staticmethod
    def remove(
        session: Session,
        cluster_uuid: EntryUUID,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("cluster"),
                Arg("remove"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )

    @staticmethod
    def list(session: Session) -> ListOfEntry:
        clusters = session.exec(
            Command(
                Arg("cluster"),
                Arg("list"),
            ),
            to_list,
        )
        if clusters is None or len(clusters) == 0:
            return []
        return clusters

    @staticmethod
    def first(session: Session) -> Entry | None:
        clusters = Cluster.list(session)
        if len(clusters) == 0:
            return None
        return clusters[0]

    @staticmethod
    def firstid(session: Session) -> EntryUUID | None:
        cluster = Cluster.first(session)
        if cluster:
            return cluster["cluster"]
        return None

    @staticmethod
    def info(session: Session, cluster_uuid: EntryUUID) -> Entry:
        return session.exec(
            Command(
                Arg("cluster"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
            ),
            to_dict,
        )


class ClusterAdmin:
    @staticmethod
    def list(
        session: Session,
        cluster_uuid: EntryUUID,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        admins = session.exec(
            Command(
                Arg("cluster"),
                Arg("admin"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if admins is None or len(admins) == 0:
            return []
        return admins

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: EntryUUID,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry | None:
        admins = ClusterAdmin.list(session, cluster_uuid, cluster_user, cluster_pwd)
        if len(admins) == 0:
            return None
        return admins[0]

    @staticmethod
    def create(
        session: Session,
        cluster_uuid: EntryUUID,
        admin_name: str | None = None,
        auth_type: str = "pwd",
        pwd: str | None = None,
        descr: str | None = None,
        os_user: str | None = None,
        agent_user: str | None = None,
        agent_pwd: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("cluster"),
                Arg("admin"),
                Arg("register"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(admin_name, "--name={}"),
                Arg(auth_type, "--auth={}"),
                Arg(pwd, "--pwd={}"),
                Arg(descr, "--descr={}"),
                Arg(os_user, "--os-user={}"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
        )

    @staticmethod
    def remove(
        session: Session,
        cluster_uuid: EntryUUID,
        admin_name: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("cluster"),
                Arg("admin"),
                Arg("remove"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(admin_name, "--name={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
        )
