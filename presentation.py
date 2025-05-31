import streamlit as st
from streamlit_reveal_slides import reveal_slides

def presentation_page():
    st.title("Презентация проекта")
    slides = [
        {"title": "Введение", "content": "Проект предиктивного обслуживания оборудования."},
        {"title": "Датасет", "content": "Используется датасет AI4I 2020 с 10 000 записей."},
        {"title": "Модели", "content": "Logistic Regression, Random Forest, XGBoost, SVM."},
        {"title": "Результаты", "content": "Оценка по точности, ROC-AUC и др."}
    ]
    reveal_slides(slides)