from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer
from rest_framework.exceptions import NotFound
from rest_framework.authentication import TokenAuthentication # 사용자 인증 (추가)
from rest_framework.permissions import IsAuthenticated # 권한 부여 (추가)

class AddressList(APIView):
    authentication_classes = [TokenAuthentication] # 추가
    permission_classes = [IsAuthenticated] # 추가
    def get(self, request):
        address=Address.objects.all()
        selializer=AddressSerializer(address, many=True)
        return Response(selializer.data)
    def post(self, request):
        user = request.user
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            address=serializer.save(user=request.user)
            serializer=AddressSerializer(address)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    


class Address_Detail(APIView):
    def get_object(self, user_id):
        try:
            return Address.objects.filter(user_id=user_id)
        except Address.DoesNotExist:
            raise NotFound
    def get(self, request,user_id):
        address=self.get_object(user_id)
        selializer=AddressSerializer(address,many=True)
        return Response(selializer.data)
class UpdateAddress(APIView):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)  # address_id가 아닌 id 필드 사용
        except Address.DoesNotExist:
            return None

    def get(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DeleteAddress(APIView):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)  # address_id가 아닌 id 필드 사용
        except Address.DoesNotExist:
            return None

    def get(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AddressSerializer(address)
        return Response(serializer.data)
    def delete(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)