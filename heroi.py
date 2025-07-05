from personagem import Personagem

class Heroi(Personagem):
    def __init__ (self, nome, bondade, idade, vida, dano, alcance, velocidade, genero, especie, hits, carga_ataque_inicial,  mana_maxima=0, tipo_magia=None, dash=0, super_ataque=None, defesa=0):
        super(). __init__ (nome, idade, vida, velocidade, genero, especie, dano, defesa, tipo_magia=None, mana_maxima=0)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if bondade not in niveis_validos:
            raise ValueError(f"Nível de bondade inválido! Escolha entre {niveis_validos}")
        self.bondade = bondade
        self.habilidade_especial_heroi_cooldown = 0 
        self.missoes_completas = 0 
        self.nivel_coragem = 1

    def curar_aliado(self, aliado: 'Personagem', quantidade_cura: int):
        """
        O herói cura um aliado, restaurando sua vida.
        Pode consumir mana ou ter um limite de usos por combate.
        """
        custo_mana = 25 # Custo de mana para a cura
        if self.mana >= custo_mana:
            self.mana -= custo_mana
            aliado.upgrade_vida(quantidade_cura) # Usa o método de upgrade_vida do aliado
            print(f"{self.nome} curou {aliado.nome} em {quantidade_cura} pontos de vida! (-{custo_mana} Mana)")
            return True
        else:
            print(f"{self.nome} não tem mana suficiente para curar {aliado.nome}. Mana atual: {self.mana}/{self.mana_maxima}.")
            return False

    def inspirar_aliado(self, aliado: 'Personagem'):
        """
        O herói inspira um aliado, concedendo um buff temporário de dano ou velocidade.
        """
        cooldown_inspire = 2 
        if self.habilidade_especial_heroi_cooldown == 0:
            print(f"{self.nome} inspirou {aliado.nome}, aumentando seu poder!")
         
            aliado.dano += 5
            aliado.velocidade += 2
            print(f"{aliado.nome} agora tem {aliado.dano} de dano e {aliado.velocidade} de velocidade.")

            self.habilidade_especial_heroi_cooldown = cooldown_inspire
            return True
        else:
            print(f"{self.nome} não pode inspirar agora. Cooldown restante: {self.habilidade_especial_heroi_cooldown}.")
            return False

    def completar_missao(self):
        """
        Registra uma missão completa para o herói, potencialmente aumentando um atributo.
        """
        self.missoes_completas += 1
        print(f"{self.nome} completou uma missão! Total de missões: {self.missoes_completas}.")
 
        if self.missoes_completas % 3 == 0:
            self.defesa += 1
            print(f"{self.nome} ganhou +1 de defesa por sua bravura! Defesa atual: {self.defesa}.")

    def __str__(self):
        """
        Retorna uma representação em string do herói, incluindo sua bondade.
        """
        personagem_str = super().__str__() 
        return f'{personagem_str}, Bondade: {self.bondade}, Missões: {self.missoes_completas}'


    


    
