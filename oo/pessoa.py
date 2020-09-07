class Pessoa:
    def __init__(self, *filhos , nome=None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list (filhos)
    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    Renzo = Pessoa (nome = 'Renzo')
    luciano = Pessoa(Renzo, nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filhos in luciano.filhos:
        print(filhos.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(Renzo.__dict__)