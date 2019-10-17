def func(*, keyword_1, keyword_2):
    pass


def func(positional_1, positional_2, /, arg_1, arg_2, *, keyword_1, keyword_2):
    pass


# Works just fine!
func(1, 2, arg_1=3, arg_2=4, keyword_1=5, keyword_2=6)

# Raises an exception!!
func(positional_1=1, positional_2=2, arg_1=3, arg_2=4, keyword_1=5, keyword_2=6)
