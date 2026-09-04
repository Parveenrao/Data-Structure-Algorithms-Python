class Monotonic:

    def decr_monotonic(self, arr: list[int]) -> bool:

        if len(arr) <= 1:
            return True

        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                return False

        return True


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5]

    monotonic = Monotonic()

    print(monotonic.decr_monotonic(arr))