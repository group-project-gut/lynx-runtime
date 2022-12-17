from src.actions.destroy import Destroy
from src.common.point import Point
from src.common.serializable import Properties
from src.objects.door import Door
from src.objects.object import Object


class Key(Object):
    """
    `Object` existing in a `scene`.
    """
    base: str
    properties: Properties
    scene: 'Scene'
    walkable: bool
    fit_door: int

    def __init__(self, scene: 'Scene', position: Point) -> None:
        super().__init__(position, scene)

    def fit_door(self, door: Door):
        door.keys.append(self.properties.id)
        self.fit_door = door.properties.id

    def on_collision(self, other) -> None:
        Destroy(self).execute()
        other.items.append(self.properties.id)
        self.scene.objects_map[self.properties.position].remove(self)
