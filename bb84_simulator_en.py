import random

PHOTONZO = "Photonzo"
BITBERT = "Bitbert"
EVETRON = "Evetron"

BASES = ["Z", "X", "Y"]
BITS = [0, 1]


def generate_list(options, amount):
    return [random.choice(options) for _ in range(amount)]


def measure(original_bit, original_basis, measurement_basis):
    if original_basis == measurement_basis:
        return original_bit
    return random.choice(BITS)


def show_list(name, values):
    print(f"{name}: {' '.join(map(str, values))}")


def ask_amount():
    while True:
        try:
            amount = int(input("How many bits do you want to simulate? (e.g., 10, 20, 50): "))
            if amount > 0:
                return amount
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def choose_role():
    print("Choose your role:")
    print(f"1. Play as {PHOTONZO}")
    print(f"2. Play as {BITBERT}")
    print(f"3. Play as {EVETRON}")

    role = input("Enter 1, 2, or 3: ").strip()

    while role not in ["1", "2", "3"]:
        print("Invalid option.")
        role = input("Enter 1, 2, or 3: ").strip()

    return role


def ask_yes_no(question):
    while True:
        answer = input(question).lower().strip()

        if answer in ["yes", "y"]:
            return True
        if answer in ["no", "n"]:
            return False

        print("Please answer yes or no.")


def simulate_bb84():
    role = choose_role()

    print(f"\n=== BB84 SIMULATOR (ENGLISH): {PHOTONZO}, {BITBERT}, and {EVETRON} ===\n")

    amount = ask_amount()

    # Decide whether Evetron will eavesdrop
    if role == "3":
        print(f"\n😈 You are {EVETRON}. You will eavesdrop automatically.")
        evetron_active = True
    else:
        evetron_active = ask_yes_no(f"Will {EVETRON} eavesdrop? yes/no: ")

    # Generate random bits and bases
    bits_photonzo = generate_list(BITS, amount)
    bases_photonzo = generate_list(BASES, amount)
    bases_bitbert = generate_list(BASES, amount)

    # Evetron intercepts and measures the bits
    if evetron_active:
        bases_evetron = generate_list(BASES, amount)
        bits_after_evetron = []

        for i in range(amount):
            intercepted_bit = measure(
                bits_photonzo[i],
                bases_photonzo[i],
                bases_evetron[i]
            )
            bits_after_evetron.append(intercepted_bit)
    else:
        bases_evetron = ["-"] * amount
        bits_after_evetron = bits_photonzo.copy()

    # Bitbert measures the received bits
    bits_bitbert = []

    for i in range(amount):
        received_bit = measure(
            bits_after_evetron[i],
            bases_photonzo[i],
            bases_bitbert[i]
        )
        bits_bitbert.append(received_bit)

    # Create the shared key using only matching bases
    key_photonzo = []
    key_bitbert = []

    for i in range(amount):
        if bases_photonzo[i] == bases_bitbert[i]:
            key_photonzo.append(bits_photonzo[i])
            key_bitbert.append(bits_bitbert[i])

    # Count mismatches in the shared key
    errors = 0

    for i in range(len(key_photonzo)):
        if key_photonzo[i] != key_bitbert[i]:
            errors += 1

    # Results based on the selected role
    print("\n--- RESULTS BASED ON YOUR ROLE ---")

    if role == "1":
        print(f"\nYou are {PHOTONZO}.")
        show_list("Your original bits", bits_photonzo)
        show_list("Your bases", bases_photonzo)
        show_list(f"{BITBERT}'s public bases", bases_bitbert)

    elif role == "2":
        print(f"\nYou are {BITBERT}.")
        show_list("Your bases", bases_bitbert)
        show_list("Your measured bits", bits_bitbert)
        show_list(f"{PHOTONZO}'s public bases", bases_photonzo)

    elif role == "3":
        print(f"\nYou are {EVETRON}.")
        show_list("Your eavesdropping bases", bases_evetron)
        show_list("Bits you measured", bits_after_evetron)
        print("If you used the wrong basis, you may have changed some bits without noticing.")

    # Public information
    print("\n--- PUBLIC INFORMATION ---")
    show_list(f"{PHOTONZO}'s bases", bases_photonzo)
    show_list(f"{BITBERT}'s bases", bases_bitbert)

    # Shared key
    print("\n--- SHARED KEY ---")
    print(f"Only the bits where {PHOTONZO} and {BITBERT} used the same basis are kept.")

    if len(key_photonzo) == 0:
        print("No key was generated because the bases never matched.")
    else:
        show_list(f"{PHOTONZO}'s key", key_photonzo)
        show_list(f"{BITBERT}'s key", key_bitbert)

    # Eavesdropping detection
    print("\n--- EAVESDROPPING DETECTION ---")

    if len(key_photonzo) == 0:
        print("Security could not be analyzed because no shared key was generated.")

    elif errors > 0:
        print(f"🚨 ALERT: {errors} error(s) detected.")
        print(f"{EVETRON} was detected eavesdropping.")
        print("The key is NOT secure and must be discarded.")

    else:
        if evetron_active:
            print("⚠️ No errors were detected, but there was eavesdropping.")
            print(f"{EVETRON} intervened but went unnoticed.")
            print("The key might NOT be secure.")
        else:
            print("✅ No eavesdropping was detected.")
            print("The key is secure.")

    # Summary
    print("\n--- SUMMARY ---")
    print(f"Simulated bits: {amount}")
    print(f"Matching bases: {len(key_photonzo)}")
    print(f"Detected errors: {errors}")

    if evetron_active:
        print(f"Real status: {EVETRON} did intervene.")
    else:
        print(f"Real status: {EVETRON} did not intervene.")


simulate_bb84()
