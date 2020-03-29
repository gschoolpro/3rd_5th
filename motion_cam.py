# モジュールのインポート
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import wiringpi as pi
import picamera

delay = ___     # 休止時間を0.2秒に設定
END = ___        # 終了時間を10秒に設定
sensor_pin = ___ # 人感センサをGPIO18に接続

# カメラを使用する設定
camera = picamera.PiCamera()
# 画像サイズを400 x 400に
camera.resolution = (___, ___)

# 初期設定
def sensor_init():
    GPIO.setmode(GPIO.BCM)
    pi.wiringPiSetupGpio()
    pi.pinMode(sensor_pin, pi.INPUT)

# 動作設定
def main():
    sensor_init()
    # 動画の保存ファイル名の初期化
    video_count = __
    # センサ検知のカウント回数の初期化
    count = __
    # 開始時間の代入
    start = time.time()
    # 無限ループ
    while True:
        print('start recording')
        time.sleep(1)
        # 動画の保存ファイル名の設定
        video_file = '{:03d}.h264'.format(video_count)
        # 録画開始
        camera.start_recording(video_file)
        # ファイル名の変更
        video_count = video_count + 1

        # センサが感知したとき
        if( pi.digitalRead( sensor_pin ) == pi.HIGH ):
            # count を +1 する
            count = ____________
            time.sleep(delay)
            print(count)
        # センサが感知しなかったとき
        elif( pi.digitalRead( sensor_pin ) == pi.LOW ):
            # 何もせずdelay秒待つ
            time.sleep(delay)

        # 指定時間終了後
        # 「現在時間(time.time()) - 開始時間」
        # が END 秒以上経過していたら
        if int(time.time() - start) >= END:
            # 録画の停止
            camera.stop_recording()
            time.sleep(1)
            # センサの検知が検知回数の半分未満だったら
            # （人がいないと判断したら）
            if count < (END * (1 / delay) / 2):
                # 録画したファイルを削除する
                os.remove(video_file)
            # センサ検知のカウント回数の初期化
            count = ____
            start = time.time()


if __name__ == '__main__':

    try:  # 通常時
        main()
    except KeyboardInterrupt:  # キーボードが押されたとき
        pass
    finally:  # 終了時(ctrl+cなど)
        pass
