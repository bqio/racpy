from typing import List
from .command import Command, Arg
from ..session import Session
from ..handlers import to_list
from ..utils import list_to_dc
from ..schemas import ServiceSchema


class Service:
    """Режим администрирования сервиса менеджера кластера."""

    @staticmethod
    def list(
        session: Session,
        cluster: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> List[ServiceSchema]:
        """
        Получение списка информации о сервисах.

        Args:
            session (Session): Уникальная сессия подключения.
            cluster (str): Идентификатор кластера серверов.
            cluster_user (str | None): Имя администратора кластера.
            cluster_pwd (str | None): Пароль администратора кластера.

        Returns:
            List[ServiceSchema]: Список сервисов.
        """
        services = session.exec(
            Command(
                Arg("service"),
                Arg(cluster, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
                Arg("list"),
            ),
            to_list,
        )
        if services is None or len(services) == 0:
            return []
        return list_to_dc(services, ServiceSchema)
