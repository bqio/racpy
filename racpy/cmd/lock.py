from typing import List
from .command import Command, Arg
from ..session import Session
from ..handlers import to_list
from ..utils import list_to_dc
from ..schemas import LockSchema


class Lock:
    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        infobase_uuid: str,
        connection_uuid: str,
        user_session_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> List[LockSchema]:
        locks = session.exec(
            Command(
                Arg("lock"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(infobase_uuid, "--infobase={}"),
                Arg(connection_uuid, "--connection={}"),
                Arg(user_session_uuid, "--session={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if locks is None or len(locks) == 0:
            return []
        return list_to_dc(locks, LockSchema)
