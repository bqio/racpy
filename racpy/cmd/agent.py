from .command import Command, Arg
from ..session import Session
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
    ) -> list[dict[str, str | int]] | None:
        return session.exec(
            Command(
                Arg("agent"),
                Arg("admin"),
                Arg("list"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
            ),
            to_list,
        )

    @staticmethod
    def first(
        session: Session, agent_user: str | None = None, agent_pwd: str | None = None
    ) -> dict[str, str | int] | None:
        admins = AgentAdmin.list(session, agent_user, agent_pwd)
        if admins is None:
            return admins
        return admins[0]

    @staticmethod
    def remove(
        session: Session,
        name: str,
        agent_user: str | None = None,
        agent_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("agent"),
                Arg("admin"),
                Arg("remove"),
                Arg(name, "--name={}"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
            ),
        )

    @staticmethod
    def create(
        session: Session,
        name: str,
        auth: str = "pwd",
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
                Arg(name, "--name={}"),
                Arg(auth, "--auth={}"),
                Arg(pwd, "--pwd={}"),
                Arg(descr, "--descr={}"),
                Arg(os_user, "--os-user={}"),
                Arg(agent_user, "--agent-user={}"),
                Arg(agent_pwd, "--agent-pwd={}"),
            ),
            None,
        )
