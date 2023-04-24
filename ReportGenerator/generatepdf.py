from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch


def report_generation_pdf(report_data_location_prop, report_data_location, report_data_prop):
    try:
        # Set up the PDF document
        doc = SimpleDocTemplate("Property_Report.pdf", pagesize=letter, title="Property Report")
        elements = []

        # Define the table headings
        table_data_lo_prop = [
            ['Property Type', 'Location', 'Price', 'Bedrooms', 'Bathrooms', 'Sq Footage']
        ]

        table_data_location = [
            ['Location', 'Price', 'Sq Footage']
        ]

        table_data_prop = [
            ['Property Type', 'Bedrooms', 'Bathrooms']
        ]

        for item in report_data_location_prop:
            row = [item['Property Type'], item['Location'], item['Price'], item['Bedrooms'], item['Bathrooms'],
                   item['Sq Footage']]
            table_data_lo_prop.append(row)

        for item in report_data_location:
            row = [item['Location'], item['Price'], item['Sq Footage']]
            table_data_location.append(row)

        for item in report_data_prop:
            row = [item['Property Type'], item['Bedrooms'], item['Bathrooms']]
            table_data_prop.append(row)

        # Add a heading to the document
        styles = getSampleStyleSheet()
        elements.append(Paragraph('<h6>Summarized Average Property Report</h6>', styles['Heading1']))
        elements.append(Spacer(1, 0.2 * inch))

        # Create the table and add it to the document
        table_lo_prop = Table(table_data_lo_prop)
        table_location = Table(table_data_location)
        table_property = Table(table_data_prop)
        style = TableStyle([
            ('BACKGROUND', (0, 0), (5, 0), colors.green),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('LINEBEFORE', (2, 1), (2, -1), 2, colors.red),
            ('LINEABOVE', (0, 2), (-1, 2), 2, colors.green),
            ('GRID', (0, 1), (-1, -1), 2, colors.black),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ])

        table_lo_prop.setStyle(style)
        table_location.setStyle(style)
        table_property.setStyle(style)

        # Alternate background color
        row_num_lo_prop = len(report_data_location_prop) + 1
        for i in range(1, row_num_lo_prop):
            if i % 2 == 0:
                bc = colors.burlywood
            else:
                bc = colors.beige

            ts = TableStyle(
                [('BACKGROUND', (0, i), (-1, i), bc)]
            )
            table_lo_prop.setStyle(ts)

        row_num_location = len(report_data_location) + 1
        for i in range(1, row_num_location):
            if i % 2 == 0:
                bc = colors.burlywood
            else:
                bc = colors.beige

            ts = TableStyle(
                [('BACKGROUND', (0, i), (-1, i), bc)]
            )
            table_location.setStyle(ts)

        row_num_prop = len(report_data_prop) + 1
        for i in range(1, row_num_prop):
            if i % 2 == 0:
                bc = colors.burlywood
            else:
                bc = colors.beige

            ts = TableStyle(
                [('BACKGROUND', (0, i), (-1, i), bc)]
            )
            table_property.setStyle(ts)

        elements.append(table_lo_prop)
        elements.append(Spacer(1, 0.6*inch))
        elements.append(table_location)
        elements.append(Spacer(1, 0.6*inch))
        elements.append(table_property)

        # Build the document
        doc.build(elements)
    except Exception as ex:
        print(ex)

