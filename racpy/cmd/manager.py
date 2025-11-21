from typing import List
from .command import Command, Arg
from ..session import Session
from ..handlers import to_list, to_dict
from ..utils import list_to_dc, to_dc
from ..schemas import ManagerSchema


class Manager:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        manager_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ManagerSchema:
        manager = session.exec(
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
        return to_dc(manager, ManagerSchema)

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> List[ManagerSchema]:
        managers = session.exec(
            Command(
                Arg("manager"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if managers is None or len(managers) == 0:
            return []
        return list_to_dc(managers, ManagerSchema)
