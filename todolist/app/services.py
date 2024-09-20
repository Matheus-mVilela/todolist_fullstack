from app import models

# ******Service list_task methods****** #


def get_list_task_by_pk_and_user_id(list_task, user):
    try:
        list_of_task = models.ListOfTask.objects.get(pk=list_task, user=user)

    except Exception:
        return None

    return list_of_task


def filter_lists_of_tasks_by_user_id(user):
    try:
        lists_of_tasks = models.ListOfTask.objects.filter(user=user).order_by("id")

    except Exception:
        return None

    return lists_of_tasks


def create_list_of_task(user, title, start_date, end_date, description, c_status):
    try:
        list_of_task = models.ListOfTask.objects.create(
            user=user,
            title=title,
            start_date=start_date,
            end_date=end_date,
            description=description,
            status=c_status,
        )
    except Exception:
        return None

    return list_of_task


def update_list_of_task(
    list_of_task, title, start_date, end_date, description, c_status
):

    try:
        list_of_task.title = title
        list_of_task.start_date = start_date
        list_of_task.end_date = end_date
        list_of_task.description = description
        list_of_task.status = c_status

        list_of_task.save()

    except Exception:
        return None

    return list_of_task


def chek_equal_list_task(user, title, description):
    try:
        tasks = models.ListOfTask.objects.filter(user=user)

        for task in tasks:
            if task.title == title or task.description == description:
                return None

    except Exception:
        return None

    return True


# ******Service task methods****** #


def get_task_by_pk_and_user_id(task_pk, user):
    try:
        task = models.Task.objects.get(pk=task_pk, user=user)

    except Exception:
        return None

    return task


def filter_tasks_by_user_id(user):
    try:
        tasks = models.Task.objects.filter(user=user).order_by("-id")

    except Exception:
        return None

    return tasks


def create_task(
    user,
    list_identification,
    title,
    start_date,
    end_date,
    description,
    c_status,
):
    try:
        task = models.Task.objects.create(
            user=user,
            list_task=list_identification,
            title=title,
            start_date=start_date,
            end_date=end_date,
            description=description,
            status=c_status,
        )

    except Exception:
        return None

    return task


def check_list_of_task(list_identificatin, user):
    try:
        list_of_task = models.ListOfTask.objects.get(id=list_identificatin, user=user)

    except Exception:
        return None

    return list_of_task


def chek_equal_task(list_identification, title, description):
    try:
        tasks = models.Task.objects.filter(list_task=list_identification)

        for task in tasks:
            if task.title == title or task.description == description:
                return None

    except Exception:
        return None

    return True


def update_task(task, title, start_date, end_date, description, c_status):
    try:
        task.title = title
        task.start_date = start_date
        task.end_date = end_date
        task.description = description
        task.status = c_status

        task.save()

    except Exception:
        return None

    return task
