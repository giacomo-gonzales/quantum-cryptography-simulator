import streamlit as st
import random

FOTONCIO = "Fotoncio"
BITBERTO = "Bitberto"
EVETRON = "Evetron"

BASES = ["Z", "X", "Y"]
BITS = [0, 1]

st.set_page_config(
    page_title="BB84 Quantum Game",
    page_icon="🔐",
    layout="centered"
)

def colored_bit(bit, match=True):
    color = "green" if match else "red"
    return f"<span style='color:{color}; font-size:24px; font-weight:bold'>{bit}</span>"

def measure(original_bit, original_basis, measurement_basis):
    if original_basis == measurement_basis:
        return original_bit
    return random.choice(BITS)

def reset_game():
    st.session_state.round_number = 0
    st.session_state.score = 0
    st.session_state.errors = 0
    st.session_state.matches = 0
    st.session_state.key_fotoncio = []
    st.session_state.key_bitberto = []
    st.session_state.full_fotoncio_bits = []
    st.session_state.full_bitberto_bits = []
    st.session_state.game_started = False
    st.session_state.game_finished = False
    st.session_state.current_bit = None
    st.session_state.current_basis = random.choices(BASES)
    st.session_state.evetron_basis = random.choices(BASES)
    st.session_state.bit_after_evetron = None
    st.session_state.last_result = ""
    st.session_state.balloon_shown = False

if "round_number" not in st.session_state:
    reset_game()

st.title("🔐 BB84 Quantum Game")
st.caption("Learn the BB84 quantum cryptography protocol by playing.")

st.markdown("""
### 🎮 Goal

You play as **Bitberto**.

**Fotoncio** sends a hidden bit using a hidden basis: `Z` or `X`.

Your job is to choose the correct basis.

If your basis matches Fotoncio's basis, the bit can become part of the shared key.

But if **Evetron** is spying, some bits may change and errors can reveal the attack.
""")

st.divider()

# 👥 PERSONAJES
st.markdown("## 👥 Quantum Team")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
        background-color:#1E1E1E;
        padding:20px;
        border-radius:15px;
        text-align:center;
        border:2px solid #FFD700;
    ">
        <h1>🟡</h1>
        <h3>Fotoncio</h3>
        <p>Quantum Sender</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background-color:#1E1E1E;
        padding:20px;
        border-radius:15px;
        text-align:center;
        border:2px solid #00BFFF;
    ">
        <h1>🔵</h1>
        <h3>Bitberto</h3>
        <p>The Player</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background-color:#1E1E1E;
        padding:20px;
        border-radius:15px;
        text-align:center;
        border:2px solid #FF4B4B;
    ">
        <h1>👾</h1>
        <h3>Evetron</h3>
        <p>Eavesdropper</p>
    </div>
    """, unsafe_allow_html=True)

rounds = st.slider("Number of rounds", 3, 20, 10)
evetron_active = st.checkbox("Enable Evetron as an eavesdropper", value=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Start new game"):
        reset_game()
        st.session_state.game_started = True

with col2:
    if st.button("🔄 Reset"):
        reset_game()

st.divider()

if st.session_state.game_started and not st.session_state.game_finished:

    if st.session_state.current_bit is None:
        st.session_state.current_bit = random.choice(BITS)
        st.session_state.current_basis = random.choice(BASES)

        if evetron_active:
            st.session_state.evetron_basis = random.choice(BASES)
            st.session_state.bit_after_evetron = measure(
                st.session_state.current_bit,
                st.session_state.current_basis,
                st.session_state.evetron_basis
            )
        else:
            st.session_state.evetron_basis = "-"
            st.session_state.bit_after_evetron = st.session_state.current_bit

    st.subheader(f"Round {st.session_state.round_number + 1} of {rounds}")

    st.progress((st.session_state.round_number) / rounds)

    st.info(f"{FOTONCIO} sent a hidden quantum bit. Choose a basis to measure it.")

    chosen_basis = st.radio(
        "Choose Bitberto's basis:",
        BASES,
        horizontal=True
    )

    if st.button("Measure bit"):

        measured_bit = measure(
            st.session_state.bit_after_evetron,
            st.session_state.current_basis,
            chosen_basis
        )

        st.session_state.full_fotoncio_bits.append(
            st.session_state.current_bit
        )

        st.session_state.full_bitberto_bits.append(
            measured_bit
        )

        if chosen_basis == st.session_state.current_basis:
            st.session_state.matches += 1
            st.session_state.key_fotoncio.append(st.session_state.current_bit)
            st.session_state.key_bitberto.append(measured_bit)
            st.session_state.full_fotoncio_bits.append(st.session_state.current_bit)
            st.session_state.full_bitberto_bits.append(measured_bit)

            if measured_bit == st.session_state.current_bit:
                st.session_state.score += 1
                st.session_state.last_result = "✅ Correct basis. The bit was kept safely."
            else:
                st.session_state.errors += 1
                st.session_state.last_result = "🚨 Correct basis, but the bit changed. Evetron may have been detected."
        else:
            st.session_state.last_result = "⚠️ Wrong basis. This bit was discarded."

        st.session_state.round_number += 1

        st.session_state.revealed_fotoncio_basis = st.session_state.current_basis
        st.session_state.revealed_fotoncio_bit = st.session_state.current_bit
        st.session_state.revealed_measured_bit = measured_bit
        st.session_state.revealed_chosen_basis = chosen_basis
        st.session_state.revealed_evetron_basis = st.session_state.evetron_basis

        st.session_state.current_bit = None
        st.session_state.current_basis = None
        st.session_state.evetron_basis = None
        st.session_state.bit_after_evetron = None

        st.session_state.balloon_shown = False

        if st.session_state.round_number >= rounds:
            st.session_state.game_finished = True

        st.rerun()

    if (
         "Correct basis" in st.session_state.last_result
         and not st.session_state.balloon_shown
     ):
        st.balloons()
        st.session_state.balloon_shown = True

        st.success(st.session_state.last_result)

        st.write("### 🎯 Last round details")

        match = (
            st.session_state.revealed_fotoncio_bit ==
            st.session_state.revealed_measured_bit
     )

        st.markdown(f"**Your basis:** {st.session_state.revealed_chosen_basis}")
        st.markdown(f"**{FOTONCIO}'s real basis:** {st.session_state.revealed_fotoncio_basis}")

        st.markdown(
           f"**{FOTONCIO}'s original bit:** "
           f"{colored_bit(st.session_state.revealed_fotoncio_bit, match)}",
           unsafe_allow_html=True
     )

        st.markdown(
           f"**Your measured bit:** "
           f"{colored_bit(st.session_state.revealed_measured_bit, match)}",
           unsafe_allow_html=True
     )

        if evetron_active:
            st.write(f"**{EVETRON}'s hidden basis:** {st.session_state.revealed_evetron_basis}")

    st.divider()

    st.write("### 📊 Current stats")
    st.write(f"**Score:** {st.session_state.score}")
    st.write(f"**Matching bases:** {st.session_state.matches}")
    st.write(f"**Detected errors:** {st.session_state.errors}")

elif st.session_state.game_finished:

    st.subheader("🏁 Game finished")

    st.write(f"**Total rounds:** {rounds}")
    st.write(f"**Score:** {st.session_state.score}")
    st.write(f"**Matching bases:** {st.session_state.matches}")
    st.write(f"**Detected errors:** {st.session_state.errors}")
    st.write("### 📜 Full transmission history")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🟡 Fotoncio")
        st.write(
            " ".join(
                map(str, st.session_state.full_fotoncio_bits)
            )
        )
    with col2:
        st.markdown("### 🔵 Bitberto")
        st.write(
            " ".join(
                map(str, st.session_state.full_bitberto_bits)
            )
        )

    st.write("### 🔑 Shared key")

    if len(st.session_state.key_fotoncio) == 0:
        st.warning("No shared key was generated.")
    else:
        st.write(f"**{FOTONCIO}'s key:** {' '.join(map(str, st.session_state.key_fotoncio))}")
        st.write(f"**{BITBERTO}'s key:** {' '.join(map(str, st.session_state.key_bitberto))}")

        st.write("### 📡 Fotoncio vs Bitberto")

        for i, (f, b) in enumerate(
            zip(st.session_state.key_fotoncio,
                st.session_state.key_bitberto),
            start=1
        ):
            if f == b:
                st.write(f"Round {i}: 🟢 {f} → {b}")
            else:
                st.write(f"Round {i}: 🔴 {f} → {b}")
        
        # 🔥 VISUALIZACIÓN
        st.write("### 🎨 Key visualization")

        key_visual = ""

        for f, b in zip(
            st.session_state.key_fotoncio,
            st.session_state.key_bitberto
        ):
            if f == b:
                key_visual += "🟢 "
            else:
                key_visual += "🔴 "
            st.markdown(f"<h2>{key_visual}</h2>", unsafe_allow_html=True)

    st.write("### 🛡️ Security result")

    if len(st.session_state.key_fotoncio) == 0:
        st.warning("Security could not be analyzed because no shared key was generated.")
    elif st.session_state.errors > 0:
        st.error(f"{EVETRON} was detected. The key is not secure and should be discarded.")
    else:
        if evetron_active:
            st.warning(f"No errors were detected, but {EVETRON} did eavesdrop. The key might not be secure.")
        else:
            st.success("No eavesdropping was detected. The key is secure.")

else:
    st.warning("Click **Start new game** to begin.")
