from greenthumb_core.core.task.serial_pin_binary_control import SerialPinBinaryControl

a = SerialPinBinaryControl()

print("Run 1")
a.run()
a.cleanup()
