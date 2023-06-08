from generic_api_stuff.Alerts import Alert

def as_single_dict(*args,**kwargs):
    temp_dict = {}

    for arg in args:
        if type(arg) == Alert:
            temp_dict["alert"] = arg.dict()
        if type(arg) == dict:
            temp_dict.update(arg)
        raise ValueError(f"Argument of {type(arg)} not supported as Positional Argument")

    for key, value in kwargs.items():
        if type(arg) == Alert:
            temp_dict[key] = arg.dict()
        elif type(arg) == dict:
            temp_dict[key] = arg
        else:
            temp_dict[key] = value

    return temp_dict
