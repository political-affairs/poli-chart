import altair as alt
import pandas as pd

def line_point_chart1(d):
    # Define colors
    colors = ['green', 'grey', 'red', 'blue', 'orange']#'black',
    colors = ['#6DBF47','grey' , '#E89043', '#3753A3', 'red']#'black',
    # Base chart        x=alt.X('month_number:N', axis=alt.Axis(title='', ticks=True, tickSize=10)),
    base_chart = alt.Chart(d).encode(
        x=alt.X('month_number:N', axis=alt.Axis(title='', ticks=True, tickSize=10, labelColor='black')),
        y=alt.Y('Speech Time (Days):Q', axis=alt.Axis(title='Speech Time (days)', labelColor='black', titleColor='black')),
        color=alt.Color('party:N', scale=alt.Scale(range=colors), legend=None)
    )
    # Party labels at the end of the line
    text_chart = base_chart.mark_text(
        align='left',
        baseline='middle',
        dx=10,
        fontSize=14
    ).encode(
        text='party:N'
    ).transform_filter(
        alt.datum['month_number'] == max(d['month_number'])
    )

    # Scatter chart
    scatter_chart = base_chart.mark_circle(opacity=0.6, size=50).encode(
        tooltip=['month_number', 'Speech Time (Days)', 'party']
    )
    # Cardinal line chart
    line_chart = base_chart.mark_line(size=4, interpolate='cardinal', opacity=0.9).encode(
        y='Speech Time (Days):Q'
    )

    # Combine scatter chart and line chart
    final_chart = (scatter_chart + line_chart + text_chart).properties(
        background='transparent', padding={'left': 0, 'right': 40, 'top': 10, 'bottom': 0}

    )
    # Adjust the y-axis grid lines
    final_chart = final_chart.configure_axisX(
        grid=True,
    )

    #.configure_axisY(
    #    tickCount=alt.TickCount({"interval": 2})
    #)
    # Display the final chart
    return final_chart.configure_axisX(labelAngle=-45)# # Rotate x-axis labels by 45 degrees


def line_point_chart(d):
    # Define colors
    colors = ['#3753A3',  '#6DBF47', 'grey', 'red', '#E89043']#

    # Base chart
    base_chart = alt.Chart(d).encode(
        x=alt.X('month_number:N', axis=alt.Axis(title='Months of Parliament Session', titleColor='black', ticks=True, tickSize=10, labelColor='black')),
        y=alt.Y('Speech Time (Days):Q', axis=alt.Axis(title='Speech Time (days)', labelColor='black', titleColor='black')),
        color=alt.Color('party:N', scale=alt.Scale(range=colors), legend=None)
    )

    # Party labels at the end of the line
    text_chart = base_chart.mark_text(
        align='left',
        baseline='middle',
        dx=10,
        fontSize=14
    ).encode(
        text='party:N'
    ).transform_filter(
        alt.datum['month_number'] == max(d['month_number'])
    )


    # Cardinal line chart
    line_chart = base_chart.mark_line(size=4, interpolate='cardinal', opacity=0.95).encode(
        y='Speech Time (Days):Q'
    )

    # Combine scatter chart and line chart
    final_chart = (scatter_chart + line_chart + text_chart).properties(
        background='transparent', padding={'left': 0, 'right': 40, 'top': 10, 'bottom': 0}
    )

    # Adjust the x-axis grid lines
    final_chart = final_chart.configure_axisX(
        grid=True
    ).configure_axisY(
        grid=True,
        gridColor='black',  # Set the grid line color
        #gridDash=[1, 5],   # Optional: Customize the grid line style
        domain=False,      # Hide the domain line on the left side
        #orient='right',
        tickCount=3     # Move the y-axis to the right side
    )

    # Display the final chart
    return final_chart.configure_axisX(labelAngle=-1)  # Rotate x-axis labels by 45 degrees


def area_chart(d):
    d = d[d['party'] !='0']
    # Define colors
    colors = ['#6DBF47', 'grey', 'red', '#E89043', '#3753A3']

    # Base chart
    base_chart = alt.Chart(d).encode(
        x=alt.X('month_number:N', axis=alt.Axis(title='Months of Parliament Session', titleColor='black', ticks=True, tickSize=10, labelColor='black')),
        y=alt.Y('Speech Time (Days):Q', axis=alt.Axis(title='', labelColor='black', titleColor='black')),
        color=alt.Color('party:N', scale=alt.Scale(range=colors), legend=alt.Legend(labelColor='black',titleColor='black', orient='top'))
    )#Speech Time (days)

    # Area chart
    area_chart = base_chart.mark_area(opacity=0.6, interpolate='cardinal').encode(
        y=alt.Y('Speech Time (Days):Q', axis=alt.Axis(title='', labelColor='black')),tooltip=[
            alt.Tooltip('month_number:N', title='Month'),
            alt.Tooltip('Speech Time (Days):Q', title='', format='.2f', formatType='number'),
            alt.Tooltip('party:N', title='Party')
        ]
    )#Speech Time (Days)

    final_chart = area_chart.properties(
        background='transparent',
        padding={'left': 0, 'right': 20, 'top': 0, 'bottom': 0},
        height=300  # Reduce height, adjust as needed
    )


    # Adjust the x-axis grid lines
    final_chart = final_chart.configure_axisX(
        grid=True
    ).configure_axisY(
        grid=True,
        gridColor='black',  # Set the grid line color
        domain=False,       # Hide the domain line on the left side
        tickCount=3         # Set the number of ticks
    ).interactive(False)
    final_chart = final_chart.configure_axisX(labelAngle=-45)

    # Display the final chart
    return final_chart.interactive(False)    # Rotate x-axis labels by 45 degrees


def bar_chart1(data):

    # Create the bar chart
    bar_chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('name:N', axis=alt.Axis(title='Name', titleColor='black', labelAngle=-45, labelColor='black')),
        y=alt.Y('Speech Time (Hrs):Q', axis=alt.Axis(title='Speech Time (Hrs)', titleColor='black')),
        color=alt.Color('name:N', legend=None)
    ).properties(
        background='transparent',
        padding={'left': 10, 'right': 30, 'top': 30, 'bottom': 40},
        width=300,
        height=400
    )

    # Configure axis
    bar_chart = bar_chart.configure_axis(
        labelColor='black',
        titleColor='black',
        grid=True,
        domain=False,
        tickCount=5
    )

    # Display the final chart
    return bar_chart


def bar_chart(data):
    # Sort the data by 'Speech Time (Hrs)' in descending order
    data = data.sort_values(by='Speech Time (Hrs)', ascending=False).iloc[:10, :]
    colors = ['#47494C']*10
    color_mapping = {name: colors[i % len(colors)] for i, name in enumerate(data['name'])}

    # Create the bar chart
    bar_chart = alt.Chart(data).mark_bar(color='#47494C').encode(
        x=alt.X('name:N',
                axis=alt.Axis(title=None, labels=True),
                sort=alt.EncodingSortField(field='Speech Time (Hrs)', order='descending')  # Sort x-axis by y value
               ),
        y=alt.Y('Speech Time (Hrs):Q', axis=alt.Axis(title='', titleColor='black'),scale=alt.Scale(domain=[0, 12])),
        color=alt.Color('name:N', legend=None, scale=alt.Scale(domain=list(color_mapping.keys()), range=list(color_mapping.values()))  # Set hex colors
), tooltip=[alt.Tooltip('Speech Time (Hrs):Q', format='.1f'), alt.Tooltip('name:N', title='MPP')])

    # Combine the bar chart and text labels
    final_chart = bar_chart.properties( background='transparent', padding={'left': 0, 'right': 30, 'top': 0, 'bottom': 0},
        width=300,
        height=300  # Reduce height as required
    )

    # Configure axis
    final_chart = final_chart.configure_axis(labelColor='black', titleColor='black', grid=True, domain=False, tickCount=5 )

    # Display the final chart
    return final_chart
