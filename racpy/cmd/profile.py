from .command import Command, Arg, Flag
from ..session import Session
from ..types import Entry, ListOfEntry, EntryUUID
from ..handlers import to_list, to_dict


class Profile:
    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> ListOfEntry:
        profiles = session.exec(
            Command(
                Arg("profile"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            ),
            to_list,
        )
        if profiles is None or len(profiles) == 0:
            return []
        return profiles

    @staticmethod
    def update(
        session: Session,
        cluster_uuid: str,
        profile_name: str,
        descr: str | None = None,
        config: bool | None = None,
        priv: bool | None = None,
        full_privileged_mode: bool | None = None,
        privileged_mode_roles: str | None = None,
        crypto: bool | None = None,
        right_extension: bool | None = None,
        right_extension_definition_roles: str | None = None,
        all_modules_extension: bool | None = None,
        modules_available_for_extension: str | None = None,
        modules_not_available_for_extension: str | None = None,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> Entry:
        pass

    @staticmethod
    def remove(
        session: Session,
        cluster_uuid: str,
        profile_name: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ) -> None:
        return session.exec(
            Command(
                Arg("profile"),
                Arg("remove"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(profile_name, "--name={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )


class ProfileACLDirectory:
    pass


class ProfileACLCOM:
    pass


class ProfileACLAddin:
    pass


class ProfileACLModule:
    pass


class ProfileACLApp:
    pass


class ProfileACLInet:
    pass
