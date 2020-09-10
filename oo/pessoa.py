class Pessoa:
    olhos = 2       #Atributo default, igual pra todas as classe

    def __init__(self, *filhos , nome=None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list (filhos)
    def cumprimentar(self):
        return f'olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    luciano.olhos = 1               #adiçao do atributo da classe no atributo de instancia
    del luciano.olhos               #apagamos o atributo do objeto apenas, não da classe
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(Renzo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(Renzo.olhos)
    print(id (Pessoa.olhos), id (luciano.olhos), id(Renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())      #metodo estatico faz com que nao necessite o parametro, como mostrado na linha 18
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
