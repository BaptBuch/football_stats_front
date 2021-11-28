import streamlit as st
import requests
import time

columns = [
    'result_ht', 'Home_D_start', 'Home_M_start', 'Home_A_start',
    'Away_D_start', 'Away_M_start', 'Away_A_start', 'Home_D_ht', 'Home_M_ht',
    'Home_A_ht', 'Away_D_ht', 'Away_M_ht', 'Away_A_ht', 'Home_D_60',
    'Home_M_60', 'Home_A_60', 'Away_D_60', 'Away_M_60', 'Away_A_60',
    'Home_D_75', 'Home_M_75', 'Home_A_75', 'Away_D_75', 'Away_M_75',
    'Away_A_75', 'Home_D_final', 'Home_M_final', 'Home_A_final',
    'Away_D_final', 'Away_M_final', 'Away_A_final'
]
Home_D_start = Home_M_start =Home_A_start =Away_D_start =Away_M_start = Away_A_start =Home_D_ht =Home_M_ht =Home_A_ht =Away_D_ht =Away_M_ht =Away_A_ht =Home_D_60 =Home_M_60 =Home_A_60 =Away_D_60 =Away_M_60 =Away_A_60 =Home_D_75 =Home_M_75 =Home_A_75 =Away_D_75 =Away_M_75 =Away_A_75 =Home_D_final =Home_M_final =Home_A_final =Away_D_final =Away_M_final =Away_A_final = 0

st.set_page_config(layout="wide")

# def get_league_seasons():
#     st.write('You selected:', option_profil)
#     col1, col2 = st.columns([1,1])
#     with col1:
#         options = st.multiselect('Select a league',['Ligue 1', 'Premier league', 'Championship', 'Liga', 'Bundesliga', 'Serie A', 'Eredevise'])
#         st.write('You selected:', ", ".join(options))

#         if 'Ligue 1' in options:
#             st.image("https://seeklogo.com/images/L/ligue-1-uber-eats-logo-E440240623-seeklogo.com.png",width=100)
#         if 'Premier league' in options:
#             st.image("https://seeklogo.com/images/P/premier-league-logo-B2889F3974-seeklogo.com.png",width=100)
#         if 'Championship' in options:
#             st.image("https://seeklogo.com/images/S/sky-bet-championship-logo-C4F6910987-seeklogo.com.png",width=100)
#         if 'Liga' in options:
#             st.image("https://seeklogo.com/images/L/la-liga-logo-0530344B7E-seeklogo.com.png",width=100)
#         if 'Bundesliga' in options:
#             st.image("https://seeklogo.com/images/B/bundesliga-logo-CA4C5CF312-seeklogo.com.png",width=100)
#         if 'Serie A' in options:
#             st.image("https://seeklogo.com/images/S/serie-a-logo-59D3C46AE5-seeklogo.com.png",width=100)
#         if 'Eredevise' in options:
#             st.image("https://seeklogo.com/images/E/eredivisie-logo-24C3DB32E5-seeklogo.com.png",width=100)
#         # se:
#         #     st.write('◀️')
#     with col2:
#         saison = st.radio('Select a saison', ('2015/2016', '2016/2017', '2017/2018', '2018/2019', '2019/2020', '2020/2021'))
#     ######################## MENU DEROULANT ############################

#     @st.cache

#     def get_select_box_data():

#         return pd.DataFrame({
#             'stats': ["Nombre de remplacant","Minutes jouées / remplacants", "Nombre de blessure", "Retournement de situation", "..." ],
#             })

#     df = get_select_box_data()

#     stats = st.selectbox('Select une stat', df['stats'])

# def get_predictions():
st.markdown("""
## Welcome !

### Football_stats is not only about stats, but also preds
We'll **try** to help you build the best tactics for your next games.
We are working on Machine Learning models build to predict the best possible decisions on substitutions managements for second half of football games.
""")

#################  First section  ###################
st.header('1) Pre-game informations')
col1, col2 = st.columns(2)
with col1:
    st.header('Tell us more about you...')
    old_rules = st.checkbox('Are you playing in the english Premier League ?',
                            key=100)
    if old_rules:
        new_rules = 'False'
        st.write('New rules : False')
    else:
        new_rules = 'True'
    home_or_away = st.radio("Will you be playing at home or away ?",
                            ('Home', 'Away'))
    if home_or_away == "Home":
        agree = st.checkbox(
            'Have you been promoted this year to your current league ?',
            key=99)
        if agree:
            H_standings = 45
            st.write('Promoted : true')
        else:
            H_standings = st.slider('How many points did you get last season?', 0, 100, 45)
        H_form = st.slider('What is your position at the start of the game ?',0,20,10,
                        key=38)
        with col2:
            st.header('...and your opponent')
            last_season = st.checkbox(
                'Has your opponent been promoted this year to your current league ?',
                key=919)
            if last_season:
                A_standings = 45
                st.write('Promoted : true')
            else:
                A_standings = st.slider(
                    'How many points did your opponent get last season ?', 0, 100, 25, key=39)
            A_form = st.slider(
                "What is your opponent's position at the start of the game ?",0,20,10, key=40)
    elif home_or_away == "Away":
        agree = st.checkbox(
            'Have you been promoted this year to your current league ?',
            key=98)
        if agree:
            A_standings = 45
            st.write('Promoted : true')
        else:
            A_standings = st.slider('How many points did you get last season?', 0, 100, 45)
        A_form = st.slider('What is your position at the start of the game ?',0,20,10, key=41)
        with col2:
            st.header('...and your opponent')
            last_season = st.checkbox(
                'Has your opponent been promoted this year to your current league ?',
                key=919)
            if last_season:
                H_standings = 45
                st.write('Promoted : true')
            else:
                H_standings = st.slider(
                    'How many points did your opponent get last season ?', 0, 100, 25, key=42)
            H_form = st.slider(
                "What is your opponent's position at the start of the game ?",0,20,10,key=43)

st.header('2) Information about your tactic')
col1, col2 = st.columns(2)
with col1:
    if home_or_away == "Home":
        Home_D_start = st.slider('How many defensive players do you have ?',1,6,2,key=4)
        Home_M_start = st.slider('How many midfield players do you have ?',1,6,2,key=5)
        Home_A_start = st.slider('How many offensive players do you have ?',1,6,2,key=6)
        if Home_D_start + Home_M_start + Home_A_start > 10:
            st.write("You can't choose more than 10 field players ! ")
            Home_D_start = Home_M_start = Home_A_start = 2

    elif home_or_away == "Away":
        Away_D_start = st.slider('How many defensive players do you have ?',1,6,2,key=7)
        Away_M_start = st.slider('How many midfield players do you have ?',1,6,2,key=8)
        Away_A_start = st.slider('How many offensive players do you have ?',1,6,2,key=9)
        if Away_D_start + Away_M_start + Away_A_start > 10:
            st.write("You can't choose more than 10 field players ! ")
            Away_D_start = Away_M_start = Away_A_start = 2
with col2:
    tactic_changes = st.radio(
        "Have you planned to change your lineups at some point in the game ?",('No', 'Yes'))
    if tactic_changes == 'Yes':
        if home_or_away == "Home":
            with st.expander("First step: 60'"):
                st.write("What could be your lineup at 60'? i.e. do you plan to do any changes between 45' and 60'")
                Home_D_60 = st.slider('How many defensive players ?',1,6,2,key=1110)
                Home_M_60 = st.slider('How many midfield players ?',1,6,2,key=1111)
                Home_A_60 = st.slider('How many offensive players ?',1,6,2,key=1112)
            with st.expander("Second step: 75'"):
                st.write("What could be your lineup at 75'? i.e. do you plan to do any changes between 60' and 75'")
                Home_D_75 = st.slider('How many defensive players ?',1,6,2,key=1113)
                Home_M_75 = st.slider('How many midfield players ?',1,6,2,key=1114)
                Home_A_75 = st.slider('How many offensive players ?',1,6,2,key=1115)
            with st.expander("Final step: 90'"):
                st.write("What could be your lineup at the end of the game?  i.e. do you plan to do any changes after the 75'")
                Home_D_final = st.slider('How many defensive players ?',1,6,2,key=116)
                Home_M_final = st.slider('How many midfield players ?',1,6,2,key=117)
                Home_A_final = st.slider('How many offensive players ?',1,6,2,key=118)

        if home_or_away == "Away":
            with st.expander("First step: 60'"):
                st.write("What could be your lineup at 60'? i.e. do you plan to do any changes between 45' and 60'")
                Away_D_60 = st.slider('How many defensive players ?',1,6,2,key=119)
                Away_M_60 = st.slider('How many midfield players ?',1,6,2,key=120)
                Away_A_60 = st.slider('How many offensive players ?',1,6,2,key=121)
            with st.expander("Second step: 75'"):
                st.write("What could be your lineup at 75'? i.e. do you plan to do any changes between 60' and 75'")
                Away_D_75 = st.slider('How many defensive players ?',1,6,2,key=122)
                Away_M_75 = st.slider('How many midfield players ?',1,6,2,key=123)
                Away_A_75 = st.slider('How many offensive players ?',1,6,2,key=124)
            with st.expander("Final step: 90'"):
                st.write("What could be your lineup at the end of the game?  i.e. do you plan to do any changes after the 75'")
                Away_D_final = st.slider('How many defensive players ?',1,6,2,key=125)
                Away_M_final = st.slider('How many midfield players ?',1,6,2,key=126)
                Away_A_final = st.slider('How many offensive players ?',1,6,2,key=127)

    else:
        if home_or_away == "Home":
            Home_D_60, Home_M_60, Home_A_60 = Home_D_75, Home_M_75, Home_A_75 = Home_D_final, Home_M_final, Home_A_final = Home_D_start, Home_M_start, Home_A_start
        elif home_or_away == "Away":
            Away_D_60, Away_M_60, Away_A_60 = Away_D_75, Away_M_75, Away_A_75 = Away_D_final, Away_M_final, Away_A_final = Away_D_start, Away_M_start, Away_A_start

st.header('3) Information about your opponent')
with st.expander('Click to open/close this section'):
    col1, col2 = st.columns(2)
    with col1:
        st.header('3) Information about your opponent')
        if home_or_away == "Home":
            Away_D_start = st.slider('How many defensive players your opponent starts with ?',1,6,2,key=28)
            Away_M_start = st.slider('How many midfield players your opponent starts with ?',1,6,2,key=29)
            Away_A_start = st.slider('How many offensive players your opponent starts with ?',1,6,2,key=30)
        elif home_or_away == "Away":
            Away_D_start = st.slider('How many defensive players your opponent starts with ?',1,6,2,key=33)
            Away_M_start = st.slider('How many midfield players your opponent starts with ?',1,6,2,key=34)
            Away_A_start = st.slider('How many offensive players your opponent starts with ?',1,6,2,key=35)

    with col2:
        tactic_changes = st.radio(
            "Do you know if your opponent is used to do some tactical changes at some point in the game ?",
            ('No', 'Yes'))
        if tactic_changes == 'Yes':
            if home_or_away == "Away":
                with st.expander("First step: 60'"):
                    st.write("What could be their lineup at 60'?")
                    Home_D_60 = st.slider('How many defensive players ?',1,6,2,key=10)
                    Home_M_60 = st.slider('How many midfield players ?', 1,6,2,key=11)
                    Home_A_60 = st.slider('How many offensive players ?',1,6,2,key=12)
                with st.expander("Second step: 75'"):
                    st.write("What could be their lineup at 75'?")
                    Home_D_75 = st.slider('How many defensive players ?',1,6,2,key=13)
                    Home_M_75 = st.slider('How many midfield players ?', 1,6,2,key=14)
                    Home_A_75 = st.slider('How many offensive players ?',1,6,2,key=15)
                with st.expander("Final step: 90'"):
                    st.write("What could be their lineup at end time?")
                    Home_D_final = st.slider('How many defensive players ?',1,6,2,key=16)
                    Home_M_final = st.slider('How many midfield players ?',1,6,2,key=17)
                    Home_A_final = st.slider('How many offensive players ?',1,6,2,key=18)
            if home_or_away == "Home":
                with st.expander("First step: 60'"):
                    st.write("What could be their lineup at 60'?")
                    Away_D_60 = st.slider('How many defensive players ?',1,6,2,key=19)
                    Away_M_60 = st.slider('How many midfield players ?', 1,6,2,key=20)
                    Away_A_60 = st.slider('How many offensive players ?',1,6,2,key=21)
                with st.expander("Second step: 75'"):
                    st.write("What could be their lineup at 75'?")
                    Away_D_75 = st.slider('How many defensive players ?',1,6,2,key=22)
                    Away_M_75 = st.slider('How many midfield players ?', 1,6,2,key=23)
                    Away_A_75 = st.slider('How many offensive players ?',1,6,2,key=24)
                with st.expander("Final step: 90'"):
                    st.write("What could be their lineup at end time?")
                    Away_D_final = st.slider('How many defensive players ?',1,6,2,key=25)
                    Away_M_final = st.slider('How many midfield players ?',1,6,2,key=26)
                    Away_A_final = st.slider('How many offensive players ?', 1,6,2,key=27)
        else:
            if home_or_away == "Home":
                Home_D_ht, Home_M_ht, Home_A_ht = Home_D_60, Home_M_60, Home_A_60 = Home_D_75, Home_M_75, Home_A_75 = Home_D_final, Home_M_final, Home_A_final = Home_D_start, Home_M_start, Home_A_start
            elif home_or_away == "Away":
                Away_D_ht, Away_M_ht, Away_A_ht = Away_D_60, Away_M_60, Away_A_60 = Away_D_75, Away_M_75, Away_A_75 = Away_D_final, Away_M_final, Away_A_final = Away_D_start, Away_M_start, Away_A_start

st.header('4) Information about your game')
col1, col2, col3 = st.columns(3)
with col1:
    if home_or_away == "Home":
        st.write("What's the score at half time ?")
        h_goals_ht = st.slider('How many goals did you score ?',0,6,2, key=31)
        a_goals_ht = st.slider('How many goals did your opponent score ?',0,6,2, key=32)
        score_ht = f'[{h_goals_ht}, {a_goals_ht}]'
        if h_goals_ht > a_goals_ht:
            result_ht = 'H'
        elif a_goals_ht > h_goals_ht:
            result_ht = 'A'
        else:
            result_ht = 'D'
        with col2:
            h_ht_changes = st.checkbox('Did you do substitutions before or at half time ?', key=97)
            if h_ht_changes:
                st.write("What's your new lineup'?")
                Home_D_ht = Home_M_ht = Home_A_ht = 0
                Home_D_ht = st.slider('How many defensive players ?',1,6,2, key=44)
                Home_M_ht = st.slider('How many midfield players ?',1,6,2, key=45)
                Home_A_ht = st.slider('How many offensive players ?',1,6,2, key=46)
                if Home_D_ht + Home_M_ht + Home_A_ht > 10:
                    st.write("You can't choose more than 10 field players ! ")
                    Home_D_ht = Home_M_ht = Home_A_ht = 2

        with col3:
            a_ht_changes = st.checkbox(
                'Did your opponent do substitutions before or at half time ?',
                key=96)
            if a_ht_changes:
                st.write("What's the new lineup'?")
                Away_D_ht= Away_M_ht= Away_A_ht = 0
                Away_D_ht = st.slider('How many defensive players ?',1,6,2, key=344)
                Away_M_ht = st.slider('How many midfield players ?',1,6,2, key=345)
                Away_A_ht = st.slider('How many offensive players ?',1,6,2, key=346)
                if Away_D_ht + Away_M_ht + Away_A_ht > 10:
                    st.write("You can't choose more than 10 field players ! ")
                    Away_D_ht = Away_M_ht = Away_A_ht = 2

    elif home_or_away == "Away":
        st.write("What's the score at half time ?")
        a_goals_ht = st.number_input('How many goals did you score ?', key=36)
        h_goals_ht = st.number_input('How many goals did your opponent score ?', key=37)
        score_ht = f'[{h_goals_ht}, {a_goals_ht}]'
        if h_goals_ht > a_goals_ht:
            result_ht = 'H'
        elif a_goals_ht > h_goals_ht:
            result_ht = 'A'
        else:
            result_ht = 'D'
        with col2:
            h_ht_changes = st.checkbox('Did your opponent do substitutions before or at half time ?',
                key=97)
            if h_ht_changes:
                h_d_ht = st.slider('How many defensive players ?',1,6,2, key=44)
                Home_D_ht = h_d_ht
                h_m_ht = st.slider('How many midfield players ?',1,6,2, key=45)
                Home_M_ht = h_m_ht
                h_a_ht = st.slider('How many offensive players ?',1,6,2, key=46)
                Home_A_ht = h_a_ht
                if Home_D_ht + Home_M_ht + Home_A_ht > 10:
                    st.write("You can't choose more than 10 field players ! ")
                    Home_D_ht = Home_M_ht = Home_A_ht = 2
        with col3:
            a_ht_changes = st.checkbox('Did you do substitutions before or at half time ?', key=96)
            if a_ht_changes:
                st.write("What's the new lineup'?")
                Away_D_ht= Away_M_ht= Away_A_ht = 0
                Away_D_ht = st.slider('How many defensive players ?',1,6,2, key=244)
                Away_M_ht = st.slider('How many midfield players ?',1,6,2, key=245)
                Away_A_ht = st.slider('How many offensive players ?',1,6,2, key=246)
                if Away_D_ht + Away_M_ht + Away_A_ht > 10:
                    st.write("You can't choose more than 10 field players ! ")
                    Away_D_ht = Away_M_ht = Away_A_ht = 2

y = [
    result_ht, Home_D_start, Home_M_start, Home_A_start, Away_D_start,
    Away_M_start, Away_A_start, Home_D_ht, Home_M_ht, Home_A_ht, Away_D_ht,
    Away_M_ht, Away_A_ht, Home_D_60, Home_M_60, Home_A_60, Away_D_60,
    Away_M_60, Away_A_60, Home_D_75, Home_M_75, Home_A_75, Away_D_75,
    Away_M_75, Away_A_75, Home_D_final, Home_M_final, Home_A_final,
    Away_D_final, Away_M_final, Away_A_final
]
result_dictionary = dict(zip(columns, y))
with st.expander('All done ?'):
    if st.checkbox('Launch prediction', key=95):
        'Starting the computation...'
        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'{i+1} % done')
            bar.progress(i + 1)
            time.sleep(0.01)
        url = 'https://footballstats-psjvb4atra-ew.a.run.app/predict'
        result = requests.get(url=url, params=result_dictionary).json()['Prediction']
        for key in result:
            st.write(f"{key}: {result.get(key)}")






#######################Sélection du profil###########################

# option_profil = st.selectbox(
#     "Why are you here ?",
#    ('','For the stats !', 'For the predictions !'))

# ######################## BOX lEAGUE SAISON ############################
# if option_profil == 'For the stats !':
#     get_league_seasons()

# ##################### BOX lEAGUE PREDICTIONS #########################
# if option_profil == 'For the predictions !':
#     get_predictions()
