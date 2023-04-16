# although we revised the code, it is still not the best solution
# because we still cannot avoid human errors such as typos (type 3 instead of 13)
# so to avoid this, we can use Enum class from Python 3.4
# when defing a enum and at the same time inherits basic types such as int, str, etc.
# then we can use the enum as a basic type - like int, str, etc.
from enum import Enum

class UserType(Enum):
    # vip user
    VIP = 3
    
    # banned user
    BANED = 13

DAILY_POINTS_REWARD = 100
VIP_EXTRA_POINTS = 20

# Finally, we rewrite the code as below
def add_daily_points(user_type, points):
    if user_type == UserType.VIP:
        return points + DAILY_POINTS_REWARD + VIP_EXTRA_POINTS
    elif user_type == UserType.BANED:
        return points
    else:
        return points + DAILY_POINTS_REWARD

