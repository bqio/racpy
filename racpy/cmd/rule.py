from .command import Command, Arg, Flag
from ..session import Session
from ..types import Entry, ListOfEntry, EntryUUID
from ..handlers import to_list, to_dict


class Rule:
    @staticmethod
    def apply(
        session: Session,
        cluster_uuid: str,
        partial: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("rule"),
                Arg("apply"),
                Arg(cluster_uuid, "--cluster={}"),
                Flag(partial, "--partial"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )

    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        server_uuid: str,
        rule_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry:
        rule = session.exec(
            Command(
                Arg("rule"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Arg(rule_uuid, "--rule={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )
        return rule

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        server_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        rules = session.exec(
            Command(
                Arg("rule"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if rules is None or len(rules) == 0:
            return []
        return rules

    @staticmethod
    def insert(
        session: Session,
        cluster_uuid: str,
        server_uuid: str,
        position: int,
        object_type: str | None = None,
        infobase_name: str | None = None,
        rule_type: str | None = None,
        application_ext: str | None = None,
        priority: int | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> EntryUUID:
        rule = session.exec(
            Command(
                Arg("rule"),
                Arg("insert"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Arg(position, "--position={}"),
                Arg(object_type, "--object-type={}"),
                Arg(infobase_name, "--infobase-name={}"),
                Arg(rule_type, "--rule-type={}"),
                Arg(application_ext, "--application-ext={}"),
                Arg(priority, "--priority={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )
        return rule["rule"]

    @staticmethod
    def update(
        session: Session,
        cluster_uuid: str,
        server_uuid: str,
        rule_uuid: str,
        position: int,
        object_type: str | None = None,
        infobase_name: str | None = None,
        rule_type: str | None = None,
        application_ext: str | None = None,
        priority: int | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("rule"),
                Arg("update"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Arg(rule_uuid, "--rule={}"),
                Arg(position, "--position={}"),
                Arg(object_type, "--object-type={}"),
                Arg(infobase_name, "--infobase-name={}"),
                Arg(rule_type, "--rule-type={}"),
                Arg(application_ext, "--application-ext={}"),
                Arg(priority, "--priority={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
        )

    @staticmethod
    def remove(
        session: Session,
        cluster_uuid: str,
        server_uuid: str,
        rule_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("rule"),
                Arg("remove"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Arg(rule_uuid, "--rule={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )
