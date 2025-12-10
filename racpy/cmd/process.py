from .command import Command, Arg, Flag
from ..session import Session


class Process:
    @staticmethod
    def info(
        session: Session,
        cluster: str,
        process: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.exec(
            Command(
                Arg("process"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("info"),
                Arg(process, "--process={}"),
                Flag(licenses, "--licenses"),
            )
        ).to_dict()

    @staticmethod
    def list(
        session: Session,
        cluster: str,
        server: str | None = None,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.exec(
            Command(
                Arg("process"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("list"),
                Arg(server, "--server={}"),
                Flag(licenses, "--licenses"),
            )
        ).to_list()

    @staticmethod
    def turn_off(
        session: Session,
        cluster: str,
        process: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.call(
            Command(
                Arg("process"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("turn-off"),
                Arg(process, "--process={}"),
            )
        )
