from .command import Command, Arg
from ..session import Session
from ..types import EntryUUID, Entry, ListOfEntry
from ..handlers import to_list


class Lock:
    @staticmethod
    def list(
        session: Session,
        cluster_uuid: EntryUUID,
        infobase_uuid: EntryUUID,
        connection_uuid: EntryUUID,
        user_session_uuid: EntryUUID,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        locks = session.exec(
            Command(
                Arg("lock"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(infobase_uuid, "--infobase={}"),
                Arg(connection_uuid, "--connection={}"),
                Arg(user_session_uuid, "--session={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if locks is None or len(locks) == 0:
            return []
        return locks

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: EntryUUID,
        infobase_uuid: EntryUUID,
        connection_uuid: EntryUUID,
        user_session_uuid: EntryUUID,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry | None:
        locks = Lock.list(
            session,
            cluster_uuid,
            infobase_uuid,
            connection_uuid,
            user_session_uuid,
            cluster_user,
            cluster_pwd,
        )
        if len(locks) == 0:
            return None
        return locks[0]
