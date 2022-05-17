import streamlit as st
import requests


st.title("Purchase Intention Application")
Administrative = st.number_input("Administrative")
Administrative_Duration = st.number_input("Duration")
ProductRelated = st.number_input("Product Related")
ProductRelated_Duration = st.number_input("ProductRelated_Duration")
BounceRates = st.number_input("BounceRates")
ExitRates = st.number_input("ExitRates")
PageValues = st.number_input("PageValues")
TrafficType = st.number_input("TrafficType")
VisitorType_Other = st.number_input("VisitorType_Other")
VisitorType_Returning_Visitor = st.number_input("VisitorType_Returning_Visitor")
Weekend_True = st.number_input("Weekend_True")
Month_sin = st.number_input("Month_sin")
Month_cos = st.number_input("Month_cos")
SpecialDay_1 = st.number_input("SpecialDay_1")
OperatingSystems_2 = st.number_input("OperatingSystems_2")
OperatingSystems_3 = st.number_input("OperatingSystems_3")
OperatingSystems_other = st.number_input("OperatingSystems_other")
Browser_2 = st.number_input("Browser_2")
Browser_other = st.number_input("Browser_other")
Region_2 = st.selectbox("Region_2", ["0", "1"])
Region_3 = st.number_input("Region_3")
Region_4 = st.number_input("Region_4")
Region_5 = st.number_input("Region_5")
Region_6 = st.number_input("Region_6")
Region_7 = st.number_input("Region_7")
Region_8 = st.number_input("Region_8")
Region_9 = st.number_input("Region_9")
# inference
data = {'Administrative':Administrative,
        'Administrative_Duration':Administrative_Duration,
        'ProductRelated':ProductRelated,
        'ProductRelated_Duration':ProductRelated_Duration,
        'BounceRates':BounceRates,
        'ExitRates':ExitRates,
        'PageValues':PageValues,
        'TrafficType':TrafficType,
        'VisitorType_Other':VisitorType_Other,
        'VisitorType_Returning_Visitor':VisitorType_Returning_Visitor,
        'Weekend_True':Weekend_True,
        'Month_sin':Month_sin,
        'Month_cos':Month_cos,
        'SpecialDay_1':SpecialDay_1,
        'OperatingSystems_2':OperatingSystems_2,
        'OperatingSystems_3':OperatingSystems_3,
        'OperatingSystems_other':OperatingSystems_other,
        'Browser_2':Browser_2,
        'Browser_other':Browser_other,
        'Region_2':Region_2,
        'Region_3':Region_3,
        'Region_4':Region_4,
        'Region_5':Region_5,
        'Region_6':Region_6,
        'Region_7':Region_7,
        'Region_8':Region_8,
        'Region_9':Region_9}

URL = "https://deploy-milestone2-backend.herokuapp.com/predict"

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if res['code'] == 200:
    st.title(res['result']['description'])
else:
    st.write("Mohon maaf terjadi kesalahan")
    st.write(f"keterangan : {res['result']['error_msg']}")

 