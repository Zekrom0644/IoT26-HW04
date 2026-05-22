from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

# GPIO 설정
LED1 = 23
LED2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# GPIO 초기화
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)

led1_state = False
led2_state = False


@app.route("/")
def index():
    global led1_state, led2_state

    # 실제 GPIO 상태 읽기
    led1_state = GPIO.input(LED1)
    led2_state = GPIO.input(LED2)

    return render_template(
        "index.html",
        led1=led1_state,
        led2=led2_state
    )


@app.route("/led1/<action>")
def led1_control(action):

    if action == "on":
        GPIO.output(LED1, GPIO.HIGH)

    elif action == "off":
        GPIO.output(LED1, GPIO.LOW)

    return index()


@app.route("/led2/<action>")
def led2_control(action):

    if action == "on":
        GPIO.output(LED2, GPIO.HIGH)

    elif action == "off":
        GPIO.output(LED2, GPIO.LOW)

    return index()


if __name__ == "__main__":
    try:
        app.run(
            host="0.0.0.0",
            port=8080,
            debug=False
        )

    finally:
        GPIO.cleanup()
