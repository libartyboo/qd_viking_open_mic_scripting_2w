from faker import Faker
from config_sql import sql_get_all
from db_crud_sqlite import db_get, db_create_tb, db_store
from config import projects_list


def new_user(project):
    db_create_tb(projects_list)
    faker = Faker()
    user_data = [faker.first_name(), faker.last_name(), faker.safe_email(), faker.password()]
    print("-" * 100)
    print(f"NEW USER: {user_data}")
    print("-" * 100)
    db_store(project, *user_data)
    return


def select_data_from_table(project):
    return db_get(sql_get_all(project))


def db_actions(project):
    answer_1 = int(input(f"[create new user] - 1, [get all] - 2: \n"))
    if answer_1 == 1:
        new_user(project)
    elif answer_1 == 2:
        print("-" * 100)
        for user in select_data_from_table(project):
            print(user)
        print("-" * 100)


def projects_menu():
    i = 0
    projects = []
    for project in projects_list:
        i += 1
        print(project)
        projects.append(f"[{project}] - {i}")
    return projects


def menu():
    projects = projects_menu()
    while True:
        answer = int(input(f"{projects}, [выход] - 0: \n"))
        if answer != 0:
            db_actions(projects_list[answer-1])
        elif answer == 0:
            print("exit")
            break


if __name__ == '__main__':
    menu()
