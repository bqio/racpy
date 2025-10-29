from .command import Command, Arg
from ..session import Session
from ..handlers import to_list, to_dict
from ..utils import list_to_dc, to_dc
from ..schemas import ConnectionSchema, ConnectionShortSchema


class Connection:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        connection_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ConnectionShortSchema:
        connection = session.exec(
            Command(
                Arg("connection"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(connection_uuid, "--connection={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )
        return to_dc(connection, ConnectionShortSchema)

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        process_uuid: str,
        infobase_uuid: str,
        infobase_user: str | None = None,
        infobase_pwd: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> list[ConnectionSchema]:
        connections = session.exec(
            Command(
                Arg("connection"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(process_uuid, "--process={}"),
                Arg(infobase_uuid, "--infobase={}"),
                Arg(infobase_user, "--infobase-user={}"),
                Arg(infobase_pwd, "--infobase-pwd={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if connections is None or len(connections) == 0:
            return []
        return list_to_dc(connections, ConnectionSchema)

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: str,
        process_uuid: str,
        infobase_uuid: str,
        infobase_user: str | None = None,
        infobase_pwd: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ConnectionSchema | None:
        connections = Connection.list(
            session,
            cluster_uuid,
            process_uuid,
            infobase_uuid,
            infobase_user,
            infobase_pwd,
            cluster_user,
            cluster_pwd,
        )
        if len(connections) == 0:
            return None
        return connections

    @staticmethod
    def firstid(
        session: Session,
        cluster_uuid: str,
        process_uuid: str,
        infobase_uuid: str,
        infobase_user: str | None = None,
        infobase_pwd: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> str | None:
        connection = Connection.first(
            session,
            cluster_uuid,
            process_uuid,
            infobase_uuid,
            infobase_user,
            infobase_pwd,
            cluster_user,
            cluster_pwd,
        )
        if connection:
            return connection.connection
        return None

    @staticmethod
    def kill(
        session: Session,
        cluster_uuid: str,
        process_uuid: str,
        connection_uuid: str,
        infobase_user: str | None = None,
        infobase_pwd: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("connection"),
                Arg("disconnect"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(process_uuid, "--process={}"),
                Arg(connection_uuid, "--connection={}"),
                Arg(infobase_user, "--infobase-user={}"),
                Arg(infobase_pwd, "--infobase-pwd={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )
