import asyncio
import random
from multiprocessing import Queue
from typing import Any, Dict, List

from viam.components.arm import Arm
from viam.components.base import Base
from viam.components.board import Board
from viam.components.board.board import PostProcessor
from viam.components.imu import (IMU, Acceleration, AngularVelocity,
                                 EulerAngles, Orientation)
from viam.components.motor import Motor
from viam.components.pose_tracker import PoseTracker
from viam.components.sensor import Sensor
from viam.components.servo import Servo
from viam.errors import ComponentNotFoundError
from viam.proto.api.common import (AnalogStatus, BoardStatus,
                                   DigitalInterruptStatus, Pose, PoseInFrame)
from viam.proto.api.component.arm import JointPositions


class ExampleArm(Arm):

    def __init__(self, name: str):
        self.position = Pose(
            x=1,
            y=2,
            z=3,
            o_x=2,
            o_y=3,
            o_z=4,
            theta=20,
        )
        self.joint_positions = JointPositions(degrees=[0, 0, 0, 0, 0, 0])
        super().__init__(name)

    async def get_end_position(self) -> Pose:
        return self.position

    async def move_to_position(self, pose: Pose):
        self.position = pose

    async def get_joint_positions(self) -> JointPositions:
        return self.joint_positions

    async def move_to_joint_positions(self, positions: JointPositions):
        self.joint_positions = positions


class ExampleBase(Base):

    def __init__(self, name: str):
        self.position = 0
        self.angle = 0
        self.stopped = True
        super().__init__(name)

    async def move_straight(
        self,
        distance: int,
        velocity: float,
        blocking: bool
    ):
        if distance == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.position += distance
        else:
            self.position -= distance

        self.stopped = False

    async def move_arc(
        self,
        distance: int,
        velocity: float,
        angle: float,
        blocking: bool
    ):
        if distance == 0:
            return await self.spin(angle, velocity, blocking)

        if velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.position += distance
            self.angle += angle
        else:
            self.position -= distance
            self.angle -= angle

        self.stopped = False

    async def spin(self, angle: float, velocity: float, blocking: bool):
        if angle == 0 or velocity == 0:
            return await self.stop()

        if velocity > 0:
            self.angle += angle
        else:
            self.angle -= angle

        self.stopped = False

    async def stop(self):
        self.stopped = True


class ExampleAnalogReader(Board.AnalogReader):

    def __init__(self, name: str, value: int):
        self.value = value
        super().__init__(name)

    async def read(self) -> int:
        return self.value


class ExampleDigitalInterrupt(Board.DigitalInterrupt):

    def __init__(self, name: str):
        self.high = False
        self.last_tick = 0
        self.num_ticks = 0
        self.callbacks: List[Queue] = []
        self.post_processors: List[PostProcessor] = []
        super().__init__(name)

    async def value(self) -> int:
        return self.num_ticks

    async def tick(self, high: bool, nanos: int):
        self.high = high
        self.last_tick = nanos
        self.num_ticks += 1

    async def add_callback(self, queue: Queue):
        self.callbacks.append(queue)

    async def add_post_processor(self, processor: PostProcessor):
        self.post_processors.append(processor)


class ExampleGPIOPin(Board.GPIOPin):

    def __init__(self, name: str):
        self.high = False
        self.pwm = 0.0
        self.pwm_freq = 0
        super().__init__(name)

    async def get(self) -> bool:
        return self.high

    async def set(self, high: bool):
        self.high = high

    async def get_pwm(self) -> float:
        return self.pwm

    async def set_pwm(self, duty_cycle: float):
        self.pwm = duty_cycle

    async def get_pwm_frequency(self) -> int:
        return self.pwm_freq

    async def set_pwm_frequency(self, frequency: int):
        self.pwm_freq = frequency


class ExampleBoard(Board):

    def __init__(self,
                 name: str,
                 analog_readers: Dict[str, Board.AnalogReader],
                 digital_interrupts: Dict[str, Board.DigitalInterrupt],
                 gpio_pins: Dict[str, Board.GPIOPin]
                 ):
        self.analog_readers = analog_readers
        self.digital_interrupts = digital_interrupts
        self.gpios = gpio_pins
        super().__init__(name)

    async def analog_reader_by_name(self, name: str) -> Board.AnalogReader:
        try:
            return self.analog_readers[name]
        except KeyError:
            raise ComponentNotFoundError('Board.AnalogReader', name)

    async def digital_interrupt_by_name(
        self,
        name: str
    ) -> Board.DigitalInterrupt:
        try:
            return self.digital_interrupts[name]
        except KeyError:
            raise ComponentNotFoundError('Board.DigitalInterrupt', name)

    async def gpio_pin_by_name(self, name: str) -> Board.GPIOPin:
        try:
            return self.gpios[name]
        except KeyError:
            raise ComponentNotFoundError('Board.GPIOPin', name)

    async def analog_reader_names(self) -> List[str]:
        return [key for key in self.analog_readers.keys()]

    async def digital_interrupt_names(self) -> List[str]:
        return [key for key in self.digital_interrupts.keys()]

    async def status(self) -> BoardStatus:
        return BoardStatus(
            analogs={
                name: AnalogStatus(value=await analog.read())
                for (name, analog) in self.analog_readers.items()
            },
            digital_interrupts={
                name: DigitalInterruptStatus(value=await di.value())
                for (name, di) in self.digital_interrupts.items()
            }
        )

    async def model_attributes(self) -> Board.Attributes:
        return Board.Attributes(remote=True)


class ExampleIMU(IMU):

    async def read_acceleration(self) -> Acceleration:
        return Acceleration(
            x_mm_per_sec_per_sec=random.random(),
            y_mm_per_sec_per_sec=random.random(),
            z_mm_per_sec_per_sec=random.random()
        )

    async def read_angular_velocity(self) -> AngularVelocity:
        return AngularVelocity(
            x_degs_per_sec=random.random(),
            y_degs_per_sec=random.random(),
            z_degs_per_sec=random.random()
        )

    async def read_orientation(self) -> Orientation:
        angles = EulerAngles(
            roll_deg=random.random(),
            pitch_deg=random.random(),
            yaw_deg=random.random()
        )
        return Orientation(euler_angles=angles)


class ExampleMotor(Motor):

    def __init__(self, name: str):
        self.position: float = 0
        self.power = 0
        self.powered = False
        self.task = None
        super().__init__(name)

    async def run_continuously(self, rpm: float):
        rps = rpm/60
        while True:
            await asyncio.sleep(1)
            self.position += rps

    async def set_power(self, power: float):
        self.power = power
        self.powered = power != 0
        if self.powered:
            self.task = asyncio.create_task(self.run_continuously(power))
        else:
            if self.task:
                self.task.cancel()

    async def go_for(self, rpm: float, revolutions: float):
        if self.task:
            self.task.cancel()
        target = 0
        rps = rpm/60
        if rpm > 0:
            target = self.position + revolutions
        if rpm < 0:
            target = self.position - revolutions
        self.powered = True
        while abs(self.position-target) > 0.01:
            await asyncio.sleep(1)
            self.position += rps
        self.powered = False

    async def go_to(self, rpm: float, position_revolutions: float):
        if self.task:
            self.task.cancel()
        distance = position_revolutions - self.position
        rps = rpm/60
        self.powered = True
        while distance > 0:
            await asyncio.sleep(1)
            distance -= abs(rps)
            self.position += rps
        self.powered = False

    async def reset_zero_position(self, offset: float):
        if (self.position > 0 and offset > 0) \
                or (self.position < 0 and offset < 0):
            self.position = offset
        else:
            self.position += offset
        self.powered = False

    async def get_position(self) -> float:
        return self.position

    async def get_features(self) -> Motor.Features:
        return {'position_reporting': True}

    async def is_powered(self) -> bool:
        return self.powered


class ExamplePoseTracker(PoseTracker):

    async def get_poses(self, body_names: List[str]) -> Dict[str, PoseInFrame]:
        all_poses = {
            "body1": PoseInFrame(
                reference_frame='0',
                pose=Pose(
                    x=1,
                    y=2,
                    z=3,
                    o_x=2,
                    o_y=3,
                    o_z=4,
                    theta=20
                )
            ),
            "body2": PoseInFrame(
                reference_frame='0',
                pose=Pose(
                    x=3,
                    y=2,
                    z=3,
                    o_x=4,
                    o_y=3,
                    o_z=4,
                    theta=40
                )
            )
        }
        return {k: v for k, v in all_poses.items() if k in body_names}


class ExampleSensor(Sensor):

    def __init__(self, name: str):
        self.num_readings = random.randint(1, 10)
        super().__init__(name)

    async def get_readings(self) -> List[Any]:
        return [random.random() for _ in range(self.num_readings)]


class ExampleServo(Servo):

    def __init__(self, name: str):
        self.angle = 0
        super().__init__(name)

    async def move(self, angle: int):
        self.angle = angle

    async def get_position(self) -> int:
        return self.angle
