# script to calculate uptime based on given total hours run, and downtime hours


def calculate_uptime(total_hours, downtime_hours):
    # get uptime by subtracting downtime hours from total hours
    uptime_hours = total_hours - downtime_hours 

    # divide uptime by total hours then multiply by 100 to get percentage value
    uptime_percentage = (uptime_hours / total_hours) * 100

    # round to 2 decimal places
    print(f"The service has an uptime of {round(uptime_percentage, 2)}%")
    return round(uptime_percentage, 2)

calculate_uptime(431, 20)