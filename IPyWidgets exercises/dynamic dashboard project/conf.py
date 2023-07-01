config = [
    {
        "type": "VBox",
        "children": [
            {
                "type": "Dropdown",
                        "props": {
                            "description": "Scenario",
                            "values_source": "dropDownOptions"
                            # "value": "Option 1"
                        },
                "id": "dropdown",
                # "handler_func": lambda change, widget_id="dropdown": print(f"{widget_id} value changed: {change['new']}")
            },
            {
                "type": "HBox",
                "children": [
                    {
                        "type": "DatePicker",
                        "props": {
                            "description": "Start Date"
                        },
                        "id": "startDate",
                        # "handler_func": lambda change, widget_id="startDate": print(f"{widget_id} value changed: {change['new']}")
                    },
                    {
                        "type": "intSlider",
                        "props": {
                            "description": "Start Hour",
                            "min": 0,
                            "max": 23,
                            "value": 0
                        },
                        "id": "startHour",
                        # "handler_func": lambda change, widget_id="startHour": print(f"{widget_id} value changed: {change['new']}")
                    },
                    {
                        "type": "intSlider",
                        "props": {
                            "description": "Start Minute",
                            "min": 0,
                            "max": 59,
                            "value": 0
                        },
                        "id": "startMin",
                        # "handler_func": lambda change, widget_id="startMin": print(f"{widget_id} value changed: {change['new']}")
                    },
                    {
                        "type": "intSlider",
                        "props": {
                            "description": "Start Second",
                            "min": 0,
                            "max": 59,
                            "value": 0
                        },
                        "id": "startSec",
                        # "handler_func": lambda change, widget_id="slider1": print(f"{widget_id} value changed: {change['new']}")
                    }
                ]
            },
            {
                "type": "HBox",
                "children": [
                    {
                        "type": "DatePicker",
                        "props": {
                            "description": "End Date"
                        },
                        "id": "endDate",
                        # "handler_func": lambda change, widget_id="endDate": print(f"{widget_id} value changed: {change['new']}")
                    },
                    {
                        "type": "intSlider",
                        "props": {
                            "description": "End Hour",
                            "min": 0,
                            "max": 23,
                            "value": 0
                        },
                        "id": "endHour",
                        # "handler_func": lambda change, widget_id="endHour": print(f"{widget_id} value changed: {change['new']}")
                    },
                    {
                        "type": "intSlider",
                        "props": {
                            "description": "End Minute",
                            "min": 0,
                            "max": 59,
                            "value": 0
                        },
                        "id": "endMin",
                        # "handler_func": lambda change, widget_id="endMin": print(f"{widget_id} value changed: {change['new']}")
                    },
                    {
                        "type": "intSlider",
                        "props": {
                            "description": "End Second",
                            "min": 0,
                            "max": 59,
                            "value": 0
                        },
                        "id": "endSec",
                        # "handler_func": lambda change, widget_id="endSec": print(f"{widget_id} value changed: {change['new']}")
                    }
                ]
            },
            {
                "type": "Textarea",
                "props": {
                    "description": "Enter Query",
                    "value" : str({"uitid":"TBD", "parsingTime" : "timeRange"})
                },
                "id": "freeTextQuery"
                # "handler_func": lambda btn: print("Button clicked!")
            },
            {
                "type": "Button",
                "props": {
                    "description": "Submit"
                },
                # "handler_func": lambda btn: print("Button clicked!")
            }
        ]
    }
]

# Define the function to execute with the changed widget values

def getDateTime(valDate,valH,valM,valS):
        from datetime import datetime
        if valDate != None:
            dateTimeFormat = datetime(valDate.year, valDate.month, valDate.day,
                            valH, valM, valS)
            return dateTimeFormat
        else:
            print('No date was set yet and NOW was returned as default')
            return datetime.now()

def execute_function(values):
    startDateTime = getDateTime(values['startDate'], values['startHour'], values['startMin'], values['startSec'])
    endDateTime = getDateTime(values['endDate'], values['endHour'], values['endMin'], values['endSec'])
    if values['startDate'] and values['endDate']:
        datesRange = {"$gte":startDateTime, "$lte":endDateTime}
    elif values['startDate']:
        datesRange = {"$gte":startDateTime}
    elif values['endDate']:
        datesRange = {"$lte":endDateTime}
    else:
        datesRange = {}
    # print(f"start date is:{startDateTime}")
    query = values['freeTextQuery'].replace('timeRange', str(datesRange))
    print("Executing function with widget values:")
    print(f"initial query: {query}")
    # for widget_id, value in values.items():
    #     print(f"{widget_id}: {value}")