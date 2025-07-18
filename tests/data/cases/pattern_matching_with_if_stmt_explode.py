# flags: --minimum-version=3.10

# case black_test_match_case_conditional_001
def f(x):
    match x:
        # Should change
        case [
            y
        ] if y == 123:
            pass

        # Should change
        case [
            y
        ] if True:
            pass

        # Should not change
        case [
            y,
        ] if True:
            pass

        # Should not change
        case [
            y,
        ] if y == 123:
            pass

        # Should change
        case [
            y,
        ] if (
            y == 123
        ):
            pass

        # Should not change
        case [
            y,
        ] if c(
            very_complex=True,
            perhaps_even_loooooooooooooooooooooooooooooooooooooong=-1,
        ):
            pass

        # Should change
        case [
            y,
        ] if perhaps_even_looooooooooooooooooooooooooooooooooooooooooooooooong == True:
            pass

# output

# case black_test_match_case_conditional_001
def f(x):
    match x:
        # Should change
        case [y] if y == 123:
            pass

        # Should change
        case [y] if True:
            pass

        # Should not change
        case [
            y,
        ] if True:
            pass

        # Should not change
        case [
            y,
        ] if y == 123:
            pass

        # Should change
        case [
            y,
        ] if y == 123:
            pass

        # Should not change
        case [
            y,
        ] if c(
            very_complex=True,
            perhaps_even_loooooooooooooooooooooooooooooooooooooong=-1,
        ):
            pass

        # Should change
        case [
            y,
        ] if (
            perhaps_even_looooooooooooooooooooooooooooooooooooooooooooooooong == True
        ):
            pass
