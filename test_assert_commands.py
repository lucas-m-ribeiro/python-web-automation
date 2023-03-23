# o assert sempre verifica se o retorno da condição é true
assert True

#assert numbers 
num_esperado = 5
num_obtido = 2
assert num_esperado > num_obtido, f"Esperado {num_esperado} Atual {num_obtido}" 

#assert text
text_esperado = "selenium webdriver"
text_obtido = "selenium webdriver"
assert text_esperado == text_obtido, f"Esperado {text_esperado} Atual {text_obtido}" 

#assert text in string
text_esperado = "selenium"
text_obtido = "selenium Webdriver"
assert text_esperado in text_obtido, f"Esperado {text_esperado} dentro da string Atual {text_obtido}" 
