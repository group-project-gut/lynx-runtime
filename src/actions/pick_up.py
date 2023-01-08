from typing import Dict

from src.actions.action import Action
from src.actions.destroy import Destroy
from src.common.point import Point
from src.common.serializable import Properties
from src.objects.interactive_object import InteractiveObject
from src.objects.object import Object


class PickUp(Action):
    base: str
    properties: Properties
    agent: 'Agent'
    objects_dict: Dict[int, Object]
    agent_position: Point
    object_id: int  # id of the object being picked up

    def __init__(self, agent: 'Agent', object_id: int) -> None:
        super().__init__()
        self.agent = agent
        self.agent_position = agent.properties.position
        self.objects_dict = agent.scene.objects_dict
        self.object_id = object_id

    def execute(self) -> None:
        self.__pick_up()

    def __pick_up(self):
        object = self.objects_dict.get(self.object_id)
        if self.__can_pick_up(object):
            Destroy(object).execute()
            self.agent.items.append(object.properties.id)
            self.agent.scene.objects_map[object.properties.position].remove(self)
        else:
            print(f"Unable to pick up object with id {self.object_id}")

    def __can_pick_up(self, object):
        if (object.properties.position.__eq__(self.agent_position) and
                issubclass(object.__class__, InteractiveObject) and
                object.can_pick_up):
            return True
        return False
