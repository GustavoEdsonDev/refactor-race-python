# legacy_checkout.py

ORDERS_PROCESSED = []

# --- CONSTANTES ---
EXPRESS_SHIPPING_MULTIPLIER = 1.8
TAX_RATES = {
    "MG": 0.07,
    "SP": 0.09,
    "RJ": 0.08,
    "ES": 0.07
}
DEFAULT_TAX_RATE = 0.12
SOUTHEAST_STATES = {"MG", "SP", "RJ", "ES"}

# --- FUNÇÕES EXTRAÍDAS ---

def calculate_subtotal(items):
    return sum(item["price"] * item["qty"] for item in items if item["qty"] > 0)

def calculate_discount(customer, subtotal, coupon):
    desconto = 0
    
    # Desconto por tipo de cliente
    if customer["type"] == "vip":
        desconto = subtotal * 0.15 if subtotal >= 1000 else subtotal * 0.10
    elif customer["type"] == "employee":
        desconto = subtotal * 0.20
    elif customer["type"] == "regular" and subtotal >= 800:
        desconto = subtotal * 0.05

    # Cupons
    if coupon == "PROMO10":
        desconto += subtotal * 0.10
    elif coupon == "PROMO20" and subtotal >= 500:
        desconto += subtotal * 0.20
    elif coupon == "VIP50" and customer["type"] == "vip":
        desconto += 50

    # Limite de desconto (máximo 25% do subtotal)
    return min(desconto, subtotal * 0.25)

def calculate_shipping(subtotal, items, state, express):
    if subtotal >= 500 and not express:
        return 0

    peso_total = sum(item.get("weight", 0) * item["qty"] for item in items)
    
    frete_base = 20 + peso_total * 0.4 if state in SOUTHEAST_STATES else 35 + peso_total * 0.6
    
    return frete_base * EXPRESS_SHIPPING_MULTIPLIER if express else frete_base

def calculate_tax(valor_com_desconto, state):
    taxa = TAX_RATES.get(state, DEFAULT_TAX_RATE)
    return valor_com_desconto * taxa

def calculate_points(customer, total_gasto):
    divisor = 5 if customer["type"] == "vip" else 10
    return int(total_gasto / divisor)

def find_duplicate_products(items):
    vistos = set()
    duplicados = set()
    for item in items:
        nome = item["name"]
        if nome in vistos:
            duplicados.add(nome)
        else:
            vistos.add(nome)
    return list(duplicados)

# --- FUNÇÃO PRINCIPAL ---

def process_order(customer, items, coupon="", state="MG", express=False):
    
    subtotal = calculate_subtotal(items)
    desconto = calculate_discount(customer, subtotal, coupon)
    valor_com_desconto = subtotal - desconto
    
    frete = calculate_shipping(subtotal, items, state, express)
    imposto = calculate_tax(valor_com_desconto, state)
    
    total_gasto = valor_com_desconto + frete + imposto
    pontos = calculate_points(customer, total_gasto)
    
    duplicados = find_duplicate_products(items)
    total_final = round(total_gasto, 2)

    resultado = {
        "customer": customer["name"],
        "subtotal": round(subtotal, 2),
        "discount": round(desconto, 2),
        "shipping": round(frete, 2),
        "tax": round(imposto, 2),
        "total": total_final,
        "points": pontos,
        "duplicate_products": duplicados
    }

    ORDERS_PROCESSED.append(resultado)

    print(f"Pedido processado para {customer['name']}")
    print(f"Subtotal: {subtotal}")
    print(f"Desconto: {desconto}")
    print(f"Frete: {frete}")
    print(f"Imposto: {imposto}")
    print(f"TOTAL: {total_final}")

    return resultado