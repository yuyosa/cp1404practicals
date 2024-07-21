class Project:
    def __init__(self,name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start = start_date
        self.priority = priority
        self.cost = cost_estimate
        self.completion = completion_percentage


#s

    def __repr__(self):
        start_date_str = self.start.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_date_str}, priority {self.priority}, "
                f"estimate: ${self.cost:.2f}, completion: {self.completion}%")