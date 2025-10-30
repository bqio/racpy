from typing import List
from .command import Command, Arg
from ..session import Session
from ..handlers import to_list, to_dict
from ..utils import list_to_dc, to_dc
from ..schemas import LimitSchema


class Limit:
    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> List[LimitSchema]:
        limits = session.exec(
            Command(
                Arg("limit"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if limits is None or len(limits) == 0:
            return []
        return list_to_dc(limits, LimitSchema)

    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        limit_name: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> LimitSchema:
        limit = session.exec(
            Command(
                Arg("limit"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(limit_name, "--limit={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )
        return to_dc(limit, LimitSchema)

    @staticmethod
    def update(
        session: Session,
        cluster_uuid: str,
        limit_name: str,
        action: str,
        counter_name: str,
        duration: int | None = None,
        cpu_time: int | None = None,
        memory: int | None = None,
        read: int | None = None,
        write: int | None = None,
        duration_dbms: int | None = None,
        dbms_bytes: int | None = None,
        service: int | None = None,
        call: int | None = None,
        number_of_active_sessions: int | None = None,
        number_of_sessions: int | None = None,
        error_message: str | None = None,
        descr: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("limit"),
                Arg("update"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(limit_name, "--name={}"),
                Arg(action, "--action={}"),
                Arg(counter_name, "--counter={}"),
                Arg(duration, "--duration={}"),
                Arg(cpu_time, "--cpu-time={}"),
                Arg(memory, "--memory={}"),
                Arg(read, "--read={}"),
                Arg(write, "--write={}"),
                Arg(duration_dbms, "--duration-dbms={}"),
                Arg(dbms_bytes, "--dbms-bytes={}"),
                Arg(service, "--service={}"),
                Arg(call, "--call={}"),
                Arg(number_of_active_sessions, "--number-of-active-sessions={}"),
                Arg(number_of_sessions, "--number-of-sessions={}"),
                Arg(error_message, "--error-message={}"),
                Arg(descr, "--descr={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
        )

    @staticmethod
    def remove(
        session: Session,
        cluster_uuid: str,
        limit_name: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("limit"),
                Arg("remove"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(limit_name, "--name={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
        )
