from a import A
from b import B


def get_plugin(plugin):
    if plugin == "A":
        return A()
    
    if plugin == "B":
        return B()
    
    raise ValueError("Invalid Plugin!")


def test_annotation(plugin):
    if plugin:
        return get_plugin(plugin)
    else:
        raise ValueError("Invalid Plugin!")