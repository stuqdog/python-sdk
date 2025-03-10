import abc
from logging import Logger
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Mapping, Optional, SupportsBytes, SupportsFloat, Union, cast

from typing_extensions import Self

from viam.errors import MethodNotImplementedError
from viam.logging import getLogger
from viam.proto.common import Geometry
from viam.resource.base import ResourceBase

if TYPE_CHECKING:
    from viam.resource.types import API
    from viam.robot.client import RobotClient


ValueTypes = Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, None]


class ComponentBase(abc.ABC, ResourceBase):
    """
    Base component.
    All components must inherit from this class.
    """

    API: ClassVar["API"]

    def __init__(self, name: str, *, logger: Optional[Logger] = None):
        self.name = name
        self.logger = logger if logger is not None else getLogger(f"{self.API}.{name}")

    @classmethod
    def from_robot(cls, robot: "RobotClient", name: str) -> Self:
        """Get the component named ``name`` from the provided robot.

        Args:
            robot (RobotClient): The robot
            name (str): The name of the component

        Returns:
            Self: The component, if it exists on the robot
        """
        component = robot.get_component(cls.get_resource_name(name))
        return cast(cls, component)  # type: ignore

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        raise NotImplementedError()

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        """
        Get all geometries associated with the component, in their current configuration, in the
        `frame <https://docs.viam.com/operate/mobility/define-geometry/>`__ of the component.

        ::

            geometries = await component.get_geometries()

            if geometries:
                # Get the center of the first geometry
                print(f"Pose of the first geometry's centerpoint: {geometries[0].center}")

        Returns:
            List[Geometry]: The geometries associated with the Component.
        """
        raise MethodNotImplementedError("get_geometries")
