from .command import Command, Arg
from ..session import Session
from ..handlers import to_str, to_list
from ..types import List, String


class Agent:
    @staticmethod
    def version(session: Session) -> String:
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
    ) -> List | None:
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
