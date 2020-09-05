class Pessoa:
    def __init__(self, nome=None, idade = None):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('luciano','32')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'renzo'
    print(p.nome)
    print(p.idade)