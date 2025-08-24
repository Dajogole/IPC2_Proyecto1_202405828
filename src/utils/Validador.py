def requerido(valor, msg):
    if not valor or not str(valor).strip():
        raise ValueError(msg)
