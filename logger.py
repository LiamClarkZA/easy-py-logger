import logging
import time
import serial

if __name__ == "__main__":
    filename = "./file_{t}.log".format(
        t=time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
    f = open(filename, "w+")
    f.close()
    logging.basicConfig(filename=filename, level=logging.DEBUG,
                        format="%(asctime)s:" + logging.BASIC_FORMAT)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter(
        "%(asctime)s:" + logging.BASIC_FORMAT))
    logging.getLogger().addHandler(console)
    logger = logging.getLogger(__name__)
    logger.info("Logging Beginning")

    port = input("Enter com port: ")
    baud = int(input("Enter baud rate: "))
    rate = 1/int(input("Enter serial read frequency: "))

    ser = serial.Serial(port, baud)
    while(True):
            time.sleep(rate)
            logger.info(ser.readline())
