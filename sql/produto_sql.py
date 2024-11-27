SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        descricao VARCHAR(1000) NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL,
        idCategoria INTEGER NOT NULL FOREIGN KEY REFERENCES id(categoria);
"""

SQL_INSERIR = """
    INSERT INTO produto (nome, descricao, preco, estoque, idCategoria) 
    VALUES (?, ?, ?, ?);
"""

SQL_ALTERAR = """
    UPDATE produto 
    SET nome = ?, descricao = ?, preco = ?, estoque = ?, idCategoria = ? 
    WHERE id = ?;
"""

SQL_EXCLUIR = """
    DELETE FROM produto 
    WHERE id = ?;
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, descricao, preco, estoque, idCategoria 
    FROM produto 
    WHERE id = ?;
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, descricao, preco, estoque, idCategoria
    FROM produto 
    ORDER BY nome;
"""
