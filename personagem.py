class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, idade, vida, dano, alcance, velocidade, genero, especie, hits, carga_ataque_inicial,  mana_maxima=0, tipo_magia=None, dash=0, super_ataque=None, defesa=0):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.dano = dano
        self.alcance = alcance
        self.velocidade = velocidade
        self.genero = genero
        self.especie = especie
        self.hits = hits
        self.mana_maxima = mana_maxima
        self. mana = mana_maxima
        self.tipo_magia = tipo_magia
        self.dash = dash
        self.defesa = defesa
        self.super_ataque = super_ataque
        self.max_carga_ataque = carga_ataque_inicial # Define a capacidade máxima
        self.carga_ataque = carga_ataque_inicial 

        
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

   


    def velocidade_personagem(self):
        self.velocidade = 5


    def dano_recebido(self):
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

    def usar_magia(self, custo_mana, nome_magia):
        """
        Permite que seja usado magia, mas isso consome mana
        """
        if self.mana >= custo_mana:
            self.mana -= custo_mana
            print(f"{self.nome} usou {nome_magia} ! Mana restante: {nome_magia}. Mana atual: {self.mana}/{self.mana_maxima}")
            return True 
        else:
            print(f"{self.nome} não tem mana suficiente para usar '{nome_magia}'. Mana atual: {self.mana}/{self.mana_maxima}")
            return False
        
    
    def restaurar_mana (self, quantidade_restaurada):
        """
        Restaura a mana do personagem
        """
        self.mana += quantidade_restaurada
        if self.mana > self.mana_maxima:
            self.mana = self.mana_maxima
        print(f"Mana de {self.nome} restaurada em {quantidade_restaurada} ana atual: {self.mana}/{self.mana_maxima}")
                    
                

    def super_ataque(self):
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

    def carga(self):
        """
        Quantidade de vezes que o personagem pode atacar, sendo recarregado constantemente quando uma carga é utilizada
        """
        if self.carga_ataque > 0:
            self.carga_ataque -= 1
            print(f"{self.nome} realizou um ataque com carga! Cargas restantes: {self.carga_ataque}/{self.max_carga_ataque}")
            return True
        else:
            print(f"{self.nome} não tem cargas de ataque disponíveis!")
            return False
        
    def recarregar_carga(self, quantidade_recarregada=1):
        """
        Recarrega a carga de ataque do personagem em uma certa quantidade,
        até o limite da carga máxima.
        """
        if self.carga_ataque < self.max_carga_ataque:
            self.carga_ataque += quantidade_recarregada
            # Garante que a carga não exceda o máximo
            if self.carga_ataque > self.max_carga_ataque:
                self.carga_ataque = self.max_carga_ataque
            print(f"Carga de ataque de {self.nome} recarregada em {quantidade_recarregada}. Cargas atuais: {self.carga_ataque}/{self.max_carga_ataque}")
        else:
            print(f"{self.nome} já tem carga de ataque máxima.")


    def velocidade_personagem(self):
        """
        Velocidade padrão de locomoção do personagem
        """
        velocidade = 5
    
    def dano_recebido(self):
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

    def evasao (self):
        """
        O personagem tem a habilidade de dar dashs/avanços rápidos, seja para desviar de ataques ou se locomover mais rápido
        """
        self.dash = 15
        if self.downgrade_vida:
            self.dash += 5
        else:
            self.dash

    def escudo (self):
        """
        Indica os pontos de defesa que protegem a vida do personagem
        """
        self.defesa = 10
        if self.downgrade_vida:
            self.defesa += 10
        else: 
            None







def __str__(self):
        """
        Retorna uma representação em string do personagem.
        """
        return (f'Personagem: {self.nome} (Idade: {self.idade}, {self.genero} de {self.especie}), '
                f'Vida: {self.vida}/{self.vida_maxima}, Mana: {self.mana}/{self.mana_maxima}, Tipo de Magia: {self.tipo_magia}, '
                f'Dano: {self.dano}, Alcance: {self.alcance}, Velocidade: {self.velocidade}')
