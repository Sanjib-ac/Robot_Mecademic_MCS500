import mecademicpy.robot as mdr
import mecademicpy.robot_initializer as initializer
import mecademicpy.tools as tools

robot = mdr.Robot()


def status(robt: mdr.Robot):
    stus = robt.GetStatusRobot(synchronous_update=False)
    print(f'Status: {stus}')


if __name__ == "__main__":
    address = '192.168.1.150'
    robot = mdr.Robot()
    robot.Connect(address=address)
    robot.ActivateRobot()
    robot.WaitHomed()
    robot.MoveJoints(0, 0, 0, 0)
    robot.WaitIdle(60)
    robot.Delay(1)
    # robot.WaitIdle(60)
    robot.DeactivateRobot()

    # with initializer.RobotWithTools() as robot:
    #     robot.Connect(address=address)
    #     robot.ActivateRobot()
    #     status(robot)
    #
    #     # initializer.reset_motion_queue(robot, activate_home=True)
    #     robot.WaitHomed()
    #     robot.MoveJoints(90, 0, 0, 0)
    #     robot.WaitIdle(60)
    #     robot.Delay(1)
    #     # robot.WaitIdle(60)
    #     robot.DeactivateRobot()
