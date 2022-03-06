import yaml 


def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        data = yaml.safe_load(file_descriptor)
    return data 

def yaml_dump(filepath, data):
    """Dumps data to a yaml file"""
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor) 

if __name__=="__main__":
    filepath = "test.yml"
    data = yaml_loader(filepath)
    print(type(data))
    print(data)        