from typing import List
from .command import Command, Arg, Flag
from ..session import Session
from ..handlers import to_list, to_dict
from ..utils import list_to_dc, to_dc
from ..schemas import ProcessSchema, ProcessWithLicensesSchema


class Process:
    @staticmethod
    def info(
        session: Session,
        cluster_uuid: str,
        process_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ProcessSchema | ProcessWithLicensesSchema:
        process = session.exec(
            Command(
                Arg("process"),
                Arg("info"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(process_uuid, "--process={}"),
                Flag(licenses, "--licenses"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_dict,
        )
        if licenses:
            return to_dc(process, ProcessWithLicensesSchema)
        return to_dc(process, ProcessSchema)

    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        server_uuid: str,
        licenses: bool = False,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> List[ProcessSchema | ProcessWithLicensesSchema]:
        processes = session.exec(
            Command(
                Arg("process"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(server_uuid, "--server={}"),
                Flag(licenses, "--licenses"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if processes is None or len(processes) == 0:
            return []
        if licenses:
            return list_to_dc(processes, ProcessWithLicensesSchema)
        return list_to_dc(processes, ProcessSchema)
