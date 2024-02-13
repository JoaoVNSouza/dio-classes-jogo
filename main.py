class heroi():
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        
    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreio":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        else:
            ataque = "shuriken"

        print(f"o {self.tipo} atacou usando {ataque}")


heroi1 = heroi("Gandalf", 100, "mago")
heroi1.atacar()