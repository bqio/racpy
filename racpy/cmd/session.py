from typing import List
from .command import Command, Arg, Flag
from ..session import Session
from ..handlers import to_list, to_dict
from ..utils import list_to_dc, to_dc
from ..schemas import UserSessionSchema, UserSessionWithLicensesSchema


class UserSession:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        user_session_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> UserSessionSchema | UserSessionWithLicensesSchema:
        user_session = session.exec(
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
        if licenses:
            return to_dc(user_session, UserSessionWithLicensesSchema)
        return to_dc(user_session, UserSessionSchema)

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str | None = None,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> List[UserSessionSchema | UserSessionWithLicensesSchema]:
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
        if licenses:
            return list_to_dc(sessions, UserSessionWithLicensesSchema)
        return list_to_dc(sessions, UserSessionSchema)

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> UserSessionSchema | UserSessionWithLicensesSchema | None:
        user_sessions = UserSession.list(
            session, cluster_uuid, infobase_uuid, licenses, cluster_user, cluster_pwd
        )
        if len(user_sessions) == 0:
            return None
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
        if user_session:
            return user_session.session
        return None

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
