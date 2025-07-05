from personagem import Personagem  # Importa a classe Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, maldade, minions, habilidade_especial_vilao_cooldown, nome, idade, vida, dano, alcance, velocidade, genero, especie, hits, carga_ataque_inicial,  mana_maxima=0, tipo_magia=None, dash=0, super_ataque=None, defesa=0):
        super().__init__( nome, idade, vida, dano, alcance, velocidade, genero, especie, hits, carga_ataque_inicial,  mana_maxima=0, tipo_magia=None, dash=0, super_ataque=None, defesa=0)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade
        self.minions = 0
        self.habilidade_especial_vilao_cooldown = 0
        

    def ataque(self, personagem):
        """ 
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida()

    def invocar_minions (self, quantidade=1):
        """
        O vilão consegue invocar uma quantidade de lacaios
        """
        self.minions += quantidade
        print(f"{self.nome} invocou {quantidade} lacaio(s)! Total de lacaios: {self.minions}")


    def habilidade_especial_vilao(self):
        """
        O vilão usa uma habilidade especial única (ex: Amaldiçoar, Roubar Vida).
        Pode ter um cooldown.
        """
        if self.habilidade_especial_vilao_cooldown == 0:
            print(f"{self.nome} usa sua Habilidade Especial Maligna!")
            # Lógica específica da habilidade:
            # Ex: self.vida += 20 # Rouba vida
            # Ex: self.dano += 5 # Buff temporário
            self.habilidade_especial_vilao_cooldown = 3 # Define cooldown de 3 turnos/usos
        else:
            print(f"{self.nome} não pode usar a habilidade especial. Cooldown: {self.habilidade_especial_vilao_cooldown}")

    def reduzir_cooldowns(self, quantidade=1):
        """
        Reduz os cooldowns do vilão. Chamado a cada turno do jogo.
        """
        if self.habilidade_especial_vilao_cooldown > 0:
            self.habilidade_especial_vilao_cooldown -= quantidade
            if self.habilidade_especial_vilao_cooldown < 0:
                self.habilidade_especial_vilao_cooldown = 0
            print(f"Cooldown da Habilidade Especial de {self.nome} reduzido. Restam: {self.habilidade_especial_vilao_cooldown}")



    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}, Lacaios: {self.minions}'
