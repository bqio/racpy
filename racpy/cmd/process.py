from .command import Command, Arg, Flag
from ..session import Session


class Process:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        process_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.exec(
            Command(
                Arg("process"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(process_uuid, "--process={}"),
                Flag(licenses, "--licenses"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        ).to_dict()

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        server_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.exec(
            Command(
                Arg("process"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Flag(licenses, "--licenses"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        ).to_list()
