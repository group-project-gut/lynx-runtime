from src.actions.action import Action
from src.common.serializable import Properties
from src.objects.object import Object


class Die(Action):
    """
    Simple action for dying.
    """
    base: str
    properties: Properties
    object: Object

    def __init__(self, object: Object) -> None:
        super().__init__()
        self.properties.object_id = object.properties.id
        self.object = object

    def execute(self) -> None:
        pass
