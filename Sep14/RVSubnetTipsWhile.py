import time

# Ryan's Subnetting Countdown: 10 Tips, 10 Steps, While Loop Edition

subnetting_tips = [
    "CIDR /24 means 24 bits for the network - classic Class C.",
    "Subnet mask 255.255.255.0 = 8 bits per octet for the first three octets.",
    "To calculate subnets: 2^borrowed bits. Borrow 3 bits? You get 8 subnets.",
    "Hosts per subnet = 2^host bits - 2. Always subtract for network & broadcast.",
    "/30 gives 4 IPs: 2 usable. Ideal for router-to-router links.",
    "/28 = 16 IPs, 14 usable. Great for small device clusters.",
    "Subnet mask alignment matters - don't eyeball, calculate.",
    "Avoid overlapping subnets. They confuse routing tables.",
    "Private IP ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.",
    "Practice binary math - it's your subnetting superpower."
]

i = 0
while i < len(subnetting_tips):
    print(f"{i + 1}. {subnetting_tips[i]}")
    time.sleep(3)  # Delay between tips
    i += 1