import abc
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from client.views.view import View

ViewType = TypeVar('ViewType', bound="View")


class Controller(abc.ABC):
    def __init__(self):
        self.view = None

    @abc.abstractmethod
    def set_view(self, view: ViewType):
        pass
