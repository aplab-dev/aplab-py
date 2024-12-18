import plotly.graph_objects as go

from aplab.config.styles import CHART_STYLES, TEXT_STYLES


def create_flow_chart(nodes, x_positions=None):
    """Create a flow chart with consistent styling"""
    if x_positions is None:
        x_positions = list(range(len(nodes)))

    fig = go.Figure()

    # Add nodes
    fig.add_trace(go.Scatter(
        x=x_positions,
        y=[0] * len(nodes),
        mode='markers+text',
        marker=dict(
            size=40,
            color=CHART_STYLES['node_colors'][:len(nodes)],
            line=dict(color=CHART_STYLES['border_color'], width=2)
        ),
        text=nodes,
        textposition='middle center',
        textfont=dict(
            size=TEXT_STYLES['body']['size'],
            color=TEXT_STYLES['body']['color'],
            family=TEXT_STYLES['body']['family']
        )
    ))

    # Add arrows
    for i in range(len(nodes)-1):
        fig.add_annotation(
            x=x_positions[i]+0.5,
            y=0,
            ax=x_positions[i],
            ay=0,
            xref='x',
            yref='y',
            axref='x',
            ayref='y',
            text='',
            showarrow=True,
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=2,
            arrowcolor=CHART_STYLES['arrow_color']
        )

    # Update layout
    fig.update_layout(
        showlegend=False,
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[min(x_positions)-0.5, max(x_positions)+0.5]
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-0.5, 0.5]
        ),
        plot_bgcolor=CHART_STYLES['background'],
        paper_bgcolor=CHART_STYLES['background'],
        height=200,
        margin=dict(l=20, r=20, t=20, b=20)
    )

    return fig