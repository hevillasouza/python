# nome de classe sempre começa com letra maiusculo
class Pessoa():
    def __init__(self, cpf, nome, idade, cidade, genero ):
        self.cpf = cpf
        self.nome = nome #usa self porque é uma variável do objetivo
        self.idade = idade
        self.cidade = cidade
        self.genero = genero
    def __str__(self):
        return f"A pessoa {self.nome} com CPF {self.cpf} tem {self.idade}, mora na cidade {self.cidade} e é do gênero {self.genero}!"     
    def comer(self, alimento):
        # não usa self em alimento porque é um parâmetro do método
        return f"A pessoa {self.nome} está comendo {alimento}!"
    def estudo(self, conteudo):
        return f"A pessoa {self.nome} está estudando {conteudo}!"
    def dormir(self):
        # não usa self porque é um parâmetro do método
        return "zzzzzzzzzzz!"
    def jogar(self, jogo):
        # não usa self porque é um parâmetro do método
        return f"A pessoa {self.nome} está jogando {jogo}!"

pessoa = Pessoa(123,"Mário",24,"Caruaru","Masculino")
print(pessoa)
print(pessoa.comer("bolacha"))
print(pessoa.estudo("Orientação à Objeto"))
print(pessoa.dormir())
print(pessoa.jogar("LOL"))

