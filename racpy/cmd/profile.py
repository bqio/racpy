from .command import Command, Arg
from ..session import Session
from ..utils import b2yn


class Profile:
    @staticmethod
    def list(
        session: Session,
        cluster_uuid: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.exec(
            Command(
                Arg("profile"),
                Arg("list"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        ).to_list()

    @staticmethod
    def update(
        session: Session,
        cluster_uuid: str,
        name: str,
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
    ):
        return session.call(
            Command(
                Arg("profile"),
                Arg("update"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(name, "--name={}"),
                Arg(descr, "--descr={}"),
                Arg(b2yn(config), "--config={}"),
                Arg(b2yn(priv), "--priv={}"),
                Arg(b2yn(full_privileged_mode), "--full-privileged-mode={}"),
                Arg(privileged_mode_roles, "--privileged-mode-roles={}"),
                Arg(b2yn(crypto), "--crypto={}"),
                Arg(b2yn(right_extension), "--right-extension={}"),
                Arg(
                    right_extension_definition_roles,
                    "--right-extension-definition-roles={}",
                ),
                Arg(b2yn(all_modules_extension), "--all-modules-extension={}"),
                Arg(
                    modules_available_for_extension,
                    "--modules-available-for-extension={}",
                ),
                Arg(
                    modules_not_available_for_extension,
                    "--modules-not-available-for-extension={}",
                ),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )

    @staticmethod
    def remove(
        session: Session,
        cluster_uuid: str,
        name: str,
        cluster_user: str | None = None,
        cluster_pwd: str | None = None,
    ):
        return session.call(
            Command(
                Arg("profile"),
                Arg("remove"),
                Arg(cluster_uuid, "--cluster={}"),
                Arg(name, "--name={}"),
                Arg(cluster_user, "--cluster-user={}"),
                Arg(cluster_pwd, "--cluster-pwd={}"),
            )
        )

    class ACL:
        class Directory:
            @staticmethod
            def list(
                session: Session,
                cluster_uuid: str,
                name: str,
                access: str = "list",
                cluster_user: str | None = None,
                cluster_pwd: str | None = None,
            ):
                return session.exec(
                    Command(
                        Arg("profile"),
                        Arg("acl"),
                        Arg(cluster_uuid, "--cluster={}"),
                        Arg(name, "--name={}"),
                        Arg(cluster_user, "--cluster-user={}"),
                        Arg(cluster_pwd, "--cluster-pwd={}"),
                        Arg("directory"),
                        Arg("list"),
                        Arg(access, "--access={}"),
                    )
                ).to_list()

            @staticmethod
            def update(
                session: Session,
                cluster_uuid: str,
                name: str,
                alias: str,
                descr: str | None = None,
                physicalPath: str | None = None,
                allowedRead: bool | None = None,
                allowedWrite: bool | None = None,
                access: str = "list",
                cluster_user: str | None = None,
                cluster_pwd: str | None = None,
            ):
                return session.call(
                    Command(
                        Arg("profile"),
                        Arg("acl"),
                        Arg(cluster_uuid, "--cluster={}"),
                        Arg(name, "--name={}"),
                        Arg(cluster_user, "--cluster-user={}"),
                        Arg(cluster_pwd, "--cluster-pwd={}"),
                        Arg("directory"),
                        Arg("update"),
                        Arg(alias, "--alias={}"),
                        Arg(descr, "--descr={}"),
                        Arg(physicalPath, "--physicalPath={}"),
                        Arg(b2yn(allowedRead), "--allowedRead={}"),
                        Arg(b2yn(allowedWrite), "--allowedWrite={}"),
                        Arg(access, "--access={}"),
                    )
                )

            @staticmethod
            def remove(
                session: Session,
                cluster_uuid: str,
                profile_name: str,
                alias: str,
                access: str = "list",
                cluster_user: str | None = None,
                cluster_pwd: str | None = None,
            ):
                return session.call(
                    Command(
                        Arg("profile"),
                        Arg("acl"),
                        Arg("directory"),
                        Arg("remove"),
                        Arg(cluster_uuid, "--cluster={}"),
                        Arg(profile_name, "--name={}"),
                        Arg(alias, "--alias={}"),
                        Arg(access, "--access={}"),
                        Arg(cluster_user, "--cluster-user={}"),
                        Arg(cluster_pwd, "--cluster-pwd={}"),
                    )
                )

        class COM:
            pass

        class Addin:
            pass

        class Module:
            pass

        class App:
            pass

        class Inet:
            pass
