import plotly.express as px
import pandas as pd

# Load a sample dataset
df = pd.DataFrame({
    "country": ["India", "United States", "China", "Brazil", "Australia"],
    "value": [1, 2, 3, 4, 5]  # Example values, not used for display here
})

# Create a choropleth map
fig = px.choropleth(
    df,
    locations="country",       # Column with country names
    locationmode="country names",  # Match country names
    color="value",             # Column for color coding (optional)
    hover_name="country",      # Column to display on hover
    title="World Map with Hover",
)

# Update layout for better visualization
fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type="equirectangular"  # Set map projection
    ),
)

# Show the map
fig.show()
