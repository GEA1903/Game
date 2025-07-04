from personagem import Personagem

class Heroi(Personagem):
    def __init__ (self, nome, idade, vida, dano, velocidade, alcance, honra, dash, genero, especie):
        super(). init (nome, idade, vida, velocidade, genero, especie)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if honra not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.honra = honra
        self.dash = dash


    def super_ataque(self, hits, dano, alcance, carga_ataque, velocidade):
        """
        O dano causado e a distância do ataque e a carga e a velocidade do personagem aumentam com o super
        """
        
        if self.hits == 10:
            self.dano += 30 
            self.alcance += 40 
            self.carga_ataque += 4
            self.velocidade += 5
            print(f"{self.nome} ativou o modo SUPER! Dano: {self.dano}, Alcance: {self.alcance}, Carga: {self.carga_ataque}")
            try: 
                if self.hits == 25:
                    self.dano
                    self.alcance
                    self.carga_ataque
                    self.velocidade
                elif 10 < self.hits < 25:
                    self.dano += 30 
                    self.alcance += 40 
                    self.carga_ataque += 4
                    self.velocidade += 5
                else:
                    None
            except ValueError:
                None

    def carga(self, carga_ataque):
        carga_ataque = 4

    def velocidade_personagem(self, velocidade):
        velocidade = 5
    
    def dano_recebido(self, vida):
        """
        Quando o personagem estiver próximo de morrer, alguns atributos dele são aumentados
        """
        if self.downgrade_vida:
            self.dano += 10
            self.alcance += 5
            self.carga_ataque += 2
            self.velocidade += 8
        else:
            self.vida

    def evasao (self, dash):
        self.dash = 15
        if self.downgrade_vida:
            self.dash += 5
        else:
            self.dash
    
