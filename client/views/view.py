import abc
from typing import TYPE_CHECKING, TypeVar, Generic

if TYPE_CHECKING:
    from ..controllers import Controller

ControllerType = TypeVar('ControllerType', bound="Controller")


class View(abc.ABC):
    def __init__(self, parent):
        self.parent = parent
        self.controller = None

    def set_controller(self, controller: ControllerType):
        self.controller = controller
        self._bind_commands()

    @abc.abstractmethod
    def _create_widgets(self):
        pass

    @abc.abstractmethod
    def _set_layout(self):
        pass

    @abc.abstractmethod
    def _bind_commands(self):
        pass
