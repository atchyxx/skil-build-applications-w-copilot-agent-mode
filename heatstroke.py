import math


def heat_index(temperature_celsius: float, humidity: float) -> float:
    """Calculate the heat index in Celsius.

    The formula converts the temperature to Fahrenheit, applies the US National
    Weather Service formula for heat index, then converts the result back to
    Celsius.

    Args:
        temperature_celsius: Ambient air temperature in degrees Celsius.
        humidity: Relative humidity in percent (0-100).

    Returns:
        The heat index in degrees Celsius.
    """
    temperature_f = temperature_celsius * 9 / 5 + 32
    t = temperature_f
    r = humidity

    hi_f = (
        -42.379
        + 2.04901523 * t
        + 10.14333127 * r
        - 0.22475541 * t * r
        - 6.83783e-3 * t ** 2
        - 5.481717e-2 * r ** 2
        + 1.22874e-3 * t ** 2 * r
        + 8.5282e-4 * t * r ** 2
        - 1.99e-6 * t ** 2 * r ** 2
    )

    hi_c = (hi_f - 32) * 5 / 9
    return hi_c


def classify_heat_index(hi_celsius: float) -> str:
    """Classify the heat index value."""
    if hi_celsius < 27:
        return "Caution"
    if hi_celsius < 39:
        return "Extreme Caution"
    if hi_celsius < 51:
        return "Danger"
    return "Extreme Danger"


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Heat index calculator")
    parser.add_argument("temperature", type=float, help="Temperature in Celsius")
    parser.add_argument("humidity", type=float, help="Relative humidity in percent")
    args = parser.parse_args()

    hi = heat_index(args.temperature, args.humidity)
    category = classify_heat_index(hi)
    print(f"Heat Index: {hi:.1f} °C - {category}")


if __name__ == "__main__":
    main()
