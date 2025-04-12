def load_list(path):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado: {path}")
        return []
