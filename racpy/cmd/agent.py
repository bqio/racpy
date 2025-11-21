from typing import List, Optional
from .command import Command, Arg
from ..session import Session
from ..handlers import to_str, to_list
from ..utils import list_to_dc
from ..schemas import AgentAdminSchema
from ..enums import AuthMethod


class Agent:
    """Режим администрирования агента кластера серверов."""

    class Admin:
        """Управление администраторами агента кластера."""

        @staticmethod
        def list(
            session: Session,
            agent_user: str | None = None,
            agent_pwd: str | None = None,
        ) -> List[AgentAdminSchema]:
            """
            Получение списка администраторов агента кластера.

            Args:
                session (Session): Уникальная сессия подключения.
                agent_user (str | None): Имя администратора агента кластера.
                agent_pwd (str | None): Пароль администратора агента кластера.

            Returns:
                List[AgentAdminSchema]: Список администраторов агента кластера.
            """
            admins = session.exec(
                Command(
                    Arg("agent"),
                    Arg(agent_user, "--agent-user={}"),
                    Arg(agent_pwd, "--agent-pwd={}"),
                    Arg("admin"),
                    Arg("list"),
                ),
                to_list,
            )
            if admins is None or len(admins) == 0:
                return []
            return list_to_dc(admins, AgentAdminSchema)

        @staticmethod
        def register(
            session: Session,
            name: str,
            auth: AuthMethod = AuthMethod.PWD,
            pwd: str | None = None,
            descr: str | None = None,
            os_user: str | None = None,
            agent_user: str | None = None,
            agent_pwd: str | None = None,
        ) -> None:
            """
            Добавление нового администратора агента кластера.

            Args:
                session (Session): Уникальная сессия подключения.
                name (str): Имя администратора.
                auth (AuthMethod = AuthMethod.PWD): Способ аутентификации.
                    * `PWD` — аутентификация по паролю (поле `pwd` должно быть заполнено).
                    * `OS` — аутентификация через операционную систему (поле `pwd` игнорируется).
                pwd (str | None): Пароль администратора. Используется только если выбран способ аутентификации `PWD`.
                descr (str | None): Описание администратора.
                os_user (str | None): Имя пользователя операционной системы.
                agent_user (str | None): Имя администратора агента кластера.
                agent_pwd (str | None): Пароль администратора агента кластера.
            """
            return session.exec(
                Command(
                    Arg("agent"),
                    Arg(agent_user, "--agent-user={}"),
                    Arg(agent_pwd, "--agent-pwd={}"),
                    Arg("admin"),
                    Arg("register"),
                    Arg(name, "--name={}"),
                    Arg(pwd, "--pwd={}"),
                    Arg(descr, "--descr={}"),
                    Arg(auth, "--auth={}"),
                    Arg(os_user, "--os-user={}"),
                ),
            )

        @staticmethod
        def remove(
            session: Session,
            name: str,
            agent_user: str | None = None,
            agent_pwd: str | None = None,
        ) -> None:
            """
            Удаление администратора агента кластера.

            Args:
                session (Session): Уникальная сессия подключения.
                name (str): Имя администратора.
                agent_user (str | None): Имя администратора агента кластера.
                agent_pwd (str | None): Пароль администратора агента кластера.
            """
            return session.exec(
                Command(
                    Arg("agent"),
                    Arg(agent_user, "--agent-user={}"),
                    Arg(agent_pwd, "--agent-pwd={}"),
                    Arg("admin"),
                    Arg("remove"),
                    Arg(name, "--name={}"),
                ),
            )

    @staticmethod
    def version(session: Session) -> str:
        """
        Получение версии агента кластера.

        Args:
            session (Session): Уникальная сессия подключения.

        Returns:
            str: Версия агента кластера.
        """
        return session.exec(
            Command(
                Arg("agent"),
                Arg("version"),
            ),
            to_str,
        )
