# -*- coding: utf-8 -*-
# モジュールのインポート
import RPi.GPIO as GPIO
import time
import wiringpi as pi
import picamera

delay = 0.2     # 休止時間を0.2秒に設定
END = 1         # 終了時間を10秒に設定
sensor_pin = 18 # 人感センサをGPIO18に接続
buzzerpin = 4   # ブザーのPINをGPIO4に接続

# カメラを使用する設定
camera = picamera.PiCamera()
# 画像サイズを400 x 400に
camera.resolution = (400, 400)

# 初期設定
def sensor_init():
    GPIO.setmode(GPIO.BCM)
    pi.wiringPiSetupGpio()
    pi.pinMode(sensor_pin, pi.INPUT)
    GPIO.setup(buzzerpin, GPIO.OUT, initial=GPIO.HIGH)  # ブザーの初期設定

# 動作設定
def main():
    sensor_init()
    # 動画の保存ファイル名の初期化
    video_count = 0
    # センサ検知のカウント回数の初期化
    count = 0
    # 開始時間の代入
    start = time.time()
    print('start counting')
    # 無限ループ
    while True:
        # センサが感知したとき
        if( pi.digitalRead( sensor_pin ) == pi.HIGH ):
            # count を +1 する
            count = count + 1
            time.sleep(delay)
            print(count)
        # センサが感知しなかったとき
        elif( pi.digitalRead( sensor_pin ) == pi.LOW ):
            # 何もせずdelay秒待つ
            time.sleep(delay)

        # 指定時間終了後
        # 「現在時間(time.time()) - 開始時間」が END 秒以上経過していたら
        if int(time.time() - start) >= END:
            # センサの検知が検知回数の半分未満だったら
            if count > int(END * (1 / delay) / 2):
                # ブザー
                GPIO.output(buzzerpin, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(buzzerpin, GPIO.HIGH)
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
                # 動画の保存ファイルの変更
                video_count = video_count + 1
            # 人感センサの検知回数の初期化
            count = 0
            # 開始時間をリセット
            start = time.time()
            print('start counting')

# KeyboardInterrupt時の設定
def destroy():
    # ブザーをOFFにする
    GPIO.output(buzzerpin, GPIO.HIGH)
    # GPIOのリソースを開放する
    GPIO.cleanup()

if __name__ == '__main__':
    try:  # 通常時
        main()
    except KeyboardInterrupt:  # キーボードが押されたとき
        destroy()
    finally: # 終了時(ctrl+cなど)
        pass
