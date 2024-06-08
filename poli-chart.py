import streamlit as st
import pandas as pd
import altair as alt
from streamlit_extras.stylable_container import stylable_container
from functions import line_point_chart, area_chart, bar_chart


@st.experimental_dialog("Seat Composition")
def seat_comp():
    parties = ['Progressive Conservative Party of Ontario', 'New Democratic Party of Ontario','Ontario Liberal Party', 'Independent','Green Party of Ontario'  ]
    members = [80, 28, 9, 5, 2]
    pct_seats = ['65%','22%', '7%', '4%', '1.6%' ]
    party_seats = pd.DataFrame({'Affilitation': parties, 'Members': members, '% of Seats':pct_seats})
    party_seats.set_index('Affilitation', inplace=True)

    st.write(party_seats)

def area_chart_full(d):
    with stylable_container(
           key="container_with_border",
           css_styles="""
               {
                   padding: calc(1em - 1px);
                   background-color: #DCDCDD;
               }
               """,#            border-radius: 0.5rem;
       ):
          with st.container(height=390, border=False):
             st.html("""
             <span style="color:black; font-size:16px; font-weight:bold; padding-right:50px;">
                Political Parties, Contribution in Latest Parliamentary Session
             </span>
             """)
             st.html("""
              <span style="color:black; font-size:12px; padding-right:50px;">
                 Length of speeches in parliament (days), August 2022 to June 2024
              </span>
              """)

             chart = area_chart(d)
             st.altair_chart(chart, use_container_width=True)
    st.html("""<span style="color:black; font-size:12px; font-style:italic;">Source: Hansard Tables, Political Affairs 2024</span>""")
    st.divider()

def bar_chart_full(d, text):
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                padding: calc(1em - 1px);
                background-color: #C5C3C6;
            }
            """,#            border-radius: 0.5rem;
    ):
        with st.container(height=390, border=False):
            st.html(f"""
                <span style="color:black; font-size:24px; font-style:italic; font-weight:bold; line-height:0.1;">
                    {text}
                </span>
            """)
            st.html("""<span style="color:black; font-size:12px; font-style:italic;">Indvidual speech time during session type (hrs)</span>""")
            chart = bar_chart(d[['name', 'Speech Time (Hrs)']])
            st.altair_chart(chart, use_container_width=True)

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

c = st.columns(2)
with c[0]:
    st.subheader('42nd Parliament Ontario Hansard', anchor=False)
    st.caption('August, 2022 to June, 2024')
with c[1]:
    b = st.button('Seat Composition',type='primary')
    if b:
        seat_comp()

# parties = st.multiselect('Party', data.party.unique(), default=data.party.unique())

d = data[data['party'].isin(data.party.unique())]
# Scatter Effect Simulation
# st.write(d.head())

#            border: 1px solid rgba(49, 51, 63, 0.2);

st.image('header.png')
st.divider()
with st.container():
    st.write("""
    At almost 32 days worth of dialogue, the Ontario parliament holds many keys to understanding our elected officials. For the vast majority of parliamentarians their major role and contribution to democracy will be in the form of votes, questions or answers about government programs/plans,  advocating for the disadvantage or advantage of proposed legislation, liaison with the ministries, and committee votes or reports. Hopefully they also get to help develop ideas during the private party caucus to benefit constituents. And if they are one of the lucky few, they will be drafting laws and managing ministries from the cabinet that makes up the executive government.

    So for most, an important measure for judging their performance is looking at how their dialogue contributes to improving or developing government programs for citizens.

    With 80 of the 124 seats the Progressive Conservative Party of Ontario has spoken the most, with over 16 days worth of speech time in the last 20 months of parliament, accounting for 52% of the words in the sessions Hansard. NDP  speakers account for double the proportion of seats they hold at ~41%, almost 13 days of speech time acting as the official opposition. The Liberals contributed 5.7% to the debate, the Green Party 1.2% and the independents less than 1% of the speeches.
    """)

        #st.altair_chart(final_chart + minor_parties_chart)#
    area_chart_full(d)

    political_groups = ['Cabinet', 'PCP Back-Benchers', "NDP", 'Liberal', 'Independent', "Green Party"]
    tabs = st.tabs(political_groups)

    # for i, tab in enumerate(tabs):
    with tabs[0]:
        st.subheader('Main Orders of Business in Parliament', anchor=False)
        st.write("""The cabinet currently consists of 30 members from the PCP party, as of June 5th, 2024. The data below also includes five members that were at some point in the executive during this session but have since been booted or resigned.""")
        st.caption("""Monte McNaughton (Resigned), Steve Clark(Out of Cabinet), Kaleed Rasheed(Out of Cabinet) , Parm Gill(Resigned), Merrilee Fullerton(Resigned)""")
        name_counts = pd.read_csv("cabinet_speech_time.csv")
        c = st.columns(2)
        with c[0]:
            data = name_counts[name_counts['maintopic'] == 'Question Period']
            data = data.sort_values(by='Speech Time (Hrs)', ascending=False).iloc[:10, :]
            d = data[['name', 'Speech Time (Hrs)']]
            # d = d.set_index('name')
            bar_chart_full(data, 'Question Period')
            st.write("Question Period is designed to provide a forum for Members of Provincial Parliament (MPPs) to question the Premier and Cabinet Ministers about their policies, actions, and decisions. It's a key mechanism for holding the government accountable to the legislature and, by extension, to the public.Question Period is designed to provide a forum for Members of Provincial Parliament (MPPs) to question the Premier and Cabinet Ministers about their policies, actions, and decisions. It's a key mechanism for holding the government accountable to the legislature and, by extension, to the public.")


        with c[1]:
            data = name_counts[name_counts['maintopic'] == 'Orders of the Day']
            data = data.sort_values(by='Speech Time (Hrs)', ascending=False).iloc[:10, :]
            d = data[['name', 'Speech Time (Hrs)']]
            # d = d.set_index('name')
            bar_chart_full(data, 'Orders of the Day')
            st.write('Orders of the Day is a comprehensive look at all the business, bill proposals, that is before the Assembly and its committees on a given day. Not every item of business will be raised, and the Government House Leader chooses the order of business under Government Orders. A Member of Provincial Parliament (MPP) presents a bill to the Legislative Assembly for consideration. It may propose a new law or a change to an existing law.')
