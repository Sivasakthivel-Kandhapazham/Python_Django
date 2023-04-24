import pandas as pd
from itertools import groupby
import generatepdf
import utils

df = pd.read_csv('Property_Data.csv', index_col=0)
df = df.reset_index()


# Define a class to represent each row in the DataFrame
class PropertyData:
    def __init__(self, sno, property_type, location, price, no_of_bedrooms, bathrooms, sq_footage):
        self.sno = sno
        self.property_type = property_type
        self.location = location
        self.price = price
        self.no_of_bedrooms = no_of_bedrooms
        self.bathrooms = bathrooms
        self.sq_footage = sq_footage


# Create a list of class instances
property_data = [PropertyData(row["SNo"], row["Property Type"], row["Location"], row["Price"],
                              row["Number of Bedrooms"], row["Bathrooms"],
                              row["Square Footage"]) for index, row in df.iterrows()]

# sort the data according to grouping
sorted_lo_prop = sorted(property_data, key=lambda x: (x.property_type, x.location))
sorted_location = sorted(property_data, key=lambda x: x.location)
sorted_prop_type = sorted(property_data, key=lambda x: x.property_type)

# group by the data
grouped_location_prop_data = groupby(sorted_lo_prop, key=lambda x: (x.property_type, x.location))
grouped_location_data = groupby(sorted_location, key=lambda x: x.location)
grouped_property_data = groupby(sorted_prop_type, key=lambda x: x.property_type)

# call the methods to get average value
summarize_data_location_prop = utils.grouping_location_prop(grouped_location_prop_data)
summarize_data_location = utils.grouping_location(grouped_location_data)
summarize_data_property_type = utils.grouping_property_type(grouped_property_data)

# generate pdf method
generatepdf.report_generation_pdf(summarize_data_location_prop, summarize_data_location, summarize_data_property_type)
