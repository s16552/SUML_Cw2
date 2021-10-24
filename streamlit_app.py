import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os


st.success('Witaj - aplikacja załadowała się poprawnie')

st.title('Filmy godne uwagi - przegląd tytułów, które mogą zmienić Twoje życie')
st.info('Aplikacja pozwala na przegląd wybranych filmów, które zwyczajnie lubię. Udostępnia także linki do szerszych opisów wymienionych tytułów (ta część jest w ramach bawienia się streamlit - zdążyłem tylko z jednym filmem) oraz tłumaczy tekst z angielskiego na niemiecki (to już w ramach zadania)')

st.header('Animowane')

st.subheader('Spirited Away')
st.info('Piękna animacja z jeszcze piękniejszą oprawą muzyczną. Opisuje podróż pełną przygód z typowym dla studia Ghibli niejednoznacznym podziałem na bohaterów złych i dobrych')
st.write('Link do szczegółów - https://www.filmweb.pl/film/Spirited+Away%3A+W+krainie+Bog%C3%B3w-2001-33288')
st.image('https://th.bing.com/th/id/R.e96b650f0c9d3a9b5eec2bf12725f447?rik=ZJuww35p3jXWMw&pid=ImgRaw&r=0')

#--------------------------------------------
st.header('Tłumaczenie z angielskiego na niemiecki')

import streamlit as st
from transformers import pipeline

text = st.text_area(label="Wpisz tekst")
if text:
    translator = pipeline("translation_en_to_de")
    st.write(translator(text, max_length=40))
#--------------------------------------------

st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')

st.header('s16552')
