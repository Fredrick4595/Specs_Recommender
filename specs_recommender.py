# game_recommender_streamlit.py
import streamlit as st

cross_recommend = {
    "resolution": ["2560x1440", "1920x1080", "1080x720"],
    "graphics": ["High", "Medium", "Low"],
}
#just a comment to check git changes
GAME_TYPES = ["AAA", "AA", "INDIE"]
PC_SPECS = ["High", "Medium", "Low"]

def recommend(pc_spec: str, game_type: str):
    # normalize inputs to predictable form
    pc = pc_spec.lower()
    g = game_type.upper()

    if pc == "high":
        return f"Recommended for HIGH spec: Resolution: {cross_recommend['resolution'][0]}, Graphics: {cross_recommend['graphics'][0]}"
    if pc == "medium":
        # for medium, pick 1080p and Medium graphics; but allow slight tweaks for indie/aa
        if g == "INDIE":
            return f"Recommended for MEDIUM spec (Indie): Resolution: {cross_recommend['resolution'][1]}, Graphics: {cross_recommend['graphics'][1]}"
        return f"Recommended for MEDIUM spec: Resolution: {cross_recommend['resolution'][1]}, Graphics: {cross_recommend['graphics'][1]}"
    if pc == "low":
        return f"Recommended for LOW spec: Resolution: {cross_recommend['resolution'][2]}, Graphics: {cross_recommend['graphics'][2]}"
    return "Give appropriate input"

def main():
    st.title("Game Settings Recommender")
    st.write("Choose your PC spec and the game type to get recommended resolution & graphics.")

    pc = st.selectbox("PC spec", PC_SPECS)
    game = st.selectbox("Game type", GAME_TYPES)

    if st.button("Recommend"):
        st.success(recommend(pc, game))
    
if __name__ == "__main__":
    main()
