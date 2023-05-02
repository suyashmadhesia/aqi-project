import pickle
import random
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .serializer import AQIDataSerializer
from .models import AQI
from sklearn.preprocessing import StandardScaler
import pandas as pd

aqi_model = pickle.load(open('/Users/suyash/aqi-project/aqi/models/model_pkl', 'rb'))
scaler = pickle.load(open('/Users/suyash/aqi-project/aqi/models/scaler_pkl', 'rb'))

class AQIView(APIView):
    
    def get(self, request):
        aqi_data = AQI.objects.all()
        aqi_data = aqi_data.filter(id=len(aqi_data)).first()
        currentValue = { 'PM2.5': [aqi_data.pm25], 'PM10':[aqi_data.pm10], 'NO':[aqi_data.no], 'NO2':[aqi_data.no2], 'NOx':[aqi_data.nox], 'CO': [aqi_data.co]}
        data = pd.DataFrame(currentValue)
        transformed_data = scaler.transform(data)
        pred = aqi_model.predict(transformed_data)
        return Response({'AQI': aqi_data.pm25}, status=HTTP_200_OK)

    def post(self, request):
        data:dict = request.data
        serializer = AQIDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


