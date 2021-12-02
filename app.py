import streamlit as st
import requests
import time
import pandas as pd
import plot

columns = ['result_ht', 'Home_D_start', 'Home_M_start', 'Home_A_start','Away_D_start', 'Away_M_start', 'Away_A_start', 'Home_D_ht', 'Home_M_ht','Home_A_ht', 'Away_D_ht', 'Away_M_ht', 'Away_A_ht', 'Home_D_60','Home_M_60', 'Home_A_60', 'Away_D_60', 'Away_M_60', 'Away_A_60','Home_D_75', 'Home_M_75', 'Home_A_75', 'Away_D_75', 'Away_M_75','Away_A_75', 'Home_D_final', 'Home_M_final', 'Home_A_final','Away_D_final', 'Away_M_final', 'Away_A_final']
Home_D_start = Home_M_start =Home_A_start =Away_D_start =Away_M_start = Away_A_start =Home_D_ht =Home_M_ht =Home_A_ht =Away_D_ht =Away_M_ht =Away_A_ht =Home_D_60 =Home_M_60 =Home_A_60 =Away_D_60 =Away_M_60 =Away_A_60 =Home_D_75 =Home_M_75 =Home_A_75 =Away_D_75 =Away_M_75 =Away_A_75 =Home_D_final =Home_M_final =Home_A_final =Away_D_final =Away_M_final =Away_A_final = 0

st.set_page_config(page_title='Football stats',layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)


with st.container():
    st.title("Bienvenue sur Paul 2.0!")
    st.header("Paul 2.0 est l'alliance parfaite entre la puissance du Machine Learning et la tradition :squid:")

    #################  First section  ###################
    with st.expander('1) Informations pré-match'):
        col1, col2 = st.columns(2)
        with col1:
            st.header('Votre équipe')
            old_rules = st.checkbox('Jouez vous en Premier League ?',
                                    key=1)
            if old_rules:
                new_rules = 'False'
            else:
                new_rules = 'True'
            home_or_away = st.radio("Jouez-vous à domicile ou à l'extérieur ?",
                                    ('Home', 'Away'))
            if home_or_away == "Home":
                agree = st.checkbox(
                    'Avez-vous été promu cette saison ?',
                    key=2)
                if agree:
                    H_standings = 40
                else:
                    H_standings = st.slider('Combien de points avez vous gagné la saison dernière ?', 0, 100, 40)
                H_form = st.select_slider('Quel est votre classement au début du match ?',options=[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1],value=10,
                                key=3)
                with col2:
                    st.header('Votre adversaire')
                    last_season = st.checkbox(
                        'Votre adversaire est-il un promu ?',
                        key=4)
                    if last_season:
                        A_standings = 40
                    else:
                        A_standings = st.slider(
                            'Combien de points votre adversaire a-t-il gagné la saison dernière?', 0, 100, 40, key=5)
                    A_form = st.select_slider(
                        "Quel est son classement au début du match ?",options=[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1],value=10, key=6)
            elif home_or_away == "Away":
                agree = st.checkbox(
                    'Avez-vous été promu cette saison ?',
                    key=98)
                if agree:
                    A_standings = 40
                else:
                    A_standings = st.slider(
                        'Combien de points avez vous gagné la saison dernière ?',
                        0, 100, 40)
                A_form = st.select_slider('Quel est votre classement au début du match ?',options=[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1],value=10, key=7)
                with col2:
                    st.header('Votre adversaire')
                    last_season = st.checkbox(
                        'Votre adversaire est-il un promu ?', key=8)
                    if last_season:
                        H_standings = 40
                    else:
                        H_standings = st.slider(
                            'Combien de points votre adversaire a-t-il gagné la saison dernière?', 0, 100, 40, key=9)
                    H_form = st.select_slider(
                        "Quel est son classement au début du match ?",options=[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1],value=10,key=10)

    #################  Second section  ###################
    with st.expander('2) Informations sur votre organisation tactique'):
        col1, col2 = st.columns(2)
        with col1:
            if home_or_away == "Home":
                Home_D_start = st.slider('Combien de joueurs défensifs avez vous au début du match ?',1,5,4,key=1)
                Home_M_start = st.slider('Combien de milieux avez vous au début du match ?',1,5,3,key=12)
                Home_A_start = st.slider('Combien de joueurs offensifs avez vous au début du match ?',1,5,3,key=13)
                if Home_D_start + Home_M_start + Home_A_start > 10:
                    st.write("Vous ne pouvez pas avoir plus de 10 joueurs de champs !")
                    Home_D_start = Home_M_start = Home_A_start = 2
                own_tactic_changes = st.radio(
                "Avez vous prévu des changements tactiques en cours de match ?",('Non', 'Oui'))


            elif home_or_away == "Away":
                Away_D_start = st.slider('Combien de joueurs défensifs avez vous au début du match ?',1,5,4,key=14)
                Away_M_start = st.slider('Combien de milieux avez vous au début du match ?',1,5,3,key=15)
                Away_A_start = st.slider('Combien de joueurs offensifs avez vous au début du match ?',1,5,3,key=16)
                if Away_D_start + Away_M_start + Away_A_start > 10:
                    st.write("Vous ne pouvez pas avoir plus de 10 joueurs de champs ! ")
                    Away_D_start = Away_M_start = Away_A_start = 2
                own_tactic_changes = st.radio(
                 "Avez vous prévu des changements tactiques en cours de match ?",('Non', 'Oui'))

        with col2:
            if home_or_away == "Home":
                if [Home_D_start, Home_M_start, Home_A_start] == [4,3,3]:
                    x_home, y_home= plot.get_433_home()
                    plot.plot_lineup(x_home, y_home, [], [])
                elif [Home_D_start, Home_M_start, Home_A_start] == [3,4,3]:
                    x_home, y_home = plot.get_343_home()
                    plot.plot_lineup(x_home, y_home, [], [])
                elif [Home_D_start, Home_M_start, Home_A_start] == [4,4,2]:
                    x_home, y_home = plot.get_442_home()
                    plot.plot_lineup(x_home, y_home, [], [])
                elif [Home_D_start, Home_M_start, Home_A_start] == [5,3,2]:
                    x_home, y_home = plot.get_532_home()
                    plot.plot_lineup(x_home, y_home, [], [])
                elif [Home_D_start, Home_M_start, Home_A_start] == [4,2,4]:
                    x_home, y_home = plot.get_424_home()
                    plot.plot_lineup(x_home, y_home, [], [])
                elif [Home_D_start, Home_M_start, Home_A_start] == [3,5,2]:
                    x_home, y_home = plot.get_352_home()
                    plot.plot_lineup(x_home, y_home, [], [])
                elif [Home_D_start, Home_M_start, Home_A_start] == [4,5,1]:
                    x_home, y_home = plot.get_451_home()
                    plot.plot_lineup(x_home, y_home, [], [])
                elif [Home_D_start, Home_M_start, Home_A_start] == [5,4,1]:
                    x_home, y_home = plot.get_541_home()
                    plot.plot_lineup(x_home, y_home, [], [])
                else:
                    x_home, y_home= plot.get_433_home()
                    plot.plot_lineup(x_home, y_home, [], [])
                    st.write('Merci de vérifier votre sélection, il semble que vous avez trop peu ou trop de joueurs sélectionnés.')
                [Home_D_60, Home_M_60, Home_A_60] = [Home_D_75, Home_M_75, Home_A_75] = [Home_D_final, Home_M_final, Home_A_final] = [Home_D_start, Home_M_start, Home_A_start]
            elif home_or_away == "Away":
                if [Away_D_start, Away_M_start, Away_A_start] == [4, 3, 3]:
                    x_away, y_away = plot.get_433_away()
                    plot.plot_lineup(x_away, y_away, [], [])
                elif [Away_D_start, Away_M_start, Away_A_start] == [3, 4, 3]:
                    x_away, y_away = plot.get_343_away()
                    plot.plot_lineup(x_away, y_away, [], [])
                elif [Away_D_start, Away_M_start, Away_A_start] == [4, 4, 2]:
                    x_away, y_away = plot.get_442_away()
                    plot.plot_lineup(x_away, y_away, [], [])
                elif [Away_D_start, Away_M_start, Away_A_start] == [5, 3, 2]:
                    x_away, y_away = plot.get_532_away()
                    plot.plot_lineup(x_away, y_away, [], [])
                elif [Away_D_start, Away_M_start, Away_A_start] == [4, 2, 4]:
                    x_away, y_away = plot.get_424_away()
                    plot.plot_lineup(x_away, y_away, [], [])
                elif [Away_D_start, Away_M_start, Away_A_start] == [3, 5, 2]:
                    x_away, y_away = plot.get_352_away()
                    plot.plot_lineup(x_away, y_away, [], [])
                elif [Away_D_start, Away_M_start, Away_A_start] == [4, 5, 1]:
                    x_away, y_away = plot.get_451_away()
                    plot.plot_lineup(x_away, y_away, [], [])
                elif [Away_D_start, Away_M_start, Away_A_start] == [5, 4, 1]:
                    x_away, y_away = plot.get_541_away()
                    plot.plot_lineup(x_away, y_away, [], [])
                else:
                    x_away, y_away = plot.get_433_away()
                    plot.plot_lineup(x_away, y_away, [], [])
                    st.write(
                        'Please check your lineups, it seems that you selected too much or too few players.'
                    )
                [Away_D_60, Away_M_60, Away_A_60] = [Away_D_75, Away_M_75, Away_A_75] = [Away_D_final, Away_M_final, Away_A_final] = [Away_D_start, Away_M_start, Away_A_start]

    #################  Third section  ###################
    with st.expander("3) Informations sur l'organisation tactique de votre adversaire"):
        col1, col2 = st.columns(2)
        with col1:
            if home_or_away == "Home":
                Away_D_start = st.slider('How many defensive players your opponent starts with ?',1,5,4,key=35)
                Away_M_start = st.slider('How many midfield players your opponent starts with ?',1,5,3,key=36)
                Away_A_start = st.slider('How many offensive players your opponent starts with ?',1,5,3,key=37)
            elif home_or_away == "Away":
                Away_D_start = st.slider('How many defensive players your opponent starts with ?',1,5,4,key=38)
                Away_M_start = st.slider('How many midfield players your opponent starts with ?',1,5,3,key=39)
                Away_A_start = st.slider('How many offensive players your opponent starts with ?',1,5,3,key=40)
            opp_tactic_changes = st.radio(
                "Do you know if your opponent is used to do some tactical changes at some point in the game ?",
                ('No', 'Yes'))


        with col2:
            if home_or_away == "Away":
                if [Home_D_start, Home_M_start, Home_A_start] == [4,3,3]:
                    x_home, y_home= plot.get_433_home()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Home_D_start, Home_M_start, Home_A_start] == [4,4,2]:
                    x_home, y_home = plot.get_442_home()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Home_D_start, Home_M_start, Home_A_start] == [5,3,2]:
                    x_home, y_home = plot.get_532_home()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Home_D_start, Home_M_start, Home_A_start] == [4,2,4]:
                    x_home, y_home = plot.get_424_home()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Home_D_start, Home_M_start, Home_A_start] == [3,5,2]:
                    x_home, y_home = plot.get_352_home()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Home_D_start, Home_M_start, Home_A_start] == [3,4,3]:
                    x_home, y_home = plot.get_343_home()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Home_D_start, Home_M_start, Home_A_start] == [4,5,1]:
                    x_home, y_home = plot.get_451_home()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Home_D_start, Home_M_start, Home_A_start] == [5,4,1]:
                    x_home, y_home = plot.get_541_home()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                else:
                    st.write(
                        'Please check your lineups, it seems that you selected too much or too few players.'
                    )
                [Home_D_60, Home_M_60, Home_A_60] = [Home_D_75, Home_M_75, Home_A_75] = [Home_D_final, Home_M_final, Home_A_final] = [Home_D_start, Home_M_start, Home_A_start]
            elif home_or_away == "Home":
                if [Away_D_start, Away_M_start, Away_A_start] == [4, 3, 3]:
                    x_away, y_away = plot.get_433_away()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Away_D_start, Away_M_start,Away_A_start] == [4, 4, 2]:
                    x_away, y_away = plot.get_442_away()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Away_D_start, Away_M_start,Away_A_start] == [5, 3, 2]:
                    x_away, y_away = plot.get_532_away()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Away_D_start, Away_M_start,Away_A_start] == [4, 2, 4]:
                    x_away, y_away = plot.get_424_away()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Away_D_start, Away_M_start,Away_A_start] == [3, 5, 2]:
                    x_away, y_away = plot.get_352_away()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Away_D_start, Away_M_start,Away_A_start] == [5, 4, 1]:
                    x_away, y_away = plot.get_541_away()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Away_D_start, Away_M_start,Away_A_start] == [4,5, 1]:
                    x_away, y_away = plot.get_451_away()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                elif [Away_D_start, Away_M_start, Away_A_start] == [3,4, 3]:
                    x_away, y_away = plot.get_433_away()
                    plot.plot_lineup(x_home, y_home, x_away, y_away)
                else:
                    st.write(
                        'Please check your lineups, it seems that you selected too much or too few players.'
                    )
                [Away_D_60, Away_M_60, Away_A_60] = [Away_D_75, Away_M_75, Away_A_75] = [Away_D_final, Away_M_final, Away_A_final] = [Away_D_start, Away_M_start, Away_A_start]

    #################  4th section  ###################
    st.header('4) Prédictions sur votre match')
    col1, col2, col3 = st.columns(3)
    with col1:
        if home_or_away == "Home":
            st.write("Quel est le score à la mi-temps ?")
            h_goals_ht = st.slider('Vos buts',0,6,1, key=59)
            a_goals_ht = st.slider('Les buts de votre adversaire',0,6,1, key=60)
            score_ht = f'[{h_goals_ht}, {a_goals_ht}]'
            if h_goals_ht > a_goals_ht:
                result_ht = 'H'
            elif a_goals_ht > h_goals_ht:
                result_ht = 'A'
            else:
                result_ht = 'D'

        elif home_or_away == "Away":
            st.write("Quel est le score à la mi-temps ?")
            a_goals_ht = st.slider('Vos buts', 0, 6, 1, key=68)
            h_goals_ht = st.slider('Les buts de votre adversaire',0,6,1, key=69)
            score_ht = f'[{h_goals_ht}, {a_goals_ht}]'
            if h_goals_ht > a_goals_ht:
                result_ht = 'H'
            elif a_goals_ht > h_goals_ht:
                result_ht = 'A'
            else:
                result_ht = 'D'


    y = [
        result_ht, Home_D_start, Home_M_start, Home_A_start, Away_D_start,
        Away_M_start, Away_A_start, Home_D_ht, Home_M_ht, Home_A_ht, Away_D_ht,
        Away_M_ht, Away_A_ht, Home_D_60, Home_M_60, Home_A_60, Away_D_60,
        Away_M_60, Away_A_60, Home_D_75, Home_M_75, Home_A_75, Away_D_75,
        Away_M_75, Away_A_75, Home_D_final, Home_M_final, Home_A_final,
        Away_D_final, Away_M_final, Away_A_final
    ]
    result_dictionary = dict(zip(columns, y))
    col1, col2 = st.columns(2)
    dict_plot={}
    if (Home_D_start+ Home_M_start+ Home_A_start> 10) or (Away_D_start+
    Away_M_start+ Away_A_start>10) or (Home_D_ht+ Home_M_ht+ Home_A_ht>10) or (Away_D_ht+
    Away_M_ht+ Away_A_ht>10) or (Home_D_60+ Home_M_60+ Home_A_60>10) or (Away_D_60+
    Away_M_60+ Away_A_60>10) or (Home_D_75+ Home_M_75+ Home_A_75>10) or (Away_D_75+
    Away_M_75+ Away_A_75>10) or (Home_D_final+ Home_M_final+ Home_A_final>10) or (Away_D_final+ Away_M_final+ Away_A_final>10):
        st.write('Vous avez sélectionné plus de 10 joueurs !')
    else:
        with col1:
            if st.button('Lancer les prédictions', key=78):
                'Début des calculs...'
                # Add a placeholder
                latest_iteration = st.empty()
                bar = st.progress(0)
                time.sleep(0.3)
                url = 'https://footballstats-psjvb4atra-ew.a.run.app/predict'
                result = requests.get(url=url,
                                    params=result_dictionary).json()['Prediction']
                for i in range(100):
                    # Update the progress bar with each iteration.
                    latest_iteration.text(f'{i+1} % done')
                    bar.progress(i + 1)
                    time.sleep(0.03)
                for key in result:
                    if key == 'Probability the winner is the home team':
                        st.markdown(f"## Victoire domicile: &nbsp; &nbsp; &nbsp; &nbsp;{round(result.get(key))}%")
                    elif key == 'Probability the winner is the away team':
                        st.markdown(f"## Victoire extérieur: &nbsp; &nbsp; &nbsp; {round(result.get(key))}%")
                    elif key == 'Probability the game ends up in a draw':
                        st.markdown(
                            f"## Match nul:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {round(result.get(key))}%"
                        )
                with col2:
                    if own_tactic_changes == 'Non':
                        lineups = [[2, 3, 5], [5, 3, 2], [4, 2, 4], [4, 4, 2],
                                   [4, 3, 3], [4, 5, 1], [5, 4, 1], [3, 4, 3]]
                        if home_or_away == "Home":
                            if [Home_D_start, Home_M_start, Home_A_start] in lineups:
                                lineups.remove([Home_D_start, Home_M_start, Home_A_start])
                            for lineup in lineups:
                                dict_plot[str(lineup)] = []
                                y = [result_ht, Home_D_start, Home_M_start, Home_A_start, Away_D_start,
                                    Away_M_start, Away_A_start, Home_D_ht, Home_M_ht, Home_A_ht, Away_D_ht,
                                    Away_M_ht, Away_A_ht, lineup[0], lineup[1], lineup[2], Away_D_60,
                                    Away_M_60, Away_A_60, lineup[0], lineup[1], lineup[2], Away_D_75,
                                    Away_M_75, Away_A_75, lineup[0], lineup[1], lineup[2],
                                    Away_D_final, Away_M_final, Away_A_final]
                                result_dictionary = dict(zip(columns, y))
                                url = 'https://footballstats-psjvb4atra-ew.a.run.app/predict'
                                addl_result = requests.get(url=url,
                                    params=result_dictionary).json()['Prediction']
                                with st.expander(f'Nos prédictions de victoire pour un changement en {lineup}:'):
                                    for key in addl_result:
                                        if key == 'Probability the winner is the home team':
                                            st.markdown(
                                                f"## Victoire domicile: &nbsp; &nbsp; &nbsp; &nbsp;{round(addl_result.get(key))}%"
                                            )
                                        elif key == 'Probability the winner is the away team':
                                            st.markdown(
                                                f"## Victoire extérieur: &nbsp; &nbsp; &nbsp; {round(addl_result.get(key))}%"
                                            )
                                        elif key == 'Probability the game ends up in a draw':
                                            st.markdown(
                                                f"## Match nul:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {round(addl_result.get(key))}%"
                                            )
                        elif home_or_away == 'Away':
                            if [Away_D_start, Away_M_start, Away_A_start] in lineups:
                                lineups = lineups.remove([Away_D_start, Away_M_start, Away_A_start])
                            for lineup in lineups:
                                dict_plot[str(lineup)]=[]
                                y = [result_ht, Home_D_start, Home_M_start, Home_A_start, Away_D_start,
                                    Away_M_start, Away_A_start, Home_D_ht, Home_M_ht, Home_A_ht, Away_D_ht,
                                    Away_M_ht, Away_A_ht, lineup[0], lineup[1], lineup[2], Away_D_60,
                                    Away_M_60, Away_A_60, lineup[0], lineup[1], lineup[2], Away_D_75,
                                    Away_M_75, Away_A_75, lineup[0], lineup[1], lineup[2],
                                    Away_D_final, Away_M_final, Away_A_final]
                                result_dictionary = dict(zip(columns, y))
                                url = 'https://footballstats-psjvb4atra-ew.a.run.app/predict'
                                addl_result = requests.get(url=url,
                                    params=result_dictionary).json()['Prediction']
                                with st.expander(f'Nos prédictions pour un passage en {lineup}:'):
                                    for key in addl_result:
                                        if key == 'Probability the winner is the home team':
                                            if key == 'Probability the winner is the home team':
                                                st.markdown(
                                                    f"## Victoire domicile: &nbsp; &nbsp; &nbsp; &nbsp;{round(addl_result.get(key))}%"
                                                )
                                            elif key == 'Probability the winner is the away team':
                                                st.markdown(
                                                    f"## Victoire extérieur: &nbsp; &nbsp; &nbsp; {round(addl_result.get(key))}%"
                                                )
                                            elif key == 'Probability the game ends up in a draw':
                                                st.markdown(
                                                    f"## Match nul:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {round(addl_result.get(key))}%"
                                                )
