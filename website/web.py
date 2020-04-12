import streamlit as st
import pandas as pd
import numpy as np
import math

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; display: inline-block; padding: 1rem; margin-bottom: 2.5rem; background-color: {}"><b>{}</b></div>"""

st.title('Solar Power Predictor')

@st.cache
def load_data(nrows):
    data = pd.read_csv('https://raw.githubusercontent.com/MateoPeri/solar-predictor/master/power.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['date'] = pd.to_datetime(data['date'])
    data = data[['date', 'production (kwh)']]
    data.reset_index(drop=True, inplace=True)
    data.set_index('date', inplace=True)
    return data

@st.cache
def load_history(nyears):
    history = pd.read_csv('https://raw.githubusercontent.com/MateoPeri/solar-predictor/master/hist.csv', nrows=math.ceil(365.25*nyears))
    lowercase = lambda x: str(x).lower()
    history.rename(lowercase, axis='columns', inplace=True)
    history['date'] = pd.to_datetime(history['date'])
    #history = history[['date', 'radiation (w/m2)']]
    history.reset_index(drop=True, inplace=True)
    history.set_index('date', inplace=True)
    return history

data_load_state = st.text('Loading data...')
data = load_data(100000)
data_load_state.text('Loading data... done!')

power = data.mean()[0]

st.markdown('This is a solar panel production model that predicts how much energy a panel would generate in Murcia, our region. The data was collected from weather stations near our town.')

st.markdown('Here you can tweak the number of solar panels to see how much they would produce, as well as some equivalencies.')
n_panels = st.slider('Number of solar panels', min_value=1, max_value=500, value=250, step=1)
st.subheader('Prediction of a solar energy output over the year')
st.line_chart(data*n_panels)

def write_html(l):
    t = '<div>{}{}</div>'.format(l[0], l[1])
    st.markdown(t, unsafe_allow_html=True)

'With solar energy, we could power...'
write_html([HTML_WRAPPER.format('CornflowerBlue', '{:.0f} lightbulbs'.format(power/0.06*n_panels)), HTML_WRAPPER.format('CornflowerBlue', '{:.0f} homes'.format(power/3*n_panels))])
#st.markdown(HTML_WRAPPER.format('CornflowerBlue', '{:.0f} lightbulbs'.format(power/0.06*n_panels)), unsafe_allow_html=True) # 1 lightbulb -> 60 watts
#st.markdown(HTML_WRAPPER.format('CornflowerBlue', '{:.0f} homes'.format(power/3*n_panels)), unsafe_allow_html=True) # 1 home -> 3 kilowatts
'...while saving'
write_html([HTML_WRAPPER.format('CornflowerBlue', '{:.0f} kilograms of oil'.format(power*0.086*n_panels)), HTML_WRAPPER.format('CornflowerBlue', '{:.0f} kilograms of of CO2'.format(power*0.086*2.042*n_panels))])
#st.markdown(HTML_WRAPPER.format('CornflowerBlue', '{:.0f} kilograms of oil'.format(power*0.086*n_panels)), unsafe_allow_html=True) # 1 kwatt -> 0.086 kg oil
#st.markdown(HTML_WRAPPER.format('CornflowerBlue', '{:.0f} kilograms of of CO2'.format(power*0.086*2.042*n_panels)), unsafe_allow_html=True) # 1 kg oil -> 2.042 kg CO2

st.sidebar.markdown('[The code!](https://github.com/MateoPeri/Helyx-Submission)')

st.text('\n\n')
if st.checkbox('Show historical radiation data'):
    st.markdown('''## Train data''')
    st.markdown('''This is the data that was used to train the model and make the predictions.
    It is solar radiation data, collected from nearby weather stations. The data is measured in Watts per meter squared.''')
    years = st.number_input('How many years?', 1, 18, 1)
    hist_load_state = st.text('Loading data...')
    history = load_history(years)
    hist_load_state.text('Loading data... done!')
    st.write(history)

if st.checkbox('Show raw power data'):
    st.subheader('Raw power data')
    st.markdown('These are the values that make up the chart above. They correspond to the amount of power provided by 1 solar panel.')
    st.write(data)

