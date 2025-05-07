# pera: 1,50
# banana: 2,00
# laranja: 3,00
# uva: 4,00
# abacaxi: 5,00
# melancia: 6,00
# maca: 7,00
# kiwi: 8,00
# morango: 9,00
# abacate: 10,00

# funcao para escolher a fruta e informar o preço

fruta = input("Escolha uma fruta: ")
frutas = {
    "pera": 1.50,
    "banana": 2.00,
    "laranja": 3.00,
    "uva": 4.00,
    "abacaxi": 5.00,
    "melancia": 6.00,
    "maca": 7.00,
    "kiwi": 8.00,
    "morango": 9.00,
    "abacate": 10.00
}

if fruta in frutas: 
    print(frutas[fruta])
else: 
    print("Fruta não encontrada, entre em contato com o vendedor.")

