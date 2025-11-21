from typing import List
from .command import Command, Arg, Flag
from ..session import Session
from ..handlers import to_dict, to_list
from ..utils import b2of, b2da, b2yn, to_dc, list_to_dc
from ..schemas import InfobaseShortSchema, InfobaseSchema
from ..enums import DBMS, SecurityLevel, DateOffset


class Infobase:
    """Режим администрирования информационной базой."""

    @staticmethod
    def info(
        session: Session,
        cluster: str,
        infobase: str,
        infobase_user: str | None = None,
        infobase_pwd: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> InfobaseSchema:
        """
        Получение информации об информационной базе.

        Args:
            session (Session): Уникальная сессия подключения.
            cluster (str): Идентификатор кластера серверов.
            infobase (str): Идентификатор информационной базы.
            infobase_user (str | None): Имя администратора информационной базы.
            infobase_pwd (str | None): Пароль администратора информационной базы.
            cluster_user (str | None): Имя администратора кластера.
            cluster_pwd (str | None): Пароль администратора кластера.

        Returns:
            InfobaseSchema: Информационная база.
        """
        _infobase = session.exec(
            Command(
                Arg("infobase"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("info"),
                Arg(infobase, "--infobase={}"),
                Arg(infobase_user, "--infobase-user={}"),
                Arg(infobase_pwd, "--infobase-pwd={}"),
            ),
            to_dict,
        )
        return to_dc(_infobase, InfobaseSchema)

    class Summary:
        """Управление краткой информацией об информационных базах."""

        @staticmethod
        def info(
            session: Session,
            cluster: str,
            infobase: str,
            cluster_user: str | None = None,
            cluster_pwd: str | None = None,
        ) -> InfobaseShortSchema:
            """
            Получение краткой информации об указанной информационной базе.

            Args:
                session (Session): Уникальная сессия подключения.
                cluster (str): Идентификатор кластера серверов.
                infobase (str): Идентификатор информационной базы.
                cluster_user (str | None): Имя администратора кластера.
                cluster_pwd (str | None): Пароль администратора кластера.

            Returns:
                InfobaseShortSchema: Информационная база с краткой информацией.
            """
            _infobase = session.exec(
                Command(
                    Arg("infobase"),
                    Arg(cluster, "--cluster={}"),
                    Arg(cluster_user, "--cluster-user={}"),
                    Arg(cluster_pwd, "--cluster-pwd={}"),
                    Arg("summary"),
                    Arg("info"),
                    Arg(infobase, "--infobase={}"),
                ),
                to_dict,
            )
            return to_dc(_infobase, InfobaseShortSchema)

        @staticmethod
        def list(
            session: Session,
            cluster: str,
            cluster_user: str | None = None,
            cluster_pwd: str | None = None,
        ) -> List[InfobaseShortSchema]:
            """
            Получение списка краткой информации об информационных базах.

            Args:
                session (Session): Уникальная сессия подключения.
                cluster (str): Идентификатор кластера серверов.
                cluster_user (str | None): Имя администратора кластера.
                cluster_pwd (str | None): Пароль администратора кластера.

            Returns:
                List[InfobaseShortSchema]: Список информационных баз с краткой информацией.
            """
            infobases = session.exec(
                Command(
                    Arg("infobase"),
                    Arg(cluster, "--cluster={}"),
                    Arg(cluster_user, "--cluster-user={}"),
                    Arg(cluster_pwd, "--cluster-pwd={}"),
                    Arg("summary"),
                    Arg("list"),
                ),
                to_list,
            )
            if infobases is None or len(infobases) == 0:
                return []
            return list_to_dc(infobases, InfobaseShortSchema)

        @staticmethod
        def update(
            session: Session,
            cluster: str,
            infobase: str,
            descr: str | None = None,
            cluster_user: str | None = None,
            cluster_pwd: str | None = None,
        ) -> None:
            """
            Обновление краткой информации об информационной базе.

            Args:
                session (Session): Уникальная сессия подключения.
                cluster (str): Идентификатор кластера серверов.
                infobase (str): Идентификатор информационной базы.
                descr (str | None): Описание информационной базы.
                cluster_user (str | None): Имя администратора кластера.
                cluster_pwd (str | None): Пароль администратора кластера.
            """
            return session.exec(
                Command(
                    Arg("infobase"),
                    Arg(cluster, "--cluster={}"),
                    Arg(cluster_user, "--cluster-user={}"),
                    Arg(cluster_pwd, "--cluster-pwd={}"),
                    Arg("summary"),
                    Arg("update"),
                    Arg(infobase, "--infobase={}"),
                    Arg(descr, "--descr={}"),
                )
            )

    @staticmethod
    def create(
        session: Session,
        cluster: str,
        name: str,
        dbms: DBMS,
        db_server: str,
        db_name: str,
        locale: str,
        db_user: str | None = None,
        db_pwd: str | None = None,
        descr: str | None = None,
        date_offset: DateOffset = DateOffset.OFS_0,
        security_level: SecurityLevel = SecurityLevel.DISABLED,
        scheduled_jobs_deny: bool = False,
        license_distribution: bool = True,
        create_database: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> str:
        """
        Создание информационной базы.

        Args:
            session (Session): Уникальная сессия подключения.
            cluster (str): Идентификатор кластера серверов.
            name (str): Имя информационной базы.
            dbms (DBMS): Тип СУБД, в которой размещается информационная база.
                * `MSSQL_SERVER`
                * `POSTGRE_SQL`
                * `IBM_DB2`
                * `ORACLE_DATABASE`
            db_server (str): Имя сервера баз данных.
            db_name (str): Имя базы данных.
            locale (str): Идентификатор национальных настроек информационной базы.
            db_user (str | None): Имя администратора базы данных.
            db_pwd (str | None): Пароль администратора базы данных.
            descr (str | None): Описание информационной базы.
            date_offset (DateOffset = DateOffset.OFS_0): Смещение дат в информационной базе.
                * `OFS_0` - если нет необходимости работать с датами, предшествующими 1 января 1753 года.
                * `OFS_2000` - если есть необходимость работать с датами, предшествующими 1 января 1753 года.
            security_level (SecurityLevel = SecurityLevel.DISABLED): Уровень безопасности соединений.
                * `DISABLED` - уровень безопасности является самым низким и самым производительным.
                    Практически все данные передаются без использования шифрования.
                * `ONLY_CONNECTION` - использование данного уровня безопасности позволяет
                    частично защитить поток данных (только пароли) между клиентом и кластером серверов.
                * `ALWAYS` - использование данного уровня безопасности позволяет полностью защитить
                    весь поток данных (как пароли, так и непосредственно данные) между клиентом и кластером серверов.
            scheduled_jobs_deny (bool = False): Управление блокировкой выполнения регламентных заданий.
                * `True` - выполнение регламентных заданий запрещено.
                * `False` - выполнение регламентных заданий разрешено.
            license_distribution (bool = True): Управление выдачей лицензий сервером 1С:Предприятия.
                * `True` - выдача лицензий разрешена.
                * `False` - выдача лицензий запрещена.
            create_database (bool = False): Управление созданием базы данных.
                * `True` - при создании информационной базы создавать базу данных.
                * `False` - при создании информационной базы не создавать базу данных.
            cluster_user (str | None): Имя администратора кластера.
            cluster_pwd (str | None): Пароль администратора кластера.

        Returns:
            str: Идентификатор информационной базы.
        """
        return session.exec(
            Command(
                Arg("infobase"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("create"),
                Flag(create_database, "--create-database"),
                Arg(name, "--name={}"),
                Arg(dbms, "--dbms={}"),
                Arg(db_server, "--db-server={}"),
                Arg(db_name, "--db-name={}"),
                Arg(locale, "--locale={}"),
                Arg(db_user, "--db-user={}"),
                Arg(db_pwd, "--db-pwd={}"),
                Arg(descr, "--descr={}"),
                Arg(date_offset, "--date-offset={}"),
                Arg(security_level, "--security-level={}"),
                Arg(b2of(scheduled_jobs_deny), "--scheduled-jobs-deny={}"),
                Arg(b2da(license_distribution), "--license-distribution={}"),
            ),
            to_dict,
        )["infobase"]

    @staticmethod
    def update(
        session: Session,
        cluster: str,
        infobase: str,
        infobase_user: str | None = None,
        infobase_pwd: str | None = None,
        dbms: DBMS | None = None,
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
        sessions_deny: bool | None = None,
        scheduled_jobs_deny: bool | None = None,
        license_distribution: bool | None = None,
        external_session_manager_connection_string: str | None = None,
        external_session_manager_required: bool | None = None,
        reserve_working_processes: bool | None = None,
        security_profile_name: str | None = None,
        safe_mode_security_profile_name: str | None = None,
        disable_local_speech_to_text: bool | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        """
        Обновление информации об информационной базе.

        Args:
            session (Session): Уникальная сессия подключения.
            cluster (str): Идентификатор кластера серверов.
            infobase (str): Идентификатор информационной базы.
            infobase_user (str | None): Имя администратора информационной базы.
            infobase_pwd (str | None): Пароль администратора информационной базы.
            dbms (DBMS | None): Тип СУБД, в которой размещается информационная база.
                * `MSSQL_SERVER`
                * `POSTGRE_SQL`
                * `IBM_DB2`
                * `ORACLE_DATABASE`
            db_server (str | None): Имя сервера баз данных.
            db_name (str | None): Имя базы данных.
            db_user (str | None): Имя администратора базы данных.
            db_pwd (str | None): Пароль администратора базы данных.
            descr (str | None): Описание информационной базы.
            denied_from (str | None): Начало интервала времени, в течение которого действует режим блокировки сеансов.
            denied_message (str | None): Cообщение, выдаваемое при попытке нарушения блокировки сеансов.
            denied_parameter (str | None): Параметр блокировки сеансов.
            denied_to (str | None): Конец интервала времени, в течение которого действует режим блокировки сеансов.
            permission_code (str | None): Код разрешения, разрешающий начало сеанса вопреки действующей блокировке сеансов.
            sessions_deny (bool | None): Ууправление режимом блокировки сеансов.
                * `True` - режим блокировки начала сеансов включен.
                * `False` - режим блокировки начала сеансов выключен.
            scheduled_jobs_deny (bool | None): Управление блокировкой выполнения регламентных заданий.
                * `True` - выполнение регламентных заданий запрещено.
                * `False` - выполнение регламентных заданий разрешено.
            license_distribution (bool | None): Управление выдачей лицензий сервером 1С:Предприятия.
                * `True` - выдача лицензий разрешена.
                * `False` - выдача лицензий запрещена.
            external_session_manager_connection_string (str | None): Параметры внешнего управления сеансами.
            external_session_manager_required (bool | None): Обязательное использование внешнего управления сеансами.
                * `True` - использование внешнего управления сеансами обязательно.
                * `False` - использование внешнего управления сеансами необязательно.
            reserve_working_processes (bool | None): Резервирование рабочих процессов.
                * `True` - резервирование рабочих процессов включено.
                * `False` - резервирование рабочих процессов выключено.
            security_profile_name (str | None): Профиль безопасности информационной базы.
            safe_mode_security_profile_name (str | None): Профиль безопасности внешнего кода.
            disable_local_speech_to_text (bool | None): Запретить локальное распознавание речи.
                * `True` - локальное распознавание речи запрещено.
                * `False` - локальное распознавание речи разрешено.
            cluster_user (str | None): Имя администратора кластера.
            cluster_pwd (str | None): Пароль администратора кластера.
        """
        return session.exec(
            Command(
                Arg("infobase"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("update"),
                Arg(infobase, "--infobase={}"),
                Arg(infobase_user, "--infobase-user={}"),
                Arg(infobase_pwd, "--infobase-pwd={}"),
                Arg(dbms, "--dbms={}"),
                Arg(db_server, "--db-server={}"),
                Arg(db_name, "--db-name={}"),
                Arg(db_user, "--db-user={}"),
                Arg(db_pwd, "--db-pwd={}"),
                Arg(descr, "--descr={}"),
                Arg(denied_from, "--denied-from={}"),
                Arg(denied_message, "--denied-message={}"),
                Arg(denied_parameter, "--denied-parameter={}"),
                Arg(denied_to, "--denied-to={}"),
                Arg(permission_code, "--permission-code={}"),
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
            )
        )

    @staticmethod
    def drop(
        session: Session,
        cluster: str,
        infobase: str,
        infobase_user: str | None = None,
        infobase_pwd: str | None = None,
        drop_database: bool = False,
        clear_database: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        """
        Удаление информационной базы.

        Args:
            session (Session): Уникальная сессия подключения.
            cluster (str): Идентификатор кластера серверов.
            infobase (str): Идентификатор информационной базы.
            infobase_user (str | None): Имя администратора информационной базы.
            infobase_pwd (str | None): Пароль администратора информационной базы.
            drop_database (bool = False): Удаление базы данных.
                * `True` - при удалении информационной базы удалять базу данных.
                * `False` - при удалении информационной базы не удалять базу данных.
            clear_database (bool = False): Очистка базы данных.
                * `True` - при удалении информационной базы очищать базу данных.
                * `False` - при удалении информационной базы не очищать базу данных.
            cluster_user (str | None): Имя администратора кластера.
            cluster_pwd (str | None): Пароль администратора кластера.
        """
        return session.exec(
            Command(
                Arg("infobase"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("drop"),
                Arg(infobase, "--infobase={}"),
                Arg(infobase_user, "--infobase-user={}"),
                Arg(infobase_pwd, "--infobase-pwd={}"),
                Flag(drop_database, "--drop-database"),
                Flag(clear_database, "--clear-database"),
            )
        )
