from dataclasses import dataclass


@dataclass
class AgentAdminSchema:
    name: str
    auth: str
    os_user: str
    descr: str


@dataclass
class ClusterAdminSchema:
    name: str
    auth: str
    os_user: str
    descr: str


@dataclass
class ClusterSchema:
    cluster: str
    host: str
    port: int
    name: str
    expiration_timeout: int
    lifetime_limit: int
    max_memory_size: int
    max_memory_time_limit: int
    security_level: int
    session_fault_tolerance_level: int
    load_balancing_mode: str
    errors_count_threshold: int
    kill_problem_processes: int
    kill_by_memory_with_dump: int
    allow_access_right_audit_events_recording: int
    ping_period: int
    ping_timeout: int
    restart_schedule: str


@dataclass
class ServerSchema:
    server: str
    agent_host: str
    agent_port: str
    port_range: str
    name: str
    using: str
    dedicate_managers: str
    infobases_limit: int
    memory_limit: int
    connections_limit: int
    safe_working_processes_memory_limit: int
    safe_call_memory_limit: int
    cluster_port: int
    critical_total_memory: int
    temporary_allowed_total_memory: int
    temporary_allowed_total_memory_time_limit: int
    service_principal_name: str
    restart_schedule: str


@dataclass
class ProcessSchema:
    process: str
    host: str
    port: int
    pid: int
    turned_on: str
    running: str
    started_at: str
    use: str
    available_perfomance: int
    capacity: int
    connections: int
    memory_size: int
    memory_excess_time: int
    selection_size: int
    avg_call_time: float
    avg_db_call_time: float
    avg_lock_call_time: float
    avg_server_call_time: float
    avg_threads: float
    reserve: str


@dataclass
class ProcessWithLicensesSchema:
    process: str
    host: str
    port: int
    pid: int
    full_name: str
    series: int
    issued_by_server: str
    license_type: str
    net: str
    max_users_all: int
    max_users_cur: int
    rmngr_address: str
    rmngr_port: int
    rmngr_pid: int
    short_presentation: str
    full_presentation: str


@dataclass
class InfobaseShortSchema:
    infobase: str
    name: str
    descr: str


@dataclass
class InfobaseSchema:
    infobase: str
    name: str
    dbms: str
    db_server: str
    db_name: str
    db_user: str
    security_level: int
    license_distribution: str
    scheduled_jobs_deny: str
    sessions_deny: str
    denied_from: str
    denied_message: str
    denied_parameter: str
    denied_to: str
    permission_code: str
    external_session_manager_connection_string: str
    external_session_manager_required: str
    security_profile_name: str
    safe_mode_security_profile_name: str
    reserve_working_processes: str
    descr: str
    disable_local_speech_to_text: str
    configuration_unload_delay_by_working_process_without_active_users: int
    minimum_scheduled_jobs_start_period_without_active_users: int
    maximum_scheduled_jobs_start_shift_without_active_users: int


@dataclass
class ConnectionShortSchema:
    connection: str
    conn_id: int
    host: str
    process: str
    infobase: str
    application: str
    connected_at: str
    session_number: int
    blocked_by_ls: int


@dataclass
class ConnectionSchema:
    connection: str
    conn_id: int
    user_name: str
    host: str
    app_id: str
    connected_at: str
    thread_mode: str
    ib_conn_mode: str
    db_conn_mode: str
    blocked_by_dbms: int
    bytes_all: int
    bytes_last_5min: int
    calls_all: int
    calls_last_5min: int
    dbms_bytes_all: int
    dbms_bytes_last_5min: int
    db_proc_info: str
    db_proc_took: int
    db_proc_took_at: str
    duration_all: int
    duration_all_dbms: int
    duration_current: int
    duration_current_dbms: int
    duration_last_5min: int
    duration_last_5min_dbms: int
    memory_current: int
    memory_last_5min: int
    memory_total: int
    read_current: int
    read_last_5min: int
    read_total: int
    write_current: int
    write_last_5min: int
    write_total: int
    duration_current_service: int
    duration_last_5min_service: int
    duration_all_service: int
    current_service_name: str
