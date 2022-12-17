from src.actions.action import Action
from src.common.serializable import Properties
from src.objects.object import Object


class InteractiveObject(Action):
    """
    Action triggered when any objects interact with each other
    """
    base: str
    properties: Properties
    object: Object

    def __init__(self, object: Object):
        super().__init__()
        self.object = object

    def execute(self) -> None:
        self.log()