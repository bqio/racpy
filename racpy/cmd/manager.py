from .command import Command, Arg
from ..session import Session
from ..types import EntryUUID, Entry, ListOfEntry
from ..handlers import to_list, to_dict


class Manager:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: EntryUUID,
        manager_uuid: EntryUUID,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry:
        return session.exec(
            Command(
                Arg("manager"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(manager_uuid, "--manager={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: EntryUUID,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        managers = session.exec(
            Command(
                Arg("manager"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if managers is None or len(managers) == 0:
            return []
        return managers

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: EntryUUID,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry | None:
        managers = Manager.list(
            session,
            cluster_uuid,
            cluster_user,
            cluster_pwd,
        )
        if len(managers) == 0:
            return None
        return managers[0]

    @staticmethod
    def firstid(
        session: Session,
        cluster_uuid: EntryUUID,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> EntryUUID | None:
        manager = Manager.first(
            session,
            cluster_uuid,
            cluster_user,
            cluster_pwd,
        )
        if manager:
            return manager["manager"]
        return None
