from .command import Command, Arg, Flag
from ..session import Session
from ..handlers import to_dict
from ..types import Dict, UUID_String
from ..utils import b2of, b2da, b2yn


class Infobase:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str,
        infobase_user: str | None = None,
        infobase_pwd: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Dict:
        return session.exec(
            Command(
                Arg("infobase"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(infobase_uuid, "--infobase={}"),
                Arg(infobase_user, "--infobase-user={}"),
                Arg(infobase_pwd, "--infobase-pwd={}"),
                Arg(infobase_uuid, "--infobase={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )

    @staticmethod
    def create(
        session: Session,
        cluster_uuid: str,
        name: str,
        db_server: str,
        db_name: str,
        locale: str,
        create_database: bool = True,
        dbms: str = "MSSQLServer",
        date_offset: str = "2000",
        scheduled_jobs_deny: bool | None = None,
        license_distribution: bool | None = None,
        security_level: int | None = None,
        db_user: str | None = None,
        db_pwd: str | None = None,
        descr: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> UUID_String:
        return session.exec(
            Command(
                Arg("infobase"),
                Arg("create"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(name, "--name={}"),
                Arg(db_server, "--db-server={}"),
                Arg(db_name, "--db-name={}"),
                Arg(locale, "--locale={}"),
                Flag(create_database, "--create-database"),
                Arg(dbms, "--dbms={}"),
                Arg(date_offset, "--date-offset={}"),
                Arg(b2of(scheduled_jobs_deny), "--scheduled-jobs-deny={}"),
                Arg(b2da(license_distribution), "--license-distribution={}"),
                Arg(db_user, "--db-user={}"),
                Arg(db_pwd, "--db-pwd={}"),
                Arg(descr, "--descr={}"),
                Arg(security_level, "--security-level={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )["infobase"]

    @staticmethod
    def update(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str,
        infobase_user: str | None = None,
        infobase_pwd: str | None = None,
        dbms: str | None = None,
        sessions_deny: bool | None = None,
        scheduled_jobs_deny: bool | None = None,
        license_distribution: bool | None = None,
        external_session_manager_connection_string: str | None = None,
        external_session_manager_required: bool | None = None,
        reserve_working_processes: bool | None = None,
        security_profile_name: str | None = None,
        safe_mode_security_profile_name: str | None = None,
        disable_local_speech_to_text: bool | None = None,
        db_server: str | None = None,
        db_name: str | None = None,
        db_user: str | None = None,
        db_pwd: str | None = None,
        descr: str | None = None,
        denied_from: str | None = None,
        denied_message: str | None = None,
        denied_parameter: str | None = None,
        denied_to: str | None = None,
        permission_code: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("infobase"),
                Arg("update"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(infobase_uuid, "--infobase={}"),
                Arg(infobase_user, "--infobase-user={}"),
                Arg(infobase_pwd, "--infobase-pwd={}"),
                Arg(db_server, "--db-server={}"),
                Arg(db_name, "--db-name={}"),
                Arg(dbms, "--dbms={}"),
                Arg(b2of(sessions_deny), "--sessions-deny={}"),
                Arg(b2of(scheduled_jobs_deny), "--scheduled-jobs-deny={}"),
                Arg(b2da(license_distribution), "--license-distribution={}"),
                Arg(
                    external_session_manager_connection_string,
                    "--external-session-manager-connection-string={}",
                ),
                Arg(
                    b2yn(external_session_manager_required),
                    "--external-session-manager-required={}",
                ),
                Arg(b2yn(reserve_working_processes), "--reserve-working-processes={}"),
                Arg(security_profile_name, "--security-profile-name={}"),
                Arg(
                    safe_mode_security_profile_name,
                    "--safe-mode-security-profile-name={}",
                ),
                Arg(
                    b2yn(disable_local_speech_to_text),
                    "--disable-local-speech-to-text={}",
                ),
                Arg(db_user, "--db-user={}"),
                Arg(db_pwd, "--db-pwd={}"),
                Arg(descr, "--descr={}"),
                Arg(denied_from, "--denied-from={}"),
                Arg(denied_message, "--denied-message={}"),
                Arg(denied_parameter, "--denied-parameter={}"),
                Arg(denied_to, "--denied-to={}"),
                Arg(permission_code, "--permission-code={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )

    @staticmethod
    def remove(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str,
        drop_database: bool = False,
        clear_database: bool = False,
        infobase_user: str | None = None,
        infobase_pwd: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("infobase"),
                Arg("drop"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(infobase_uuid, "--infobase={}"),
                Flag(drop_database, "--drop-database"),
                Flag(clear_database, "--clear-database"),
                Arg(infobase_user, "--infobase-user={}"),
                Arg(infobase_pwd, "--infobase-pwd={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )
