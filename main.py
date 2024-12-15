from led_buzzer import control_led_buzzer
# from getObd import get_obd_data
import time
# for rpm, speed in get_obd_data():
#    control_led_buzzer(26, 21, 0.03)
#    print(rpm)


if __name__ == "__main__":
    LED_GPIO = 17  # Example GPIO pin for LED
    BUZZER_GPIO = 27  # Example GPIO pin for Buzzer
    LED_FLASH = 3  # 3 seconds for LED on/off duration
    
    while True:
        print(LED_FLASH, LED_GPIO)
        control_led_buzzer(LED_GPIO, BUZZER_GPIO, LED_FLASH)
        time.sleep(3)  # Call the function again every 3 seconds
