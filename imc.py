import streamlit as st


st.title('CALCULADORA IMC')

massa = st.number_input('Digite a sua massa')

status = st.radio('Selecione a opção de unidade de mediada de altura',('cm','m'))


if (status == 'cm'):
	altura = st.number_input('Digite a altura em centímetros')
	try:
		imc = massa/((altura/100) ** 2)
	except: 
		st.error('Digite a altura em centímetros')
elif (status == 'm'):
	altura = st.number_input('Digite a altura em metros')			
	try:
		imc = massa/(altura ** 2)
	except: 
		st.error('Insira algum valor para a altura')
if altura and massa:
	if (st.button('Calcular Imc')):
		st.text('Seu índice de Imc é: {}'.format(imc))
	if(imc < 16):
		st.error('Extremamente abaixo do peso.')
	elif(imc >= 16 and imc < 18.5):
		st.warning('Abaixo do peso')
	elif(imc >= 18.5 and imc < 25 ):
		st.success('Saudável')
	elif(imc >= 25 and imc < 30):
		st.warning('Excesso de peso')
	elif(imc >= 30):
		st.error('Muito acima do peso')			





