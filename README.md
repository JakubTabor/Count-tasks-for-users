# Count-tasks-for-users
This function take list of users, and then choose 2 of the users who completed the most tasks to give them rewards.
I use defaultdict in this code for avoid exception with empty dict
I need to change list of users to conj of params and make function of it(def change_list_into_conj_of_param)
for more flexibility i add arg(key="id") so I can choose users by their ID, not only users with usersWithTopCompletedTasks can be choosed
