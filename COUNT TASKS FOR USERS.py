from collections import defaultdict
import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")


def count_tasks_frequency(tasks):
    completedTaskFrequencyByUser = defaultdict(int)
    for entry in tasks:
        if (entry["completed"] == True):
            completedTaskFrequencyByUser[entry["userId"]] += 1

    return completedTaskFrequencyByUser


def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]


def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTasks in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTasks == maxAmountOfCompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)

    return usersIdWithMaxCompletedAmountOfTasks


try:
    tasks = r.json()

except json.decoder.JSONDecodeError:
    print("incorrect format")
else:
    completedTaskFrequencyByUser = count_tasks_frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(
        completedTaskFrequencyByUser)


def change_list_into_conj_of_param(my_list, key="id"):
    conj_param = key + "="
    lastIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIteration):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key + "="

    return conj_param


conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks, "id")
r = requests.get("https://jsonplaceholder.typicode.com/users",
                 params=conj_param)

users = r.json()
for user in users:
    print("Congratulations for users named: ", user["name"])
