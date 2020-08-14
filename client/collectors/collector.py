import logging

from client.collectors.Volatile_Data.collector_base import CollectorBase
from client.collectors.Volatile_Data.connection_info import ConnectionInfo
from client.collectors.Volatile_Data.date_info import DateInfo
from client.collectors.Volatile_Data.disk_space_info import DiskSpaceInfo
from client.collectors.Volatile_Data.interface_info import InterfaceInfo
from client.collectors.Volatile_Data.loadable_kernel_modules_info import LoadableKerenlModuleInfo
from client.collectors.Volatile_Data.logging_current_info import LogginCurrentInfo
from client.collectors.Volatile_Data.logging_last_info import LogginLastInfo
from client.collectors.Volatile_Data.mount_info import MountInfo
from client.collectors.Volatile_Data.open_files_info import OpenFilesInfo
from client.collectors.Volatile_Data.password_info import PasswordInfo
from client.collectors.Volatile_Data.process_info import ProcessInfo
from client.collectors.Volatile_Data.routing_info import RoutingInfo
from client.collectors.Volatile_Data.shadow_info import ShadowInfo
from client.collectors.Volatile_Data.system_info import SystemInfo
from client.utils.message import Message


class Collector:

    def __init__(self):
        self._collector_volatile_data = CollectorVolatileData()

    def register_volatile_data(self):
        self._collector_volatile_data.register_all()

    def run_collectors(self):
        self._collector_volatile_data.run_all()


class CollectorVolatileData:

    def __init__(self):
        self._collectors = []
        self._log = logging.getLogger("CollectorVolatileData")

    def register_all(self):
        self._collectors.append(ConnectionInfo())
        self._collectors.append(DateInfo())
        self._collectors.append(DiskSpaceInfo())
        self._collectors.append(InterfaceInfo())
        self._collectors.append(LoadableKerenlModuleInfo())
        self._collectors.append(LogginCurrentInfo())
        self._collectors.append(LogginLastInfo())
        self._collectors.append(MountInfo())
        self._collectors.append(OpenFilesInfo())
        self._collectors.append(PasswordInfo())
        self._collectors.append(ProcessInfo())
        self._collectors.append(RoutingInfo())
        # self._collectors.append(ShadowInfo())
        # self._collectors.append(SystemInfo())

    def run_all(self):
        for collector in self._collectors:
            self._log.info("Calling collector %s" % collector)
            output = collector.collect()
            Message.send_message(collector, output)

