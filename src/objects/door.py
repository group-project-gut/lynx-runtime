from src.objects.interactive_object import InteractiveObject
from src.common.point import Point
from src.common.serializable import Properties
from src.objects.agent import Agent
from src.objects.object import Object


class Door(InteractiveObject):
    """
    `Object` interacting with a key
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool
    keys: list

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(position, scene)
        self.keys = []
        self.can_pick_up = False

    def on_collision(self, other) -> None:
        if isinstance(other, Agent) and self.can_open(other.items):
            pass

    def can_open(self, items: list):
        return any(item in self.keys for item in items)