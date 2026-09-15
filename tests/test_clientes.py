import os

from src.database.db import Database
from src.main import check_online_status


def test_salvar_e_listar_cliente():
    db_path = "tests/test_pdv_temp.db"
    if os.path.exists(db_path):
        os.remove(db_path)

    db = Database(db_name=db_path)
    try:
        cliente_id = db.save_cliente(
            nome="Maria Souza",
            cpf="12345678900",
            email="maria@teste.com",
            telefone="11999999999",
            endereco="Rua A, 123",
        )

        clientes = db.listar_clientes()

        assert cliente_id > 0
        assert any(c["nome"] == "Maria Souza" for c in clientes)
        assert any(c["cpf"] == "12345678900" for c in clientes)
    finally:
        db.close_connection()
        if os.path.exists(db_path):
            os.remove(db_path)


def test_check_online_status_invalido():
    status = check_online_status("https://github.invalid")

    assert status["online"] is False
    assert "offline" in status["status"].lower()
