# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal


# Numeric type (no floats!)
Numeric = Decimal | int | str
