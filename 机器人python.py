robots = [
    {
        "name": "Humanoid-01",
        "battery": 78,
        "temperature": 45,
        "speed": 0.3
    },
    {
        "name": "Humanoid-02",
        "battery": 15,
        "temperature": 48,
        "speed": 0.2
    },
    {
        "name": "Humanoid-03",
        "battery": 10,
        "temperature": 72,
        "speed": 0.4
    }
]

robots.append({
    "name": "Humanoid-04",
    "battery": 90,
    "temperature": 40,
    "speed": 0.6
})

for i in robots:
    print(i["name"], ":", i["battery"], i["temperature"], i["speed"])  # 输出每个机器人的信息


def check_robot(robot):
    status = "正常"
    battery_warning = False
    temperature_warning = False

    if robot["battery"] < 20:
        status = "异常"
        battery_warning = True

    if robot["temperature"] > 70:
        status = "异常"
        temperature_warning = True

    return status, battery_warning, temperature_warning


def check_all_robots(robots):
    for i in robots:
        status, battery_warning, temperature_warning = check_robot(i)

        print(i["name"], "机器人状态:", status)

        if battery_warning:
            print(i["name"], "电量过低，请充电！")

        if temperature_warning:
            print(i["name"], "温度过高，请检查！")

def check_speed(robots):
    for i in robots:
        if i["speed"] < 0.5:
            print(i["name"], "速度过慢，请检查！")
        else:
            print(i["name"], "速度正常。")

def find_low__battery_robots(robots):
    low_battery_robots = []
    for i in robots:
        if i["battery"] < 20:
            low_battery_robots.append(i["name"])
    return low_battery_robots

low_battery_robots = find_low__battery_robots(robots)
print("电量过低的机器人:", low_battery_robots)