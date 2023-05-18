def question1():
    results = {
        "Mark": [65, 48, 77, 56],
        "Zyra": [61, 59, 88, 74, 68],
        "Sue": [75, 64, 68, 53],
        "Ethel": [44, 53, 62, 49],
        "Keith": [43, 32, 28],
    }
    for name, value in results.items():
        passed = 0
        failed = 0
        syntax = "none"
        for mark in value:
            if mark >= 50:
                passed += 1
            else:
                failed += 1
        print(
            f"{name}: passed {syntax if passed == 0 else passed}, failed {syntax if failed == 0 else failed}, average {round(sum(value)/len(value),1)}"
        )


question1()
