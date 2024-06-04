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
        y=alt.Y('Speech Time (Days):Q', axis=alt.Axis(title='Speech Time (days)', labelColor='black', titleColor='black')),
        color=alt.Color('party:N', scale=alt.Scale(range=colors))#, legend=None
    )


    # Area chart
    area_chart = base_chart.mark_area(opacity=0.6, interpolate='cardinal').encode(
        y='Speech Time (Days):Q',tooltip=[
            alt.Tooltip('month_number:N', title='Month'),
            alt.Tooltip('Speech Time (Days):Q', title='Speech Time (Days)', format='.2f', formatType='number'),
            alt.Tooltip('party:N', title='Party')
        ]
    )


    # # Scatter chart
    # scatter_chart = base_chart.mark_circle(opacity=0.6, size=50).encode(
    #     tooltip=[            alt.Tooltip('month_number:N', title='Month'),
    #                 alt.Tooltip('Speech Time (Days):Q', title='Speech Time (Days)', format='.2f', formatType='number'),
    #                 alt.Tooltip('party:N', title='Party')]
    # )

    final_chart = (area_chart).properties(
        background='transparent', padding={'left': 0, 'right': 40, 'top': 10, 'bottom': 0}
    )


    # Adjust the x-axis grid lines
    final_chart = final_chart.configure_axisX(
        grid=True
    ).configure_axisY(
        grid=True,
        gridColor='black',  # Set the grid line color
        domain=False,       # Hide the domain line on the left side
        tickCount=3         # Set the number of ticks
    )

    # Display the final chart
    return final_chart.configure_axisX(labelAngle=-45)  # Rotate x-axis labels by 45 degrees
