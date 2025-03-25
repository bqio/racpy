from .command import Command, Arg
from ..session import Session
from ..handlers import to_list


class Lock:
    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str,
        connection_uuid: str,
        user_session_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> list[dict[str, str | int]] | None:
        return session.exec(
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

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str,
        connection_uuid: str,
        user_session_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> dict[str, str | int] | None:
        locks = Lock.list(
            session,
            cluster_uuid,
            infobase_uuid,
            connection_uuid,
            user_session_uuid,
            cluster_user,
            cluster_pwd,
        )
        if locks is None:
            return locks
        return locks[0]
