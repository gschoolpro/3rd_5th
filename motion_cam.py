# -*- coding: utf-8 -*-
# モジュールのインポート
import RPi.GPIO as GPIO
import time
import wiringpi as pi
import picamera

delay = ___      # 人感センサ読み取りの間隔を0.2秒に設定
END = ___        # カウント終了までの時間を1秒に設定
sensor_pin = ___ # 人感センサをGPIO18に接続

# カメラモジュールの呼び出し
camera = picamera.PiCamera()
# 撮影の画面サイズを 400 x 400 に設定
camera.resolution = (___, ___)

# 初期設定
def sensor_init():
    GPIO.setmode(GPIO.BCM)
    pi.wiringPiSetupGpio()
    pi.pinMode(sensor_pin, pi.INPUT)

# 動作設定
def main():
    # 初期設定の呼び出し
    sensor_init()
    # 動画の保存ファイル用変数の初期化
    video_count = ___
    # 人感センサ検知のカウント用変数の初期化
    count = ___
    # 開始時間 start を設定
    start = time.time()
    print('start counting')
    # 無限ループ
    while True:
        # センサが感知したとき
        if( pi.digitalRead( sensor_pin ) == pi.HIGH ):
            # count 自身を +1 する
            count = __________
            time.sleep(delay)
            print(count)
        # センサが感知しないとき
        elif( pi.digitalRead( sensor_pin ) == pi.LOW ):
            # delay秒だけ待つ
            time.sleep(delay)

        # カウント終了
        if int(time.time() - start) >= END:
            # センサの検知回数が全体のうち半分より多かったとき
            if count > int(END * (1 / delay) / 2):
                # 動画の保存ファイル名の設定
                video_file = '{:03d}.h264'.format(video_count)
                # 録画開始
                camera.start_preview()
                camera.start_recording(video_file)
                time.sleep(5)
                # 録画終了
                camera.stop_preview()
                camera.stop_recording()
                time.sleep(1)
                # 動画の保存ファイル名の変更
                video_count = video_count + 1
            # 人感センサ検知回数の初期化
            count = ___
            # 開始時間をリセット
            start = time.time()
            print('start counting')

if __name__ == '__main__':
    try:  # 通常時
        main()
    except KeyboardInterrupt:  # キーボードが押されたとき
        pass
    finally:  # 終了時(ctrl+cなど)
        pass
