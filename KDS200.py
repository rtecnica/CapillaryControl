import serial
import time

class KDS200:

    TIME_DEFAULT  = 100.0
    TIME_GET_DATA = 70.0 + TIME_DEFAULT
    TIME_GET_IDN  = 300.0 + TIME_DEFAULT

    def __init__(self, port):
        # Configuración
        self.ser = serial.Serial(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )

        self.ser.isOpen()

    def run(self):
        cmd = 'run\r\n'
        self.ser.write(cmd.encode())

    def stop(self):
        cmd = 'stop\r\n'
        self.ser.write(cmd.encode())

    def setDiameter(self, dia):
        cmd = 'dia '+ dia +' \r\n'
        self.ser.write(cmd.encode())

    def setRate(self, number, volUnit, timeUnit):
        units = volUnit+'/'+timeUnit
        cmd = 'ratei '+number+' '+units+'\r\n'
        self.ser.write(cmd.encode())

    def setVol(self,vol,units):
        cmd = 'voli '+vol+' '+units+'\r\n'
        self.ser.write(cmd.encode())


    def getErr(self):
        return self._sendCMD('error?', self.TIME_GET_DATA)

    def getDiameter(self):
        return self._sendCMD('dia?', self.TIME_GET_DATA)

    def getRate(self):
        return self._sendCMD('ratei?', self.TIME_GET_DATA)

    def getVol(self):
        return self._sendCMD('vol?', self.TIME_GET_DATA)

    def _sendCMD(self, cmd, t = 1000.0):

        cmd += '\r\n'
        self.ser.write(cmd.encode())

        out = ''
        # esperar 1 seg para recibir la respuesta
        # de la fuente de poder
        time.sleep(t / 1000.0)
        while self.ser.inWaiting() > 0:
            out += self.ser.read(1).decode("ASCII")

        return out
