import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

USER_NAME="nouffan"
TOKEN=os.getenv("PIXELA_TOKEN")


parm={
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
#response=requests.post("https://pixe.la/v1/users",json=parm)

#print(response.text)

graph_endpoint=f"https://pixe.la/v1/users/{USER_NAME}/graphs"

graph_config={
    "id":"graph1",
    "name":"Music_graph",
    "unit":"min",
    "type":"float",
    "color": "sora",
}
header={
    "X-USER-TOKEN":TOKEN
}

today=datetime.now()

today_formated=today.strftime("%Y%m%d")


#response=requests.post(url=graph_endpoint,json=graph_config,headers=header)

#print(response.text)


PIXEL_ENDPOINT=f"{graph_endpoint}/graph1"

pixel_config={
    "date":today_formated,
    "quantity" : input("HOW many hours you listened music today? "),


}


response2=requests.post(url=PIXEL_ENDPOINT,headers=header,json=pixel_config)

print(response2.text)