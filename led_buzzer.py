import time
import RPi.GPIO as GPIO

def control_led_buzzer(LED_GPIO, BUZZER_GPIO, led_state, buzzer_state):
    """
    LEDとブザーを即時に制御する関数。
    """
    GPIO.output(LED_GPIO, led_state)
    GPIO.output(BUZZER_GPIO, buzzer_state)
