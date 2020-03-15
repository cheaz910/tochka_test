from rest_framework import status
from rest_framework.response import Response

from .models import Account


def check_possibillity_operation(data, account):
    if not isinstance(data['addition']['value'], int):
        return Response(get_json_error(status.HTTP_400_BAD_REQUEST, "bad value"))
    if account.status != 'открыт':
        return Response(get_json_error(status.HTTP_400_BAD_REQUEST, "account status isn't opened"))


def handle_operation(data, operate):
    try:
        account = Account.objects.get(uuid=data['addition']['uuid'])
        if not isinstance(data['addition']['value'], int):
            return Response(get_json_error(status.HTTP_400_BAD_REQUEST, "bad value"))
        if account.status != 'открыт':
            return Response(get_json_error(status.HTTP_400_BAD_REQUEST, "account status isn't opened"))
        value = int(data['addition']['value'])
        result_info = operate(account, value)
        return Response({
            "status": status.HTTP_200_OK,
            "result": True,
            "addition": result_info,
            "description": {}
        })
    except KeyError:
        return Response(get_json_error(status.HTTP_400_BAD_REQUEST, "bad json format"))
    except ValueError as e:
        return Response(get_json_error(status.HTTP_400_BAD_REQUEST, str(e)))
    except Exception as e:
        return Response(get_json_error(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e)))


def get_json_error(http_status, message):
    return {
        "status": http_status,
        "result": False,
        "addition": {},
        "description": {
            "error": message
        }
    }
