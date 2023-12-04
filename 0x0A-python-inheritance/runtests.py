def run_tests():
    with open("./tests/1-my_list.txt", "r") as file:
        test_cases = file.read().split("# Test Case")

        for i, test_case in enumerate(test_cases[1:], 1):
            print(f"Running Test Case {i}:")
            code = compile(test_case, "<string>", "exec")
            exec(code)
            print("=" * 40)


if __name__ == "__main__":
    run_tests()
