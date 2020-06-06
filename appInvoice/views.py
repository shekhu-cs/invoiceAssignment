from django.http import Http404
from rest_framework import status, generics
from rest_framework.views import APIView
import tabula
from .models import InvoiceModel
from .serializers import InvoiceSerializer
from rest_framework.response import Response


class EndCustomer(APIView):
    """
    to view all structured data from db use get method which will also show status of document
    """
    def get(self, request):
        model_data = InvoiceModel.objects.all()
        serializer_data = InvoiceSerializer(model_data, many=True)
        return Response(serializer_data.data)
    """
    to post a pdf file and process that pdf file from unstructured data to structured data and store in db
    """

    def post(self, request, *args, **kwargs):
        try:
            rd = request.data
            print(rd)
            df = tabula.read_pdf(rd['file'], output_format="json")
            # print(df)
            lst = []
            for d in df:
                for data in d['data']:
                    for dd in data:
                        lst.append(dd['text'])
            # print(lst)
            pdf_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
            print(pdf_dct)
            try:
                InvoiceModel.objects.create(invoiceNumber=pdf_dct['Invoice Number'], deuDate=pdf_dct['Due Date'],
                                        orderNumber=pdf_dct['Order Number'], invoiceDate=pdf_dct['Invoice Date'],
                                        total=pdf_dct['Total'], status='document is processed')
            except Exception as ee:
                return Response({'status': 'data insertion failed', 'error_msg': str(ee)})
            return Response({'status': 'document process success'})
        except Exception as e:
            return Response({'status': 'document process failed', 'error_msg': str(e)})


class InternalUserUpdate(APIView):
    """
    to update particular record by passing id(pk)  in endpoint
    """
    def get_object(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            return InvoiceModel.objects.get(pk=pk)
        except InvoiceModel.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        model_obj = self.get_object(pk)
        serializer_data = InvoiceSerializer(model_obj)
        return Response(serializer_data.data)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        model_obj = self.get_object(pk)
        serializer_data = InvoiceSerializer(model_obj, data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class InternalUser(APIView):
    """
    to get all record and post/add new record
    """
    def get(self, request, format=None):
        model_data = InvoiceModel.objects.all()
        serializer_data = InvoiceSerializer(model_data, many=True)
        return Response(serializer_data.data)

    def post(self, request, format=None):
        serializer_data = InvoiceSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


# {
# "invoiceNumber" :"123",
#     "deuDate": "123",
#     "orderNumber": "123",:
#     "invoiceDate":"12",
#     "total": "343",
#     "status": "do"
# }