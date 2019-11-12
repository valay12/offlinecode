from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.j2")

interface_dict = {
	"name": "GigabitEthernet0/1",
	"description": "Server Port",
	"vlan": 10,
	"uplink": False
}

interface_dict1 = {
	"name": "GigabitEthernet0/0",
	"description": "Uplink port",
	"vlan": 1,
	"uplink": True
}

print(template.render(interface=interface_dict))
print(template.render(interface=interface_dict1))
