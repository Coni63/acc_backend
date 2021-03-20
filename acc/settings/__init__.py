import os

if "STAGE" in os.environ:
    if os.environ["STAGE"] == "PRE":
        from .pre import *
    elif os.environ["STAGE"] == "PROD":
        from .prod import *
    else:
        from .dev import *
else:
    from .dev import *