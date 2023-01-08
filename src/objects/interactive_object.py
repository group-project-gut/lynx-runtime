from src.actions.action import Action
from src.actions.destroy import Destroy
from src.common.point import Point
from src.common.serializable import Properties
from src.objects.object import Object


class InteractiveObject(Object):
    """
    Action triggered when any objects interact with each other
    """
    base: str
    properties: Properties
    can_pick_up: bool

    def __init__(self, position: Point, scene: 'Scene') -> None:
        super().__init__(position, scene)

    def interactive(self) -> None:
        pass

    def pick_up(self, other) -> None:
        Destroy(self).execute()
        other.items.append(self.properties.id)
        self.scene.objects_map[self.properties.position].remove(self)