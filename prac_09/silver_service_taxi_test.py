from silver_service_taxi import SilverServiceTaxi
def main():
    taxi = SilverServiceTaxi("SilverServiceTaxi", 200, 1.23, 2)
    taxi.drive(18)
    expected_fare = 1.23 * 2 * 18 + 4.50
    actual_fare = taxi.get_fare()
    print(f"Expected fare: ${expected_fare:.2f}")
    print(f"Actual fare: ${actual_fare:.2f}")

    assert abs(actual_fare - expected_fare) < 0.01
    print(taxi)

main()