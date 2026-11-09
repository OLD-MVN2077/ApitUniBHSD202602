from fastapi import FastAPI, HTTPException

from database import conectar_banco, criar_tabelas
from models import RegistroCreate, RegistroResponse

app = FastAPI(
    title="API de Gerenciamento - Projeto A4",
    description="API em camadas integrando FastAPI, SQLite e validações Pydantic.",
    version="1.0.0",
)


@app.on_event("startup")
def startup_event():
    criar_tabelas()


@app.post("/registros", response_model=RegistroResponse, status_code=201)
def criar_registro(registro: RegistroCreate):
    if not registro.titulo.strip():
        raise HTTPException(status_code=400, detail="O título não pode estar em branco.")

    conn = conectar_banco()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO registros (titulo, descricao, ativo) VALUES (?, ?, ?)",
            (registro.titulo, registro.descricao, registro.ativo),
        )
        conn.commit()
        novo_id = cursor.lastrowid
        return {**registro.model_dump(), "id": novo_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno no banco de dados: {str(e)}")
    finally:
        conn.close()


@app.get("/registros", response_model=list[RegistroResponse], status_code=200)
def listar_registros():
    conn = conectar_banco()
    try:
        registros = conn.execute("SELECT * FROM registros").fetchall()
        return [dict(registro) for registro in registros]
    finally:
        conn.close()


@app.get("/registros/{registro_id}", response_model=RegistroResponse, status_code=200)
def buscar_registro(registro_id: int):
    conn = conectar_banco()
    try:
        registro = conn.execute(
            "SELECT * FROM registros WHERE id = ?", (registro_id,)
        ).fetchone()
    finally:
        conn.close()

    if registro is None:
        raise HTTPException(status_code=404, detail="Registro não encontrado.")

    return dict(registro)


@app.put("/registros/{registro_id}", response_model=RegistroResponse, status_code=200)
def atualizar_registro(registro_id: int, registro: RegistroCreate):
    conn = conectar_banco()
    try:
        existente = conn.execute(
            "SELECT * FROM registros WHERE id = ?", (registro_id,)
        ).fetchone()
        if existente is None:
            raise HTTPException(status_code=404, detail="Registro não encontrado para atualização.")

        conn.execute(
            "UPDATE registros SET titulo = ?, descricao = ?, ativo = ? WHERE id = ?",
            (registro.titulo, registro.descricao, registro.ativo, registro_id),
        )
        conn.commit()
        return {**registro.model_dump(), "id": registro_id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
    finally:
        conn.close()


@app.delete("/registros/{registro_id}", status_code=200)
def deletar_registro(registro_id: int):
    conn = conectar_banco()
    try:
        existente = conn.execute(
            "SELECT * FROM registros WHERE id = ?", (registro_id,)
        ).fetchone()
        if existente is None:
            raise HTTPException(status_code=404, detail="Registro não encontrado para exclusão.")

        conn.execute("DELETE FROM registros WHERE id = ?", (registro_id,))
        conn.commit()
        return {"mensagem": "Registro removido com sucesso."}
    finally:
        conn.close()