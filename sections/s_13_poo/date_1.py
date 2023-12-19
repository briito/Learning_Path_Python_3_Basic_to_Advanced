class Data:
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


data_1 = Data()
data_1.dia = 2
data_1.mes = 7
data_1.ano = 2023
print(data_1)

data_2 = Data()
data_2.dia = 30
data_2.mes = 1
data_2.ano = 1983
print(data_2)
