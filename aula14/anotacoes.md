# Agregações naturais
"""
A | 250 - 1
03/05 | LUIS - 2
B | 250 - 1
GIG | 5530 - 3
03/05 | ANA - 2
07/05 | PEDRO - 2
SPS | 3058 - 3
"""

AGRUPADOS POR CLUSTERING
USANDO HEURISTICOS(PARA DESCOBERTA) DE AGREGAÇÕES NATURAL ENTRE OBJETOS

"""
GRUPO 1
A |250
B | 250

GRUPO 2
03/05 | LUIS
03/05 | ANA
07/05 | PEDRO

GRUPO 3
GIG | 5530
SPS | 3058
"""
--------------------------------------

"""
QTD | IDADE
1   |   15
1   |   20
3   |   25
2   |   26
5   |   40
1   |   41
3   |   42
2   |   33
1   |   51
"""

"""
IDADE   | QTD
0 |--15 | 0
15|--30 | 7
30|--45 | 11
45|--60 | 1
"""
----------------------------------------

CLASSIFICAR OS KDD SOB UMA ABORDAGEM BOTTON_UP COM DADOS E PADRÕES ENCONTRADOS

KNOWLEDGE-DISCOVERY UB DATABASE

---------------------------------------
CRISP-DM -> Serve de apoio ao KDD
|
|--> Cross Industry Standard Process For Data Mining 
      |
      |---> Compreensão do Negocio(1 exemplo), 
            Compreensão do Dados(1 exemplo), 
            Preparação dos Dados(1 exemplo), 
            Modelagem(1 exemplo), 
            Avaliação(1 exemplo),
            Dsenvolvimento(1 exemplo).

## Exercicio
Exemplo da Compreensão do Negocio: Realizar uma reunião com o dono de uma empresa para o entedimento e esclarecimento do negocio desse segmento, para realizar um possivel desenvolvimento de uma solução.

Exemplo da Compreensão do Dados: Realizar um estudo na base de dados e documentar seus objetos, como tabelas de um banco de dados Oracle.
È possivel realizar um estudo de dados se houver uma plataforma de dicionario de dados.

Dicionário de Dados para Sistema de Gestão de Biblioteca
1. Livros:

id: Identificador único do livro (int).
titulo: Título do livro (str).
autor: Nome do autor do livro (str).
ano_publicacao: Ano de publicação do livro (int).
genero: Gênero do livro (str).
editora: Nome da editora do livro (str).
disponivel: Indica se o livro está disponível para empréstimo (bool).
numero_exemplares: Número total de exemplares disponíveis do livro (int).

2. Usuários:

id: Identificador único do usuário (int).
nome: Nome completo do usuário (str).
idade: Idade do usuário (int).
telefone: Número de telefone do usuário (str).
email: Endereço de e-mail do usuário (str).
livros_emprestados: Lista de IDs dos livros atualmente emprestados pelo usuário (list of int).

Exemplo da Preparação dos Dados: Realizar a criação de um script, uma procedure SQL/Oracle, que nessa procedure tenha etapas de criação de variaveis e execuções de regras para preparar os dados para um destino.

CREATE OR REPLACE PROCEDURE calcular_idade_usuarios AS
BEGIN
    -- Cursor para percorrer os registros da tabela usuarios
    FOR registro IN (SELECT id_usuario, data_nascimento FROM usuarios) LOOP
        -- Calcular a idade baseada na data de nascimento
        DECLARE
            v_idade NUMBER;
            v_data_nascimento DATE := registro.data_nascimento;
            v_data_atual DATE := SYSDATE; -- Data atual do sistema
        BEGIN
            -- Calcular a idade em anos
            SELECT TRUNC(MONTHS_BETWEEN(v_data_atual, v_data_nascimento) / 12) INTO v_idade FROM dual;
            
            -- Atualizar o campo idade na tabela usuarios
            UPDATE usuarios SET idade = v_idade WHERE id_usuario = registro.id_usuario;
            
            -- Commit para aplicar as alterações
            COMMIT;
        EXCEPTION
            WHEN OTHERS THEN
                -- Tratamento de exceção, se necessário
                DBMS_OUTPUT.PUT_LINE('Erro ao calcular idade para o usuário ' || registro.id_usuario);
        END;
    END LOOP;
    
    -- Mensagem de sucesso
    DBMS_OUTPUT.PUT_LINE('Processo de cálculo de idade concluído com sucesso.');
EXCEPTION
    WHEN OTHERS THEN
        -- Tratamento de exceção global
        DBMS_OUTPUT.PUT_LINE('Erro ao executar a procedure calcular_idade_usuarios: ' || SQLERRM);
END calcular_idade_usuarios;

Exemplo da Modelagem: Realizar a criação de um objeto ou tabela no banco de dados Oracle, que contenha as informações e regras de negocio e dados que foram compreendidas em seus estudos. 

CREATE TABLE Livro (
    id_livro NUMBER PRIMARY KEY,
    titulo VARCHAR2(100),
    autor VARCHAR2(100),
    ano_publicacao NUMBER,
    genero VARCHAR2(50),
    editora VARCHAR2(100),
    numero_exemplares NUMBER
);

Exemplo de Avaliação: Realizar testes e validação com o cliente que será entregue essa solução de dados, para que essa solucução seja entregue como o esperado.
-- Inserindo dados na tabela Livro
INSERT INTO Livro (id_livro, titulo, autor, ano_publicacao, genero, editora, numero_exemplares)
VALUES (1, 'Dom Casmurro', 'Machado de Assis', 1899, 'Romance', 'Editora A', 5);

SELECT * FROM Livro;

Exemplo de Desenvolvimento: Com todas as etapas mapeadas, realizar o desenvolvimento da solução, com uma ou varias linguagem de programação ou outras teconologias. Criar novas tabelas em banco de dados, e mapear essas tabelas em um processo já existente para entregar ao cliente.