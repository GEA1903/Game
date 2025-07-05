from personagem import Personagem
from vilao import Vilao
from heroi import Heroi
import time # Para simular o tempo passando no jogo

def obter_inteiro_positivo(mensagem, min_val=0, max_val=9999):
    """Função auxiliar para obter uma entrada de inteiro positivo validada."""
    while True:
        try:
            valor = int(input(mensagem))
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"Valor inválido. Por favor, digite um número entre {min_val} e {max_val}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def obter_string_nao_vazia(mensagem):
    """Função auxiliar para obter uma entrada de string não vazia."""
    while True:
        valor = input(mensagem).strip() # .strip() remove espaços em branco extras
        if valor: # Verifica se a string não está vazia
            return valor
        else:
            print("Entrada não pode ser vazia. Por favor, digite um valor.")

# --- Nova função para criar Herói interativamente ---
def criar_heroi_interativo():
    print("\n--- CRIE SEU HERÓI ---")
    nome = obter_string_nao_vazia("Nome do Herói: ")
    idade = obter_inteiro_positivo("Idade do Herói: ", 1, 150)
    vida_maxima = obter_inteiro_positivo("Vida Máxima do Herói: ", 50, 500)
    dano = obter_inteiro_positivo("Dano Base do Herói: ", 5, 100)
    alcance = obter_inteiro_positivo("Alcance do Ataque (1-100): ", 1, 100)
    velocidade = obter_inteiro_positivo("Velocidade do Herói (1-20): ", 1, 20)
    genero = obter_string_nao_vazia("Gênero do Herói: ")
    especie = obter_string_nao_vazia("Espécie do Herói: ")
    max_carga_ataque = obter_inteiro_positivo("Máximo de Cargas de Ataque (2-5): ", 2, 5)
    defesa = obter_inteiro_positivo("Defesa do Herói: ", 0, 50)
    
    # Validação para Bondade (níveis específicos)
    niveis_bondade_validos = ['Baixa', 'Média', 'Alta']
    while True:
        bondade = obter_string_nao_vazia(f"Nível de Bondade ({', '.join(niveis_bondade_validos)}): ").capitalize()
        if bondade in niveis_bondade_validos:
            break
        else:
            print("Nível de bondade inválido. Escolha entre Baixa, Média, Alta.")

    # Magia (opcional)
    mana_maxima = 0
    tipo_magia = None
    quer_magia = obter_string_nao_vazia("Seu Herói usa magia? (sim/não): ").lower()
    if quer_magia == 'sim':
        mana_maxima = obter_inteiro_positivo("Mana Máxima do Herói: ", 10, 200)
        tipo_magia = obter_string_nao_vazia("Tipo de Magia (Ex: Divina, Arcana, Elemental): ")

    dash = False
    quer_dash = obter_string_nao_vazia("Seu Herói tem 'Dash'? (sim/não): ").lower()
    if quer_dash == 'sim':
        dash = True

    return Heroi(nome=nome, idade=idade, vida_maxima=vida_maxima, dano=dano, alcance=alcance, velocidade=velocidade,
                 genero=genero, especie=especie, hits=0, max_carga_ataque=max_carga_ataque, defesa=defesa,
                 bondade=bondade, mana_maxima=mana_maxima, tipo_magia=tipo_magia, dash=dash)

# --- Nova função para criar Vilão interativamente ---
def criar_vilao_interativo():
    print("\n--- CRIE O VILÃO ---")
    nome = obter_string_nao_vazia("Nome do Vilão: ")
    idade = obter_inteiro_positivo("Idade do Vilão: ", 50, 1000)
    vida_maxima = obter_inteiro_positivo("Vida Máxima do Vilão: ", 150, 1000)
    dano = obter_inteiro_positivo("Dano Base do Vilão: ", 10, 150)
    alcance = obter_inteiro_positivo("Alcance do Ataque (1-100): ", 1, 100)
    velocidade = obter_inteiro_positivo("Velocidade do Vilão (1-15): ", 1, 15)
    genero = obter_string_nao_vazia("Gênero do Vilão: ")
    especie = obter_string_nao_vazia("Espécie do Vilão: ")
    max_carga_ataque = obter_inteiro_positivo("Máximo de Cargas de Ataque do Vilão (1-3): ", 1, 3)
    defesa = obter_inteiro_positivo("Defesa do Vilão: ", 5, 80)

    # Validação para Maldade (níveis específicos)
    niveis_maldade_validos = ['Baixa', 'Média', 'Alta']
    while True:
        maldade = obter_string_nao_vazia(f"Nível de Maldade ({', '.join(niveis_maldade_validos)}): ").capitalize()
        if maldade in niveis_maldade_validos:
            break
        else:
            print("Nível de maldade inválido. Escolha entre Baixa, Média, Alta.")

    mana_maxima = 0
    tipo_magia = None
    quer_magia = obter_string_nao_vazia("Seu Vilão usa magia? (sim/não): ").lower()
    if quer_magia == 'sim':
        mana_maxima = obter_inteiro_positivo("Mana Máxima do Vilão: ", 20, 300)
        tipo_magia = obter_string_nao_vazia("Tipo de Magia (Ex: Sombria, Elemental, Mente): ")

    dash = False # Vilões podem ter dash também
    quer_dash = obter_string_nao_vazia("Seu Vilão tem 'Dash'? (sim/não): ").lower()
    if quer_dash == 'sim':
        dash = True

    return Vilao(nome=nome, idade=idade, vida_maxima=vida_maxima, dano=dano, alcance=alcance, velocidade=velocidade,
                 genero=genero, especie=especie, hits=0, max_carga_ataque=max_carga_ataque, defesa=defesa,
                 maldade=maldade, mana_maxima=mana_maxima, tipo_magia=tipo_magia, dash=dash)


def main():
    print("--- O DESPERTAR DOS HERÓIS ---")
    time.sleep(1) # Pausa por um segundo

    # --- 1. Inicialização dos Personagens Interativa ---
    print("\n[CENA 1: A Aldeia Pacífica]")
    # O usuário agora cria o herói principal
    heroi = criar_heroi_interativo() 

    # NPC pode ter valores padrão ou ser criado de forma simples
    npc = Personagem(nome='Zelda', idade=28, vida_maxima=80, dano=5, alcance=2, velocidade=3,
                     genero='Feminino', especie='Hylian', hits=0, max_carga_ataque=1, defesa=5)
    
    print(f"\n{heroi.nome} (Herói) está patrulhando a aldeia.")
    print(f"{npc.nome} (NPC) está no centro da aldeia.")

    print("\n--- STATUS INICIAL ---")
    print(heroi)
    print(npc)
    time.sleep(2)

    # --- 2. Evento: Ataque Inesperado do Vilão (criado pelo usuário) ---
    print("\n[CENA 2: A Ameaça Surge]")
    print("De repente, uma sombra colossal emerge das montanhas!")
    time.sleep(1.5)
    # O usuário agora cria o vilão
    vilao = criar_vilao_interativo()
    
    print(f"\n{vilao.nome} (Vilão) aparece e grita: 'Vocês não podem me deter!'")
    print(vilao)
    time.sleep(2)

    # --- 3. Diálogo e Decisão do Herói ---
    print(f"\n{npc.nome}: '{heroi.nome}, você deve lutar! A aldeia precisa de você!'")
    
    # Loop de decisão para o herói
    while True:
        escolha = input("O que você faz? (1) Enfrentar Ganon | (2) Fugir para a aldeia\nSua escolha: ").strip()
        if escolha == '1':
            print(f"\n{heroi.nome}: 'Eu não fujo de uma luta! Prepare-se, {vilao.nome}!'")
            time.sleep(1)
            break
        elif escolha == '2':
            print(f"\n{heroi.nome}: 'A aldeia é mais importante! Preciso avisá-los!'")
            print("Você tenta fugir, mas Ganon é muito rápido e o encurrala!")
            time.sleep(2)
            print("Você não tem escolha a não ser lutar!")
            break
        else:
            print("Escolha inválida. Por favor, digite '1' ou '2'.")

    # --- 4. Batalha (Estrutura de Repetição e Decisão) ---
    print("\n[CENA 3: A Batalha Começa!]")
    turno = 1
    # Loop principal da batalha
    while heroi.vida > 0 and vilao.vida > 0:
        print(f"\n--- TURNO {turno} ---")
        print(f"{heroi.nome} Vida: {heroi.vida}/{heroi.vida_maxima} | Mana: {heroi.mana}/{heroi.mana_maxima} | Cargas: {heroi.carga_ataque}/{heroi.max_carga_ataque}")
        print(f"{vilao.nome} Vida: {vilao.vida}/{vilao.vida_maxima} | Maldade: {vilao.maldade}")

        # --- Ações do Herói ---
        print(f"\n{heroi.nome}, é a sua vez!")
        acao_valida = False
        while not acao_valida:
            acao = input("Escolha sua ação: (1) Atacar | (2) Curar | (3) Habilidade Especial | (4) Defender\nSua ação: ").strip()
            
            if acao == '1': # Atacar
                if heroi.usar_ataque_com_carga(): # Usa o sistema de carga
                    print(f"{heroi.nome} ataca {vilao.nome}!")
                    vilao.receber_dano(heroi.dano) # Vilão recebe dano
                acao_valida = True
            elif acao == '2': # Curar (se o herói tiver habilidade de cura)
                # Verifica se o tipo de magia do herói é 'Divina' OU 'Cura' (se você tiver múltiplos tipos de cura)
                # E se o método de cura existe e for bem-sucedido
                if heroi.tipo_magia and ('divina' in heroi.tipo_magia.lower() or 'cura' in heroi.tipo_magia.lower()):
                    if heroi.curar_aliado(heroi, 25): # Herói se cura
                        acao_valida = True
                    else:
                        pass # Mensagem de mana insuficiente já é dada pelo curar_aliado
                else:
                    print("Seu herói não possui magia de cura ou não tem um tipo de magia definido!")
            elif acao == '3': # Habilidade Especial
                # Adapte a lógica aqui para chamar a habilidade_especial_heroi()
                # se o herói tiver uma definida e não estiver em cooldown
                if heroi.habilidade_especial_heroi_cooldown == 0:
                    # Exemplo: O herói pode escolher inspirar um aliado (o próprio NPC aqui)
                    # ou fazer um ataque especial dependendo do tipo de magia/arma.
                    # Aqui, faremos um ataque especial direto para simplificar o fluxo da batalha.
                    print(f"{heroi.nome} usa sua Habilidade Especial!")
                    dano_habilidade = heroi.dano * 1.8 # Ataque mais forte
                    vilao.receber_dano(dano_habilidade)
                    heroi.habilidade_especial_heroi_cooldown = 3 # Cooldown de 3 turnos
                    print(f"{heroi.nome} causou {dano_habilidade:.0f} de dano extra!")
                    acao_valida = True
                else:
                    print(f"Habilidade especial em cooldown. Restam {heroi.habilidade_especial_heroi_cooldown} turnos.")
            elif acao == '4': # Defender
                print(f"{heroi.nome} se prepara para defender!")
                # NOTA: Para uma defesa efetiva, o método 'receber_dano' do Personagem
                # precisaria saber se o personagem está defendendo naquele turno.
                # Por agora, aumentamos a defesa temporariamente, mas ela não será resetada automaticamente.
                # Você precisaria de um sistema de buffs/debuffs temporários.
                heroi.defesa += 5 # Buff temporário de defesa para o turno
                print(f"Defesa de {heroi.nome} aumentada para {heroi.defesa} neste turno.")
                acao_valida = True
            else:
                print("Ação inválida. Tente novamente.")
        
        # Reduzir cooldowns do herói e restaurar cargas/mana (simulando passar do tempo)
        if hasattr(heroi, 'reduzir_cooldowns'): # Verifica se o método existe
            heroi.reduzir_cooldowns() 
        if hasattr(heroi, 'recarregar_carga'):
            heroi.recarregar_carga() 
        if hasattr(heroi, 'restaurar_mana'):
            heroi.restaurar_mana(10) # Restaura 10 de mana por turno

        time.sleep(1)

        # --- Ações do Vilão (IA Simples) ---
        if vilao.vida > 0: # Vilão só ataca se estiver vivo
            print(f"\nÉ a vez de {vilao.nome}!")
            # Lógica de IA do vilão:
            # 1. Tentar ativar Super Ataque se a vida estiver baixa E o super não estiver ativo
            # 2. Tentar usar Habilidade Especial se não estiver em cooldown E tiver mana
            # 3. Caso contrário, atacar normalmente
            
            if vilao.vida <= vilao.vida_maxima * 0.3 and not vilao.is_super_ataque_ativo and hasattr(vilao, 'super_ataque_vilao'):
                vilao.super_ataque_vilao() # Tenta ativar super ataque
            elif vilao.habilidade_especial_vilao_cooldown == 0 and vilao.mana >= 30 and hasattr(vilao, 'habilidade_especial_vilao'):
                # Assumindo que habilidade_especial_vilao pode ter um alvo (heroi)
                vilao.habilidade_especial_vilao(heroi) # Vilão amaldiçoa herói (ou usa outra magia)
            else:
                vilao.ataque(heroi) # Vilão simplesmente ataca
            
            if hasattr(vilao, 'reduzir_cooldowns'): # Reduzir cooldowns do vilão
                vilao.reduzir_cooldowns()

        turno += 1
        time.sleep(2)

    # --- 5. Resultado da Batalha ---
    print("\n--- FIM DA BATALHA ---")
    if heroi.vida <= 0:
        print(f"Oh não! {heroi.nome} foi derrotado por {vilao.nome}!")
        print("Fim de Jogo!")
    else:
        print(f"Parabéns! {heroi.nome} derrotou {vilao.nome}!")
        print("A aldeia está segura por enquanto...")
        
    print("\n--- STATUS FINAL ---")
    print(heroi)
    print(vilao)

if __name__ == "__main__":
    main()
