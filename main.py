import orionsdk

swis = orionsdk.SwisClient("server", "user", "password")

devices = swis.query('SELECT IPAddress, DNS, SysName, Vendor, MachineType, Description, IOSVersion, Status FROM Orion.Nodes')

print(devices)
