from typing import List
from .command import Command, Arg
from ..session import Session
from ..handlers import to_list
from ..utils import list_to_dc, to_dc
from ..schemas import ServiceSchema


class Service:
    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> List[ServiceSchema]:
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
        return list_to_dc(services, ServiceSchema)

    @staticmethod
    def first(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ServiceSchema | None:
        services = Service.list(session, cluster_uuid, cluster_user, cluster_pwd)
        if len(services) == 0:
            return None
        return services[0]
