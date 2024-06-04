import streamlit as st
import pandas as pd
import altair as alt
from streamlit_extras.stylable_container import stylable_container
from functions import line_point_chart, area_chart


@st.experimental_dialog("Seat Composition")
def seat_comp():
    parties = ['Progressive Conservative Party of Ontario', 'New Democratic Party of Ontario','Ontario Liberal Party', 'Independent','Green Party of Ontario'  ]
    members = [80, 28, 9, 5, 2]
    pct_seats = ['65%','22%', '7%', '4%', '1.6%' ]
    party_seats = pd.DataFrame({'Affilitation': parties, 'Members': members, '% of Seats':pct_seats})
    party_seats.set_index('Affilitation', inplace=True)

    st.write(party_seats)


def quarter_year_key(qy):
    quarter, year = qy.split('-')
    quarter_num = int(quarter[1])  # Extract the numeric part of the quarter
    year_num = int(year)
    return (year_num, quarter_num)


@st.cache_data
def load_data():
    # Sample Data (Replace with your actual DataFrame)
    df = pd.read_csv('party_contribution_dates.csv')
    df['Speech Time (Days)'] = df['speech_time'].apply(lambda x: x/24)

    # Create a new column with the sort key
    # df['sort_key'] = df['quarter-year'].apply(quarter_year_key)
    # df['party'] = df['party'].apply(lambda x: 'PCP Backbenchers' if x=='PCP' else x)
    # Sort the dataframe by the sort key
    # df = df.sort_values(by='sort_key')

    return df

data = load_data()
st.logo('logo.png')

# Streamlit App
st.title('Fresh Off the Podium', anchor=False)
# st.subheader("Recent debates in Ontario parliament", anchor=False)
# st.divider()
st.subheader('42nd Parliament Ontario Hansard', anchor=False)
st.caption('August, 2022 to June, 2024')
b = st.button('Seat Composition',type='primary')
if b:
    seat_comp()

# parties = st.multiselect('Party', data.party.unique(), default=data.party.unique())

d = data[data['party'].isin(data.party.unique())]
# Scatter Effect Simulation
# st.write(d.head())

#            border: 1px solid rgba(49, 51, 63, 0.2);


with stylable_container(
    key="container_with_border",
    css_styles="""
        {
            padding: calc(1em - 1px);
            background-color: #DCDCDD;
        }
        """,#            border-radius: 0.5rem;
):

        st.html("""<span style="color:black; font-size:24px; font-style:italic; font-weight:bold;"> Political Parties, Contribution in Latest Parliamentary Session</span>""")
        st.caption('Speech time in parliament starting in August 2022 to June 2024')
        # chart = line_point_chart(d)
        chart = area_chart(d)
        st.altair_chart(chart, use_container_width=True)
        st.html("""<span style="color:black; font-size:12px; font-style:italic;">Source: Hansard Tables, Political Affairs 2024</span>""")



st.divider()
    #st.altair_chart(final_chart + minor_parties_chart)#



st.write("""
At almost 32 days worth of dialogue, the Ontario parliament holds many keys to understanding our elected officials. For the vast majority of parliamentarians their major role and contribution to democracy will be in the form of votes, questions or answers about government programs/plans,  advocating for the disadvantage or advantage of proposed legislation, liaison with the ministries, and committee votes or reports. Hopefully they also get to help develop ideas during the private party caucus to benefit constituents. And if they are one of the lucky few, they will be drafting laws and managing ministries from the cabinet that makes up the executive government.

So for most, an important measure for judging their performance is looking at how their dialogue contributes to improving or developing government programs for citizens.

With 80 of the 124 seats the Progressive Conservative Party of Ontario has spoken the most, with over 16 days worth of speech time in the last 20 months of parliament, accounting for 52% of the words in the sessions Hansard. NDP  speakers account for double the proportion of seats they hold at ~41%, almost 13 days of speech time acting as the official opposition. The Liberals contributed 5.7% to the debate, the Green Party 1.2% and the independents less than 1% of the speeches.
""")
