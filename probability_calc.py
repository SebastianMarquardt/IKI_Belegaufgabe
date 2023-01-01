import pandas as pd

# TODO functionality


def calculate_all_probability_tables(data: pd.DataFrame, endNode: str):
    #creating a new DataFrame for the propabiblity tables with labelled rows and columns
    propTable = pd.DataFrame(calculate_probability_data(data, endNode),
    index=['PrevDayUpUp', 'PrevDayUpDown', 'PrevDayDownUp', 'PrevDayDownDown'])

    print(propTable.to_string())

    return propTable


def calculate_probability_data(data: pd.DataFrame, endNode: str):

    #labels for columns
    firstColumnName = "up"
    secondColumnName = "down"

    #table used to fill the DataFrame later
    propData = {
        firstColumnName: [0, 0, 0, 0],
        secondColumnName: [0, 0, 0, 0] 
    }

    for ind in range(len(data.index) - 1):
        #if prev day was open up and close up
        if (data['trend_open'][ind] == 'up' and data['trend_close'][ind] == 'up'):
            #check if next day was open up or close up, depending on mode
            if (data[endNode][ind + 1] == 'up'):
                #add 1 to the right point of the prop data
                propData[firstColumnName][0] = propData[firstColumnName][0] + 1
            else:
                propData[secondColumnName][0] = propData[secondColumnName][0] + 1
        if (data['trend_open'][ind] == 'up' and data['trend_close'][ind] == 'down'):
            if (data[endNode][ind + 1] == 'up'):
                propData[firstColumnName][1] = propData[firstColumnName][1] + 1
            else:
                propData[secondColumnName][1] = propData[secondColumnName][1] + 1
        if (data['trend_open'][ind] == 'down' and data['trend_close'][ind] == 'up'):
            if (data[endNode][ind + 1] == 'up'):
                propData[firstColumnName][2] = propData[firstColumnName][2] + 1
            else:
                propData[secondColumnName][2] = propData[secondColumnName][2] + 1
        if (data['trend_open'][ind] == 'down' and data['trend_close'][ind] == 'down'):
            if (data[endNode][ind + 1] == 'up'):
                propData[firstColumnName][3] = propData[firstColumnName][3] + 1
            else:
                propData[secondColumnName][3] = propData[secondColumnName][3] + 1
    
    return propData


def calculate_probability_table_for_col(col):
    # Open: Depends on Previous Open and Previous Close
    # Close: Depends on Previous Close and Current Open
    raise NotImplementedError
