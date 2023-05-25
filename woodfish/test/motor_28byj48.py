import motor.motor_28byj48 as Motor

if __name__ == "__main__":
    motor = Motor([12, 16, 20, 21])
    motor.forward(0.003, 512)
    motor.backward(0.0017, 512)
