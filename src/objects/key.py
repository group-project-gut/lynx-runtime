from src.common.point import Point
from src.common.serializable import Properties
from src.objects.object import Object


class Key(Object):
    """
    `Object` existing in a `scene`.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool

    def __init__(self, position: Point, scene: 'Scene') -> None:
        super.__init__(position, scene)

    def on_collision(self, other) -> None:
        self.scene.player.items.append(self)
