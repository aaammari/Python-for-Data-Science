def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing :", type(object))
    elif isinstance(object, float) and object != object:  # Check for NaN
        print("Cheese : nan", type(object))
    elif object == 0:
        print("Zero :", type(object))
    elif object == "":
        print("Empty :", type(object))
    elif object is False:
        print("Fake :", type(object))
    else:
        print("Type not found")
        return 1
    return 0