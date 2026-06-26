import streamlit as st
import random
import pandas as pd

PHOTONZO = "Photonzo"
BITBERT = "Bitbert"
EVETRON = "Evetron"

BASES = ["Z", "X", "Y"]
BITS = [0, 1]

st.set_page_config(
    page_title="Quantum Cryptography Simulator",
    page_icon="🔐",
    layout="centered"
)

st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #050816, #0B1120, #111827); }

[data-testid="stMetric"] {
    background-color:rgba(255,255,255,0.05);
    border:1px solid rgba(0,229,255,0.3);
    border-radius:15px;
    padding:15px;
}

.quantum-card {
    background:rgba(255,255,255,0.06);
    border-radius:20px;
    padding:20px;
    text-align:center;
    backdrop-filter:blur(10px);
}

div.stButton > button {
    border: 2px solid #00E5FF !important;
    background-color: transparent !important;
    color: #00E5FF !important;
    border-radius: 10px !important;
    transition: 0.3s !important;
}
div.stButton > button:hover {
    background-color: #00E5FF !important;
    color: black !important;
    box-shadow: 0 0 15px #00E5FF;
}
</style>
""", unsafe_allow_html=True)

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
    st.session_state.key_photonzo = []
    st.session_state.key_bitbert = []
    st.session_state.full_photonzo_bits = []
    st.session_state.full_bitbert_bits = []
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

st.markdown("""
<h1 style='
text-align:center;
color:#00E5FF;
font-size:50px;
text-shadow:0px 0px 20px #00E5FF;
margin-bottom:0px;
'>
🔐 Quantum Cryptography Simulator
</h1>

<p style='
text-align:center;
font-size:20px;
color:#BBBBBB;
margin-top:0px;
'>
Explore, play, and learn the principles of quantum secure communication.
</p>
""", unsafe_allow_html=True)

st.markdown("""
### 🎮 Goal

You play as **Bitbert**.

Photonzo sends a hidden quantum bit using one of three secret bases: Z, X, or Y.

Your job is to choose the correct basis.

If your basis matches Photonzo's basis, the bit can become part of the shared key.

But if **Evetron** is spying, some bits may change and errors can reveal the attack.
""")

st.divider()

st.markdown("## 👥 Quantum Team")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="quantum-card">
        <h1 style="font-size:70px">🟡</h1>
        <h2 style="color:#FFD700">
        Photonzo
        </h2>
        <p>Quantum Sender</p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="quantum-card">
        <h1 style="font-size:70px">🔵</h1>
        <h2 style="color:#00BFFF">
        Bitbert
        </h2>
        <p>The Player</p>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="quantum-card">
        <h1 style="font-size:70px">👾</h1>
        <h2 style="color:#FF4B4B">
        Evetron
        </h2>
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
    with st.container(border=True):
        st.subheader(f"Round {st.session_state.round_number + 1} of {rounds}")
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

    st.progress((st.session_state.round_number) / rounds)

    st.info(f"{PHOTONZO} sent a hidden quantum bit. Choose a basis to measure it.")

    chosen_basis = st.radio(
        "Choose Bitbert's basis:",
        BASES,
        horizontal=True
    )

    if st.button("Measure bit"):
        
        measured_bit = measure(
            st.session_state.bit_after_evetron,
            st.session_state.current_basis,
            chosen_basis
        )

        st.session_state.full_photonzo_bits.append(
            st.session_state.current_bit
        )

        st.session_state.full_bitbert_bits.append(
            measured_bit
        )

        if chosen_basis == st.session_state.current_basis:
            st.session_state.matches += 1
            st.session_state.key_photonzo.append(st.session_state.current_bit)
            st.session_state.key_bitbert.append(measured_bit)
            st.session_state.full_photonzo_bits.append(st.session_state.current_bit)
            st.session_state.full_bitbert_bits.append(measured_bit)

            if measured_bit == st.session_state.current_bit:
                st.session_state.score += 1
                st.session_state.last_result = "✅ Correct basis. The bit was kept safely."
            else:
                st.session_state.errors += 1
                st.session_state.last_result = "🚨 Correct basis, but the bit changed. Evetron may have been detected."
        else:
            st.session_state.last_result = "⚠️ Wrong basis. This bit was discarded."

        st.session_state.round_number += 1

        st.session_state.revealed_photonzo_basis = st.session_state.current_basis
        st.session_state.revealed_photonzo_bit = st.session_state.current_bit
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
            st.session_state.revealed_photonzo_bit ==
            st.session_state.revealed_measured_bit
     )

        st.markdown(f"**Your basis:** {st.session_state.revealed_chosen_basis}")
        st.markdown(f"**{PHOTONZO}'s real basis:** {st.session_state.revealed_photonzo_basis}")

        st.markdown(
           f"**{PHOTONZO}'s original bit:** "
           f"{colored_bit(st.session_state.revealed_photonzo_bit, match)}",
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

    st.write("## 📊 Quantum Dashboard")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🏆 Score",
            st.session_state.score
        )

    with c2:
        st.metric(
            "🎯 Matches",
            st.session_state.matches
        )

    with c3:
        st.metric(
            "🚨 Errors",
            st.session_state.errors
        )

elif st.session_state.game_finished:

    st.subheader("🏁 Game finished")

    st.write(f"**Total rounds:** {rounds}")
    st.write(f"**Score:** {st.session_state.score}")
    st.write(f"**Matching bases:** {st.session_state.matches}")
    st.write(f"**Detected errors:** {st.session_state.errors}")
    st.write("### 📜 Transmission History")

    df = pd.DataFrame({
        "🟡 Photonzo": st.session_state.full_photonzo_bits,
        "🔵 Bitbert": st.session_state.full_bitbert_bits
    })

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.write("### 🔑 Shared key")

    if len(st.session_state.key_photonzo) == 0:
        st.warning("No shared key was generated.")
    else:
        st.write(f"**{PHOTONZO}'s key:** {' '.join(map(str, st.session_state.key_photonzo))}")
        st.write(f"**{BITBERT}'s key:** {' '.join(map(str, st.session_state.key_bitbert))}")

        st.write("### 📡 Photonzo vs Bitbert")

        for i, (f, b) in enumerate(
            zip(st.session_state.key_photonzo,
                st.session_state.key_bitbert),
            start=1
        ):
            if f == b:
                st.write(f"Round {i}: 🟢 {f} → {b}")
            else:
                st.write(f"Round {i}: 🔴 {f} → {b}")
        
        st.write("### 🔑 Shared Key Visualization")
        
        html = ""
        for f, b in zip(st.session_state.key_photonzo, st.session_state.key_bitbert):
            color = "#00FF88" if f == b else "#FF4444"
            
            html += f"<span style='background:{color}; padding:12px; margin:4px; border-radius:10px; font-size:25px; color:black; font-weight:bold; display:inline-block; min-width:35px; text-align:center;'>{f}</span>"

        st.markdown(html, unsafe_allow_html=True)

    st.write("### 🛡️ Security result")

    if len(st.session_state.key_photonzo) == 0:
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
