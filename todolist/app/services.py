from app import models


# ******Service list_task methods****** #


def get_list_task_by_pk_and_user_id(list_task, user):
    try:
        list_of_task = models.ListTaskModel.objects.get(pk=list_task, user=user)

    except Exception:
        return None

    return list_of_task


def filter_lists_of_tasks_by_user_id(user):
    try:
        lists_of_tasks = models.ListTaskModel.objects.filter(user=user).order_by("-id")

    except Exception:
        return None

    return lists_of_tasks


def create_list_of_task(user, title, start_date, end_date, description, c_status):
    try:
        list_of_task = models.ListTaskModel.objects.create(
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
    list_of_task, _title, _start_date, _end_date, _description, _status
):

    try:
        list_of_task.title = _title
        list_of_task.start_date = _start_date
        list_of_task.end_date = _end_date
        list_of_task.description = _description
        list_of_task.status = _status

        list_of_task.save()

    except Exception:
        return None

    return list_of_task


def chek_equal_list_task(user, title, description):
    try:
        tasks = models.ListTaskModel.objects.filter(user=user)

        for task in tasks:
            if task.title == title or task.description == description:
                return None

    except Exception:
        return None

    return True


# ******Service task methods****** #


def get_task_by_pk_and_user_id(task_pk, user):
    try:
        task = models.TaskModel.objects.get(pk=task_pk, user=user)

    except Exception:
        return None

    return task


def filter_tasks_by_user_id(user):
    try:
        tasks = models.TaskModel.objects.filter(user=user).order_by("-id")

    except Exception:
        return None

    return tasks


def create_task(
    _user,
    _list_identification,
    _title,
    _start_date,
    _end_date,
    _description,
    _status,
):
    try:
        task = models.TaskModel.objects.create(
            user=_user,
            list_task=_list_identification,
            title=_title,
            start_date=_start_date,
            end_date=_end_date,
            description=_description,
            status=_status,
        )
    except Exception:
        return None

    return task


def check_list_of_task(_list_identificatin, _user):
    try:
        list_of_task = models.ListTaskModel.objects.get(
            id=_list_identificatin, user=_user
        )

    except Exception:
        return None

    return list_of_task


def chek_equal_task(_list_identification, _title, _description):
    try:
        tasks = models.TaskModel.objects.filter(list_task=_list_identification)

        for task in tasks:
            if task.title == _title or task.description == _description:
                return None

    except Exception:
        return None

    return True


def update_task(task, _title, _start_date, _end_date, _description, _status):
    try:
        task.title = _title
        task.start_date = _start_date
        task.end_date = _end_date
        task.description = _description
        task.status = _status

        task.save()

    except Exception:
        return None

    return task
