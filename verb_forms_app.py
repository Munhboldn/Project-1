import streamlit as st
import random
import base64

# Dictionary with irregular verbs only (base, past, and past participle forms)
verb_dict = {
    "arise": {"past": "arose", "participle": "arisen"},
    "be": {"past": "was/were", "participle": "been"},
    "bear": {"past": "bore", "participle": "born"},
    "become": {"past": "became", "participle": "become"},
    "begin": {"past": "began", "participle": "begun"},
    "bend": {"past": "bent", "participle": "bent"},
    "bet": {"past": "bet", "participle": "bet"},
    "bite": {"past": "bit", "participle": "bitten"},
    "bleed": {"past": "bled", "participle": "bled"},
    "blow": {"past": "blew", "participle": "blown"},
    "break": {"past": "broke", "participle": "broken"},
    "bring": {"past": "brought", "participle": "brought"},
    "build": {"past": "built", "participle": "built"},
    "burn": {"past": "burned/burnt", "participle": "burned/burnt"},
    "buy": {"past": "bought", "participle": "bought"},
    "catch": {"past": "caught", "participle": "caught"},
    "choose": {"past": "chose", "participle": "chosen"},
    "come": {"past": "came", "participle": "come"},
    "cost": {"past": "cost", "participle": "cost"},
    "creep": {"past": "crept", "participle": "crept"},
    "cut": {"past": "cut", "participle": "cut"},
    "do": {"past": "did", "participle": "done"},
    "draw": {"past": "drew", "participle": "drawn"},
    "drink": {"past": "drank", "participle": "drunk"},
    "drive": {"past": "drove", "participle": "driven"},
    "eat": {"past": "ate", "participle": "eaten"},
    "fall": {"past": "fell", "participle": "fallen"},
    "feel": {"past": "felt", "participle": "felt"},
    "fight": {"past": "fought", "participle": "fought"},
    "find": {"past": "found", "participle": "found"},
    "fly": {"past": "flew", "participle": "flown"},
    "forget": {"past": "forgot", "participle": "forgotten"},
    "forgive": {"past": "forgave", "participle": "forgiven"},
    "freeze": {"past": "froze", "participle": "frozen"},
    "get": {"past": "got", "participle": "gotten/got"},
    "give": {"past": "gave", "participle": "given"},
    "go": {"past": "went", "participle": "gone"},
    "grow": {"past": "grew", "participle": "grown"},
    "hang": {"past": "hung", "participle": "hung"},
    "have": {"past": "had", "participle": "had"},
    "hear": {"past": "heard", "participle": "heard"},
    "hide": {"past": "hid", "participle": "hidden"},
    "hit": {"past": "hit", "participle": "hit"},
    "hold": {"past": "held", "participle": "held"},
    "hurt": {"past": "hurt", "participle": "hurt"},
    "keep": {"past": "kept", "participle": "kept"},
    "kneel": {"past": "knelt", "participle": "knelt"},
    "know": {"past": "knew", "participle": "known"},
    "lay": {"past": "laid", "participle": "laid"},
    "lead": {"past": "led", "participle": "led"},
    "leave": {"past": "left", "participle": "left"},
    "lend": {"past": "lent", "participle": "lent"},
    "let": {"past": "let", "participle": "let"},
    "lie": {"past": "lay", "participle": "lain"},
    "light": {"past": "lit/lighted", "participle": "lit/lighted"},
    "lose": {"past": "lost", "participle": "lost"},
    "make": {"past": "made", "participle": "made"},
    "mean": {"past": "meant", "participle": "meant"},
    "meet": {"past": "met", "participle": "met"},
    "pay": {"past": "paid", "participle": "paid"},
    "put": {"past": "put", "participle": "put"},
    "quit": {"past": "quit", "participle": "quit"},
    "read": {"past": "read", "participle": "read", "pronunciation": "/red/"},
    "ride": {"past": "rode", "participle": "ridden"},
    "ring": {"past": "rang", "participle": "rung"},
    "rise": {"past": "rose", "participle": "risen"},
    "run": {"past": "ran", "participle": "run"},
    "say": {"past": "said", "participle": "said"},
    "see": {"past": "saw", "participle": "seen"},
    "sell": {"past": "sold", "participle": "sold"},
    "send": {"past": "sent", "participle": "sent"},
    "set": {"past": "set", "participle": "set"},
    "sew": {"past": "sewed", "participle": "sewn/sewed"},
    "shake": {"past": "shook", "participle": "shaken"},
    "shine": {"past": "shone", "participle": "shone"},
    "shoot": {"past": "shot", "participle": "shot"},
    "show": {"past": "showed", "participle": "shown"},
    "shrink": {"past": "shrank", "participle": "shrunk"},
    "shut": {"past": "shut", "participle": "shut"},
    "sing": {"past": "sang", "participle": "sung"},
    "sink": {"past": "sank", "participle": "sunk"},
    "sit": {"past": "sat", "participle": "sat"},
    "sleep": {"past": "slept", "participle": "slept"},
    "slide": {"past": "slid", "participle": "slid"},
    "sling": {"past": "slung", "participle": "slung"},
    "slink": {"past": "slunk", "participle": "slunk"},
    "speak": {"past": "spoke", "participle": "spoken"},
    "spend": {"past": "spent", "participle": "spent"},
    "spill": {"past": "spilt/spilled", "participle": "spilt/spilled"},
    "spin": {"past": "spun", "participle": "spun"},
    "spit": {"past": "spat", "participle": "spat"},
    "splead": {"past": "spled", "participle": "spled"},
    "spread": {"past": "spread", "participle": "spread"},
    "spring": {"past": "sprang", "participle": "sprung"},
    "stand": {"past": "stood", "participle": "stood"},
    "steal": {"past": "stole", "participle": "stolen"},
    "stick": {"past": "stuck", "participle": "stuck"},
    "sting": {"past": "stung", "participle": "stung"},
    "stink": {"past": "stank", "participle": "stunk"},
    "strike": {"past": "struck", "participle": "struck"},
    "swear": {"past": "swore", "participle": "sworn"},
    "sweep": {"past": "swept", "participle": "swept"},
    "swell": {"past": "swelled", "participle": "swollen"},
    "swim": {"past": "swam", "participle": "swum"},
    "take": {"past": "took", "participle": "taken"},
    "teach": {"past": "taught", "participle": "taught"},
    "tear": {"past": "tore", "participle": "torn"},
    "tell": {"past": "told", "participle": "told"},
    "think": {"past": "thought", "participle": "thought"},
    "throw": {"past": "threw", "participle": "thrown"},
    "tread": {"past": "trod", "participle": "trodden"},
    "understand": {"past": "understood", "participle": "understood"},
    "wake": {"past": "woke", "participle": "woken"},
    "wear": {"past": "wore", "participle": "worn"},
    "weave": {"past": "wove", "participle": "woven"},
    "weep": {"past": "wept", "participle": "wept"},
    "win": {"past": "won", "participle": "won"},
    "wind": {"past": "wound", "participle": "wound"},
    "withdraw": {"past": "withdrew", "participle": "withdrawn"},
    "write": {"past": "wrote", "participle": "written"},
}

# Function to set a background image from a URL
def add_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background image from the GitHub URL
add_bg_from_url("https://raw.githubusercontent.com/Munhboldn/Project-1/main/10139763.jpg")

# App setup 
st.title("✨ Irregular Verb Form Finder ✨")
st.write("Enter an irregular verb to see its **past tense** and **past participle** forms. If you need inspiration, try the random verb button below!")

# Favorites list initialization
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# Random Verb Button
if st.button("🔄 Show Me a Random Verb"):
    verb = random.choice(list(verb_dict.keys()))
    st.write(f"Here’s a verb for you: **{verb.capitalize()}**")
else:
    # Search functionality
    search_term = st.text_input("Search for a verb:")
    verb_list = [v for v in verb_dict.keys() if search_term.lower() in v]
    verb = st.selectbox("Choose a verb:", verb_list)

# Display results
if verb:
    verb_forms = verb_dict.get(verb)
    if verb_forms:
        # Display in a table format
        st.write(f"### Forms for **{verb.capitalize()}**")
        st.table({
            "Base Form": [verb.capitalize()],
            "Past Tense": [verb_forms['past']],
            "Past Participle": [verb_forms['participle']],
        })
        
        # Add to favorites button
        if st.button("💖 Add to Favorites"):
            st.session_state.favorites.append(verb)
            st.success(f"Added **{verb.capitalize()}** to favorites!")

# Display favorites
if st.session_state.favorites:
    st.write("### Your Favorite Verbs:")
    favorite_verb = st.selectbox("Choose a favorite verb to see its forms:", st.session_state.favorites)
    
    if favorite_verb:
        favorite_verb_forms = verb_dict.get(favorite_verb)
        if favorite_verb_forms:
            st.write(f"### Forms for **{favorite_verb.capitalize()}**")
            st.table({
                "Base Form": [favorite_verb.capitalize()],
                "Past Tense": [favorite_verb_forms['past']],
                "Past Participle": [favorite_verb_forms['participle']],
            })

# Quiz Feature
if st.button("🎲 Quiz Me!"):
    quiz_verb = random.choice(list(verb_dict.keys()))
    st.session_state.quiz_verb = quiz_verb  # Save the quiz verb in session state

# Quiz input section
if 'quiz_verb' in st.session_state:
    st.write(f"What is the past tense and past participle of the verb **{st.session_state.quiz_verb.capitalize()}**?")
    answer_past = st.text_input("Past Tense:")
    answer_participle = st.text_input("Past Participle:")
    
    if st.button("Submit"):
        correct_past = verb_dict[st.session_state.quiz_verb]['past']
        correct_participle = verb_dict[st.session_state.quiz_verb]['participle']
        feedback = []
        
        if answer_past.lower() == correct_past.lower():
            feedback.append("Correct! 🎉")
        else:
            feedback.append(f"Wrong! The correct answer is: {correct_past}.")
        
        if answer_participle.lower() == correct_participle.lower():
            feedback.append("Correct! 🎉")
        else:
            feedback.append(f"Wrong! The correct answer is: {correct_participle}.")
        
        st.write("### Feedback:")
        for message in feedback:
            st.write(message)
        
        # Clear quiz state after submission
        del st.session_state.quiz_verb

# Add footer
st.markdown("---")
st.write("Created with ❤️ using Streamlit")
