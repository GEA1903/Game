
class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, idade, vida, dano, alcance, velocidade, genero, especie, hits):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.dano = dano
        self.alcance = alcance
        self.velocidade = velocidade
        self.genero = genero
        self.especie = especie
        self.hits = hits


    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')


    def downgrade_vida(self):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        if self.vida > 15:
            self.vida -= 15
        else:
            self.vida = 0
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

   


    def velocidade_personagem(self, velocidade):
        self.velocidade = 5


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


                    
                


def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Dano {self.dano}, Alcance {self.alcance}, Gênero {self.genero}, Espécie {self.especie}'
