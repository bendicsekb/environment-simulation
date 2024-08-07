import random
import time


class Environment:
    def __init__(self, initial_temp, initial_humidity):
        self.temperature = initial_temp
        self.humidity = initial_humidity

    def update(self, heater_output, humidifier_output):
        # Simulate natural changes (smaller changes for 1-second intervals)
        self.temperature += random.uniform(-0.05, 0.05)
        self.humidity += random.uniform(-0.1, 0.1)

        # Apply effects of devices
        self.temperature += heater_output
        self.humidity += humidifier_output

        # Ensure values stay within realistic ranges
        self.temperature = max(0, min(40, self.temperature))
        self.humidity = max(0, min(100, self.humidity))


class Heater:
    def __init__(self, power=0.1):  # Reduced power for 1-second intervals
        self.power = power
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def output(self):
        return self.power if self.is_on else 0


class Humidifier:
    def __init__(self, power=0.2):  # Reduced power for 1-second intervals
        self.power = power
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def output(self):
        return self.power if self.is_on else 0


class Thermostat:
    def __init__(self, target_temp):
        self.target_temp = target_temp

    def should_heat(self, current_temp):
        return current_temp < self.target_temp


class HumidityMeter:
    def __init__(self, target_humidity):
        self.target_humidity = target_humidity

    def should_humidify(self, current_humidity):
        return current_humidity < self.target_humidity


def simulate(initial_temp, initial_humidity, target_temp, target_humidity):
    env = Environment(initial_temp, initial_humidity)
    heater = Heater()
    humidifier = Humidifier()
    thermostat = Thermostat(target_temp)
    humidity_meter = HumidityMeter(target_humidity)

    time_elapsed = 0

    try:
        while True:
            if thermostat.should_heat(env.temperature):
                heater.turn_on()
            else:
                heater.turn_off()

            if humidity_meter.should_humidify(env.humidity):
                humidifier.turn_on()
            else:
                humidifier.turn_off()

            env.update(heater.output(), humidifier.output())

            print(
                f"Time: {time_elapsed}s, Temp: {env.temperature:.2f}°C, Humidity: {env.humidity:.2f}%, "
                f"Heater: {'On' if heater.is_on else 'Off'}, Humidifier: {'On' if humidifier.is_on else 'Off'}"
            )

            time.sleep(1)  # Wait for 1 second
            time_elapsed += 1

    except KeyboardInterrupt:
        print("\nSimulation ended by user.")


if __name__ == "__main__":
    # Run the simulation
    simulate(initial_temp=20, initial_humidity=50, target_temp=22, target_humidity=60)
