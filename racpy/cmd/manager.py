from .command import Command, Arg
from ..session import Session
from ..handlers import to_list, to_dict


class Manager:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        manager_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.exec(
            Command(
                Arg("manager"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(manager_uuid, "--manager={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> list[dict[str, str | int]] | None:
        return session.exec(
            Command(
                Arg("manager"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
