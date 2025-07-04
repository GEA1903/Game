from personagem import Personagem  # Importa a classe Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, maldade, dano, velocidade, alcance):
        super().__init__(nome, idade, vida, velocidade)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade
        

    def ataque(self, personagem):
        """ 
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida()
        

    def super_ataque(self, hits, dano, alcance, velocidade):
        """
        O dano causado e a distância do ataque e a carga e a velocidade do vilão aumentam com o super
        """
        
        if self.hits == 15:
            self.dano += 20
            self.alcance += 35 
            self.velocidade += 4.5
            print(f"{self.nome} ativou o modo SUPER! Dano: {self.dano}, Alcance: {self.alcance}, Carga: {self.carga_ataque}")
            try: 
                if self.hits == 20:
                    self.dano
                    self.alcance
                    self.carga_ataque
                    self.velocidade
                elif 15 < self.hits < 20:
                    self.dano += 30 
                    self.alcance += 40 
                    self.carga_ataque += 4
                    self.velocidade += 5
                else:
                    None
            except ValueError:
                None

    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}'
