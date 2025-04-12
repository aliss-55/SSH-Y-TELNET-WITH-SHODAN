import shodan

def validar_api_key(api_key):
    try:
        api = shodan.Shodan(api_key)
        info = api.info()
        print(f"✅ API Key válida. Créditos disponibles: {info['query_credits']}")
        return True
    except shodan.APIError as e:
        print(f"❌ Error al validar API Key: {e}")
        return False

def buscar_ips_shodan(api_key, query, limit=50):
    api = shodan.Shodan(api_key)
    try:
        resultados = api.search(query, limit=limit)
        ips = [match['ip_str'] for match in resultados['matches']]
        print(f"🌐 Se encontraron {len(ips)} dispositivos.")
        return ips
    except shodan.APIError as e:
        print(f"❌ Error en búsqueda Shodan: {e}")
        return []
