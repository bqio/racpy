from .command import Command, Arg
from ..types import Entry, ListOfEntry
from ..session import Session
from ..handlers import to_list, to_dict
from ..utils import b2ana


class Counter:
    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        return session.exec(
            Command(
                Arg("counter"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )

    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        counter_name: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry:
        return session.exec(
            Command(
                Arg("counter"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(counter_name, "--counter={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )

    @staticmethod
    def update(
        session: Session,
        cluster_uuid: str,
        counter_name: str,
        collection_time: str,
        group: str,
        filter_type: str,
        filter: str,
        duration: bool | None = None,
        cpu_time: bool | None = None,
        memory: bool | None = None,
        read: bool | None = None,
        write: bool | None = None,
        duration_dbms: bool | None = None,
        dbms_bytes: bool | None = None,
        service: bool | None = None,
        call: bool | None = None,
        number_of_active_sessions: bool | None = None,
        number_of_sessions: bool | None = None,
        descr: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("counter"),
                Arg("update"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(counter_name, "--name={}"),
                Arg(collection_time, "--collection-time={}"),
                Arg(group, "--group={}"),
                Arg(filter_type, "--filter-type={}"),
                Arg(filter, "--filter={}"),
                Arg(b2ana(duration), "--duration={}"),
                Arg(b2ana(cpu_time), "--cpu-time={}"),
                Arg(b2ana(memory), "--memory={}"),
                Arg(b2ana(read), "--read={}"),
                Arg(b2ana(write), "--write={}"),
                Arg(b2ana(duration_dbms), "--duration-dbms={}"),
                Arg(b2ana(dbms_bytes), "--dbms-bytes={}"),
                Arg(b2ana(service), "--service={}"),
                Arg(b2ana(call), "--call={}"),
                Arg(b2ana(number_of_active_sessions), "--number-of-active-sessions={}"),
                Arg(b2ana(number_of_sessions), "--number-of-sessions={}"),
                Arg(descr, "--descr={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
        )

    @staticmethod
    def values(
        session: Session,
        cluster_uuid: str,
        counter_name: str,
        counter_object: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        return session.exec(
            Command(
                Arg("counter"),
                Arg("values"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(counter_name, "--counter={}"),
                Arg(counter_object, "--object={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )

    @staticmethod
    def remove(
        session: Session,
        cluster_uuid: str,
        counter_name: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("counter"),
                Arg("remove"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(counter_name, "--name={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
        )

    @staticmethod
    def clear(
        session: Session,
        cluster_uuid: str,
        counter_name: str,
        counter_object: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("counter"),
                Arg("clear"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(counter_name, "--counter={}"),
                Arg(counter_object, "--object={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
        )

    @staticmethod
    def accumulated_values(
        session: Session,
        cluster_uuid: str,
        counter_name: str,
        counter_object: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        return session.exec(
            Command(
                Arg("counter"),
                Arg("accumulated-values"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(counter_name, "--counter={}"),
                Arg(counter_object, "--object={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
