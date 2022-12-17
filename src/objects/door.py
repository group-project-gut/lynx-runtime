from src.common.point import Point
from src.common.serializable import Properties
from src.objects.agent import Agent
from src.objects.object import Object


class Door(Object):
    """
    `Object` interacting with a key
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool
    matching_key: int

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(position, scene)

    def match_key(self, key):
        self.matching_key = key.properties.id

    def on_collision(self, other) -> None:
        if isinstance(other, Agent):
            print("match key")
