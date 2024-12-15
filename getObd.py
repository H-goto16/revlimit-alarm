import time
import obd
from obd import OBDStatus

def get_obd_data():
    connection = obd.OBD()
    if connection.status() == OBDStatus.CAR_CONNECTED:
        try:
            while True:
                # エンジン回転数 & 車速を取得
                rpm = connection.query(obd.commands.RPM).value.magnitude
                speed = connection.query(obd.commands.SPEED).value.magnitude

                # 値をyield
                yield rpm, speed
                
        except KeyboardInterrupt:
            connection.close()
    else:
        raise ConnectionError("車両に接続できませんでした。")

# 使用例
if __name__ == "__main__":
    try:
        for rpm, speed in get_obd_data():
            print(f'rpm: {rpm}, speed: {speed}')
    except ConnectionError as e:
        print(e)

