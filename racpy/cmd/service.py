from .command import Command, Arg
from ..session import Session
from ..types import Entry, EntryUUID, ListOfEntry
from ..handlers import to_list


class Service:
    @staticmethod
    def list(
        session: Session,
        cluster_uuid: EntryUUID,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        services = session.exec(
            Command(
                Arg("service"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if services is None or len(services) == 0:
            return []
        return services

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry | None:
        services = Service.list(session, cluster_uuid, cluster_user, cluster_pwd)
        if len(services) == 0:
            return None
        return services[0]
