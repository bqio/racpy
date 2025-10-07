from .command import Command, Arg, Flag
from ..session import Session
from ..types import EntryUUID, Entry, ListOfEntry
from ..handlers import to_list, to_dict


class Process:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: EntryUUID,
        process_uuid: EntryUUID,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry:
        return session.exec(
            Command(
                Arg("process"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(process_uuid, "--process={}"),
                Flag(licenses, "--licenses"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: EntryUUID,
        server_uuid: EntryUUID,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        processes = session.exec(
            Command(
                Arg("process"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Flag(licenses, "--licenses"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if processes is None or len(processes) == 0:
            return []
        return processes

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: EntryUUID,
        server_uuid: EntryUUID,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry | None:
        processes = Process.list(
            session, cluster_uuid, server_uuid, licenses, cluster_user, cluster_pwd
        )
        if len(processes) == 0:
            return None
        return processes[0]

    @staticmethod
    def firstid(
        session: Session,
        cluster_uuid: EntryUUID,
        server_uuid: EntryUUID,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> EntryUUID | None:
        process = Process.first(
            session, cluster_uuid, server_uuid, licenses, cluster_user, cluster_pwd
        )
        if process:
            return process["process"]
        return None
