"""
HOW TO RUN THIS
 - python manage.py runscript add_users_script -v3
"""

g_user = {
    "username": "user%s",
    "email": "user%s@company.com",
    "first_name": "User",
    "last_name": "%s",
    "password": "testpass123",
}


def _number_to_word(num):
    num_dict = {
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    return num_dict[num]


def run():
    from django.contrib.auth.models import User

    for ind in range(2, 10):
        u = User(
            username=g_user["username"].replace("%s", str(ind)),
            first_name=g_user["first_name"],
            last_name=g_user["last_name"].replace("%s", _number_to_word(ind).title()),
            email=g_user["email"].replace("%s", str(ind)),
        )
        u.set_password(g_user["password"])
        u.save()
