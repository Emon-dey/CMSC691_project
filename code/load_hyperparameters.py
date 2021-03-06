import os

def hp_convert_from_string(x):
    try:
        x = int(x)
    except ValueError:
        try:
            x = float(x)
        except ValueError:
            pass
    finally:
        return x


hp = {}

with open('hyperparameters.txt') as f:
    entries = f.readlines()
    for entry in entries:
        key, value = entry.split(":", 1)
        if "," in value:
            value = [x.strip() for x in value.split(",")]
        else:
            value = value.strip()

        if ("dir" in key) and ("name" not in key) and ("comment" not in key):
            if not os.path.isdir(value):
                os.mkdir(value)
        elif value == "True":
            value = True
        elif value == "False":
            value = False
        else:
            value = hp_convert_from_string(value)
        
        if key == "channel_names" and isinstance(value, str):
            value = [value]
        if key == "num_classes" and isinstance(value, str):
            value = int(value)
        
        hp[key] = value
