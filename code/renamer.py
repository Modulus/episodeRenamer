import code.regexp_util as rx
import re


def rename(name, regexp, split):
    if name and regexp and split:
        eps_nr = rx.extract(name, regexp)

        parts = eps_nr.split(split, 1)

        if len(parts) >= 2:
            parts[0] = "S"+parts[0]
            parts[1] = "E"+parts[1]
        return re.sub(regexp, "".join(str(x) for x in parts), name)
    return None

