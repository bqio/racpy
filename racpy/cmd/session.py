from .command import Command, Arg, Flag
from ..session import Session
from ..handlers import to_list, to_dict


class UserSession:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        user_session_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> dict[str, str | int] | None:
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
        cluster_uuid: str,
        infobase_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> list[dict[str, str | int]] | None:
        return session.exec(
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

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> dict[str, str | int] | None:
        user_sessions = UserSession.list(
            session, cluster_uuid, infobase_uuid, licenses, cluster_user, cluster_pwd
        )
        if user_sessions is None:
            return user_sessions
        return user_sessions[0]

    @staticmethod
    def firstid(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> str | None:
        user_session = UserSession.first(
            session, cluster_uuid, infobase_uuid, licenses, cluster_user, cluster_pwd
        )
        if user_session is None:
            return user_session
        return user_session["session"]

    @staticmethod
    def kill(
        session: Session,
        cluster_uuid: str,
        user_session_uuid: str,
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
        cluster_uuid: str,
        user_session_uuid: str,
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
