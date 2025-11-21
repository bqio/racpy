from enum import StrEnum, IntEnum


class AuthMethod(StrEnum):
    PWD = "pwd"
    OS = "os"


class LoadBalancingMode(StrEnum):
    PERFORMANCE = "performance"
    MEMORY = "memory"


class SecurityLevel(IntEnum):
    DISABLED = 0
    ONLY_CONNECTION = 1
    ALWAYS = 2


class DBMS(StrEnum):
    MSSQL_SERVER = "MSSQLServer"
    POSTGRE_SQL = "PostgreSQL"
    IBM_DB2 = "IBMDB2"
    ORACLE_DATABASE = "OracleDatabase"


class DateOffset(IntEnum):
    OFS_0 = 0
    OFS_2000 = 2000


class Using(StrEnum):
    MAIN = "main"
    NORMAL = "normal"


class DedicateManagers(StrEnum):
    ALL = "all"
    NONE = "none"
