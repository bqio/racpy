from .command import Command, Arg, Flag
from ..session import Session
from ..types import Entry, EntryUUID, ListOfEntry
from ..handlers import to_list, to_dict


class UserSession:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: EntryUUID,
        user_session_uuid: EntryUUID,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry:
        return session.exec(
            Command(
                Arg("session"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(user_session_uuid, "--session={}"),
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
        infobase_uuid: EntryUUID,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        sessions = session.exec(
            Command(
                Arg("session"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(infobase_uuid, "--infobase={}"),
                Flag(licenses, "--licenses"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if sessions is None or len(sessions) == 0:
            return []
        return sessions

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: EntryUUID,
        infobase_uuid: EntryUUID,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry | None:
        user_sessions = UserSession.list(
            session, cluster_uuid, infobase_uuid, licenses, cluster_user, cluster_pwd
        )
        if len(user_sessions) == 0:
            return None
        return user_sessions[0]

    @staticmethod
    def firstid(
        session: Session,
        cluster_uuid: EntryUUID,
        infobase_uuid: EntryUUID,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> EntryUUID | None:
        user_session = UserSession.first(
            session, cluster_uuid, infobase_uuid, licenses, cluster_user, cluster_pwd
        )
        if user_session:
            return user_session["session"]
        return None

    @staticmethod
    def kill(
        session: Session,
        cluster_uuid: EntryUUID,
        user_session_uuid: EntryUUID,
        error_message: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("session"),
                Arg("terminate"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(user_session_uuid, "--session={}"),
                Arg(error_message, "--error-message={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )

    @staticmethod
    def interrupt(
        session: Session,
        cluster_uuid: EntryUUID,
        user_session_uuid: EntryUUID,
        error_message: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("session"),
                Arg("interrupt-current-server-call"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(user_session_uuid, "--session={}"),
                Arg(error_message, "--error-message={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )
