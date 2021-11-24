from app import models
import pendulum


def get_list_task_by_pk_and_user_id(list_task_pk, user_id):
    try:
        list_of_task = models.ListTaskModel.objects.get(
            pk=list_task_pk, user_id=user_id
        )

    except Exception:
        return None

    return list_of_task


def filter_lists_of_tasks_by_user_id(user_id):
    return models.ListTaskModel.objects.filter(user_id=user_id).order_by("-id")


def create_list_of_task(
    _user_id, _title, _start_date, _end_date, _description, _status
):
    try:
        list_of_task = models.ListTaskModel.objects.create(
            user_id=_user_id,
            title=_title,
            start_date=_start_date,
            end_date=_end_date,
            description=_description,
            status=_status,
        )
    except Exception:
        return None

    return list_of_task


def update_list_of_task(
    list_of_task, _title, _start_date, _end_date, _description, _status
):

    list_of_task.title = _title
    list_of_task.start_date = _start_date
    list_of_task.end_date = _end_date
    list_of_task.description = _description
    list_of_task.status = _status

    list_of_task.save()

    return list_of_task
