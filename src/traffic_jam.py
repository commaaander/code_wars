from typing import List

import codewars_test as test


def traffic_jam(traffic: List[int], green_light_duration: int):
    total_passing_time = 0
    green_light_phases_count = 1

    for passing_time in traffic[::]:
        total_passing_time += passing_time
        if total_passing_time > green_light_duration:
            green_light_phases_count += 1
            total_passing_time = passing_time

    return green_light_phases_count


@test.describe("traffic_jam")
def tests():
    @test.it("Should return the number of traffic light switches")
    def test_traffic_jam():
        test.assert_equals(traffic_jam([15, 2, 8, 7], 16), 3)
        test.assert_equals(traffic_jam([12, 5, 8, 1], 16), 2)
        test.assert_equals(traffic_jam([5, 5, 2, 4], 5), 4)
