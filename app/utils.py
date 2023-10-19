def start_program():
    """프로그램 실행 시, 호출해야 한다고 가정"""

    msg = (
        "\n"  #
        "*********************\n"  #
        "*  program started  *\n"  #
        "*********************\n"  #
    )

    print(msg)


def stop_program():
    """프로그램 종료 시, 호출해야 한다고 가정"""

    msg = (
        "\n"  #
        "*********************\n"  #
        "*  program stopped  *\n"  #
        "*********************\n"  #
    )

    print(msg)


def mul(a, b):
    return a * b
