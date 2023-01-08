from typing import Dict, List

from src.actions.action import Action
from src.common.point import Point
from src.common.serializable import Properties
from src.objects.interactive_object import InteractiveObject
from src.objects.object import Object


class NearbyObjects(Action):
    base: str
    properties: Properties
    agent_position: Point
    objects_map: Dict[Point, List[Object]]

    def __init__(self, agent: 'Agent') -> None:
        super().__init__()
        self.objects_map = agent.scene.objects_map
        self.agent_position = agent.properties.position
        self.properties.agent_id = agent.properties.id

    def execute(self) -> None:
        self.properties.nearby_objects = self.__get_nearby_objects()
        self.log()

    def __get_nearby_objects(self):
        object_position = self.agent_position.__add__(Point(1, 0))
        objects = list(
            filter(lambda x: (issubclass(x.__class__, InteractiveObject)), self.objects_map.get(object_position)))
        return list(map(lambda x: (
            {
                'class_name': x.__class__.__name__,
                'id': x.properties.id,
                'position': x.properties.position
            }
        ), objects))
