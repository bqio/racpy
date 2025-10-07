from .command import Command, Arg
from ..session import Session
from ..types import ListOfEntry, Entry
from ..handlers import to_str, to_list


class Agent:
    @staticmethod
    def version(session: Session) -> str:
        return session.exec(
            Command(
                Arg("agent"),
                Arg("version"),
            ),
            to_str,
        )


class AgentAdmin:
    @staticmethod
    def list(
        session: Session, agent_user: str | None = None, agent_pwd: str | None = None
    ) -> ListOfEntry:
        admins = session.exec(
            Command(
                Arg("agent"),
                Arg("admin"),
                Arg("list"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
            ),
            to_list,
        )
        if admins is None or len(admins) == 0:
            return []
        return admins

    @staticmethod
    def first(
        session: Session, agent_user: str | None = None, agent_pwd: str | None = None
    ) -> Entry | None:
        admins = AgentAdmin.list(session, agent_user, agent_pwd)
        if len(admins) == 0:
            return None
        return admins[0]

    @staticmethod
    def remove(
        session: Session,
        admin_name: str,
        agent_user: str | None = None,
        agent_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("agent"),
                Arg("admin"),
                Arg("remove"),
                Arg(admin_name, "--name={}"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
            ),
        )

    @staticmethod
    def create(
        session: Session,
        admin_name: str,
        auth_type: str = "pwd",
        pwd: str | None = None,
        descr: str | None = None,
        os_user: str | None = None,
        agent_user: str | None = None,
        agent_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("agent"),
                Arg("admin"),
                Arg("register"),
                Arg(admin_name, "--name={}"),
                Arg(auth_type, "--auth={}"),
                Arg(pwd, "--pwd={}"),
                Arg(descr, "--descr={}"),
                Arg(os_user, "--os-user={}"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
            ),
        )
