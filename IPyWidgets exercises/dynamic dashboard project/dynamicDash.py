import ipywidgets as widgets
from IPython.display import display

class DynamicDashboard:
    def __init__(self, config, execute_func=None, dropDownOptions=None):
        self.config = config
        self.widgets = {}
        self.execute_func = execute_func
        self.dropDownOptions = dropDownOptions
        
    def build_widget(self, doc):
        doc_type = doc.get('type')
        
        # If the document is a container (HBox or VBox)
        if doc_type == 'HBox' or doc_type == 'VBox':
            children = []
            for child_doc in doc.get('children', []):
                child_widget = self.build_widget(child_doc)
                children.append(child_widget)
            
            if doc_type == 'HBox':
                widget = widgets.HBox(children)
            else:
                widget = widgets.VBox(children)
                
        # If the document is a widget
        else:
            widget_type = doc.get('type')
            widget_props = doc.get('props', {})
            
            if widget_type == 'Slider':
                widget = widgets.FloatSlider(**widget_props)
            elif widget_type == 'intSlider':
                widget = widgets.IntSlider(**widget_props)
            elif widget_type == 'DatePicker':
                widget = widgets.DatePicker(**widget_props)
            elif widget_type == 'Text':
                widget = widgets.Text(**widget_props)
            elif widget_type == 'Textarea':
                widget = widgets.Textarea(**widget_props)
            elif widget_type == 'Dropdown':
                # If values are provided directly in the config
                if 'values' in widget_props:
                    widget = widgets.Dropdown(**widget_props)
                # If values should be fetched dynamically from an external list
                elif 'values_source' in widget_props:
                    values_source = widget_props.pop('values_source')
                    values = self.fetch_values(values_source)
                    widget = widgets.Dropdown(options=values, **widget_props)
            elif widget_type == 'Button':
                widget = widgets.Button(**widget_props)
                widget.on_click(self.execute_handler)
            # Add more widget types as needed
            
            # Attach handler function if provided
            handler_func = doc.get('handler_func')
            if handler_func:
                widget.observe(handler_func, 'value')
                
        # Save the widget in the dictionary for reference
        widget_id = doc.get('id')
        if widget_id:
            self.widgets[widget_id] = widget
            
        return widget
    
    def build_dashboard(self):
        dashboard = []
        for doc in self.config:
            widget = self.build_widget(doc)
            dashboard.append(widget)
            
        return dashboard
    
    def display_dashboard(self):
        dashboard = self.build_dashboard()
        display(*dashboard)
        
    def execute_handler(self, button):
        if self.execute_func:
            values = {}
            for widget_id, widget in self.widgets.items():
                values[widget_id] = widget.value
            self.execute_func(values)
            
    def fetch_values(self, values_source):
        # Implement your logic to fetch values dynamically from an external list
        # Return the fetched values as a list
        # For demonstration purposes, a sample static implementation is provided here:
        if values_source == 'sample':
            return ['Option 1', 'Option 2', 'Option 3']
        else:
            return self.dropDownOptions


if __name__ == "__main__":
    pass