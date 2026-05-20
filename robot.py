import wpilib

class MyRobot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()
        self.leftDrive = wpilib.PWMSparkMax(0)
        self.rightDrive = wpilib.PWMSparkMax(1)
        self.robotDrive = wpilib.DifferentialDrive(self.leftDrive, self.rightDrive)
        self.controller = wpilib.NiDsXboxController(0)
        self.timer = wpilib.Timer()

        self.rightDrive.setInverted(True)

    def autonomousInit(self):
        self.timer.restart()

    def autonomousPeriodic(self):
        if self.timer.get() < 2.0:
            self.robotDrive.arcadeDrive(0.5, 0, squareInputs=False)
        else:
            self.robotDrive.stopMotor()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.robotDrive.arcadeDrive(
            -self.controller.getLeftY(), -self.controller.getRightX()
        )

    def utilityInit(self):
        pass

    def utilityPeriodic(self):
        pass