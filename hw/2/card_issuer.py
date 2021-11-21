import random


IIN_CARD_ISSUERS_MAP = {
    **{str(i): "American Express" for i in [34, 37]},
    "31": "China T-Union",
    "62": "China UnionPay",
    "36": "Diners Club International",
    "54": "Diners Club United States & Canada",
    "6011": "Discover Card",
    **{str(i): "Discover Card" for i in range(644, 650)},
    **{str(i): "Discover Card" for i in range(622126, 622926)},
    **{str(i): "UkrCard" for i in range(60400100, 60420100)},
    **{str(i): "RuPay" for i in [60, 65, 81, 82, 508, 353, 356]},
    "636": "InterPayment",
    **{str(i): "InstaPayment" for i in range(637, 640)},
    **{str(i): "JCB" for i in range(3528, 3590)},
    **{str(i): "Maestro UK" for i in [6759, 676770, 676774]},
    **{str(i): "Maestro" for i in [5018, 5020, 5038, 5893, 6304, 6759, 6761, 6762, 6763]},
    **{str(i): "Dankort" for i in [5019, 4571]},
    **{str(i): "Mir" for i in range(2200, 2205)},
    **{str(i): "NPS Pridnestrovie" for i in range(6054740, 6054745)},
    **{str(i): "Mastercard" for i in range(2221, 2721)},
    **{str(i): "Mastercard" for i in range(51, 56)},
    **{str(i): "Troy" for i in [65, 9792]},
    "4": "Visa",
    **{str(i): "Visa Electron" for i in [4026, 417500, 4508, 4844, 4913, 4917]},
    "1": "UATP",
    **{str(i): "Verve" for i in range(506099, 506199)},
    **{str(i): "Verve" for i in range(650002, 650028)},
    "357111": "LankaPay",
    "8600": "UzCard",
    "9860": "Humo"
}


def find_card_issuer(card):
    issuer = None
    iin = ""
    for i, sym in enumerate(card):
        iin += sym
        issuer = IIN_CARD_ISSUERS_MAP.get(iin)
        if i > 7 or issuer is not None:
            break
    return issuer


if __name__ == "__main__":
    card_number = f"{random.randint(1, 9)}" + "".join(str(random.randint(0, 9)) for _ in range(15))
    issuer = find_card_issuer(card_number)
    print(f"card number: {card_number}, issuer: {issuer if issuer is not None else 'issuer not found'}")
