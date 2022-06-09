from yaml import Loader, Dumper, load, dump

# Print content of a file
with open("./yaml.yaml", "r") as yamlfile:
    content = load(yamlfile, Loader=Loader)
    print(content['testing']) # Print the content of the file | Loading works the same as json

# Dump things
with open("./yaml.yaml", 'r') as yamlfile:
    yfcontent = load(yamlfile, Loader=Loader)
with open("./yaml.yaml", "w") as yamlfilew:
    yfcontent['test'] = "test"
    dump(yfcontent, yamlfilew, Dumper=Dumper)