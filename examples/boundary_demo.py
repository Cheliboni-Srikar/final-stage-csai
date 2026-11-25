"""Integer-only boundary demonstration for guide section 1.5; Python 3, no packages."""
def faulty(seats):
    return 0 <= seats <= 4

def repaired(seats):
    return 1 <= seats <= 4

if __name__ == "__main__":
    print("seats | expected | faulty | repaired")
    for seats, expected in [(0,False),(1,True),(4,True),(5,False)]:
        actual = repaired(seats)
        print(f"{seats:5} | {str(expected):8} | {str(faulty(seats)):6} | {actual}")
        assert actual == expected
    assert faulty(0) != False
    print("The zero-seat test reveals the bug. All four repaired checks pass.")
