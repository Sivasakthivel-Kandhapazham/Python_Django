from statistics import mean
import numpy as np

summarize_data_location_prop = []
summarize_data_location = []
summarize_data_property_type = []


def grouping_location_prop(property_grouped_data):
    try:
        for property_location, group in property_grouped_data:
            group = list(group)
            price = [item.price for item in group]
            bathrooms = [item.bathrooms for item in group]
            sq_footage = [item.sq_footage for item in group]
            no_of_bedrooms = [item.no_of_bedrooms for item in group]
            price_mean = mean(price)
            bathrooms_mean = mean(bathrooms)
            sq_footage_mean = mean(sq_footage)
            no_of_bedrooms_mean = mean(no_of_bedrooms)
            summarize_data_location_prop.append(
                {'Property Type': property_location[0], 'Location': property_location[1], 'Price': price_mean,
                 'Bathrooms': bathrooms_mean, 'Sq Footage': sq_footage_mean, 'Bedrooms': no_of_bedrooms_mean})
        return summarize_data_location_prop
    except Exception as ex:
        print(ex)


def grouping_location(location_grouped_data):
    try:
        for property_location, group_lo in location_grouped_data:
            group_lo = list(group_lo)
            price = [item.price for item in group_lo]
            sq_footage = [item.sq_footage for item in group_lo]
            price_mean = mean(price)
            sq_footage_mean = mean(sq_footage)
            summarize_data_location.append(
                {'Location': property_location, 'Price': np.round(price_mean, 2), 'Sq Footage': sq_footage_mean})
        return summarize_data_location
    except Exception as ex:
        print(ex)


def grouping_property_type(property_type_grouped_data):
    try:
        for property_location, group in property_type_grouped_data:
            group = list(group)
            bathrooms = [item.bathrooms for item in group]
            no_of_bedrooms = [item.no_of_bedrooms for item in group]
            bathrooms_mean = mean(bathrooms)
            no_of_bedrooms_mean = mean(no_of_bedrooms)
            summarize_data_property_type.append(
                {'Property Type': property_location, 'Bathrooms': np.round(bathrooms_mean, 2),
                 'Bedrooms': np.round(no_of_bedrooms_mean, 2)})
        return summarize_data_property_type
    except Exception as ex:
        print(ex)

