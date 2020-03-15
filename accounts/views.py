from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Account
from .utils import handle_operation, get_json_error


@api_view(['GET'])
def api_ping(request):
    return Response({
        "status": status.HTTP_200_OK,
        "result": True,
        "addition": {},
        "description": {}
    })


@api_view(['POST'])
def api_add(request):
    def add_operation(account, value):
        account.balance += value
        account.save()
        return {"uuid": account.uuid, "balance": account.balance}
    return handle_operation(request.data, add_operation)


@api_view(['POST'])
def api_substract(request):
    def substract_operation(account, value):
        if account.balance - account.hold - value < 0:
            raise ValueError("operation is impossible")
        account.balance -= value
        account.hold += value
        account.save()
        return {
                "uuid": account.uuid,
                "balance": account.balance,
                "hold": account.hold
        }
    return handle_operation(request.data, substract_operation)


@api_view(['POST'])
def api_status(request):
    try:
        account = Account.objects.get(uuid=request.data['addition']['uuid'])
        return Response({
            "status": status.HTTP_200_OK,
            "result": True,
            "addition": {
                "uuid": account.uuid,
                "balance": account.balance,
                "status": account.status
            },
            "description": {}
        })
    except KeyError:
        return Response(get_json_error(status.HTTP_400_BAD_REQUEST, "bad json format"))
    except Exception as e:
        return Response(get_json_error(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e)))
