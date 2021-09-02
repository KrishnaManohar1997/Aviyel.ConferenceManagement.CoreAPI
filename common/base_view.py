from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseView(APIView):
    def success_response(self, message):
        return Response(
            {"result": True, "message": message},
            status=status.HTTP_200_OK,
        )

    def data_response(self, message, data):
        return Response(
            {"result": True, "message": message, "data": data},
            status=status.HTTP_200_OK,
        )

    def resource_created_response(self, resource, resource_id):
        return Response(
            {
                "result": True,
                "message": f"{resource} created successfully",
                "id": resource_id,
            },
            status=status.HTTP_201_CREATED,
        )

    def resource_updated_response(self, resource, resource_id):
        return Response(
            {
                "result": True,
                "message": f"{resource} with {resource_id} updated successfully",
            },
            status=status.HTTP_202_ACCEPTED,
        )

    def bad_request_response(self, message):
        # Handles Error Objects Internally by Converting them To String
        return Response(
            {"result": False, "message": str(message)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def unauthorized_response(self, message="Unauthorized Access"):
        return Response(
            {"result": False, "message": message},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def resource_not_found_response(self, resource, id=None):
        if id:
            message = f"{resource} - {id} doesn't exist "
        else:
            message = f"Requested {resource} doesn't exist "
        return Response(
            {"result": False, "message": message},
            status=status.HTTP_404_NOT_FOUND,
        )

    def paginated_response(self, paginator, message, data):
        return paginator.get_paginated_response(
            {"result": True, "message": message, "data": data}
        )

    def serializer_error_response(self, message, serializer_errors: dict):
        print(serializer_errors)
        serializer_errors = " ".join(
            [
                error_key + ":" + error_detail[0]
                for error_key, error_detail in serializer_errors.items()
            ]
        )
        return self.bad_request_response("{}. {}".format(message, serializer_errors))

    class Meta:
        abstract = True
