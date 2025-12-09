from .command import Command, Arg, Flag
from ..session import Session


class UserSession:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        user_session_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.exec(
            Command(
                Arg("session"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(user_session_uuid, "--session={}"),
                Flag(licenses, "--licenses"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        ).to_dict()

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str | None = None,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.exec(
            Command(
                Arg("session"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(infobase_uuid, "--infobase={}"),
                Flag(licenses, "--licenses"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        ).to_list()

    @staticmethod
    def kill(
        session: Session,
        cluster_uuid: str,
        user_session_uuid: str,
        error_message: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.call(
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
    ):
        return session.call(
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
