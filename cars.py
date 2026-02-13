class Cars:
    # (class attribute): A list/dictionary that will store all the car instances created.
    all_cars = []
    # (class attribute): An integer that will keep track of the total number of cars.
    total_cars = 0
    
    # initializing instance attributes
    def __init__(self, id_num, make, model, year, mileage, services):
        self.id_num = id_num
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        
    def __repr__(self):
        return f"make: {self.make}, model: {self.model}, year: {self.year}"
        
    @property
    def id_num(self):
        return self._id_num
    
    @id_num.setter
    def id_num(self, id_val):
        if isinstance(id_val, int): 
            self._id_num = id_val
            
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make_val):
        if isinstance(make_val, str):
            self._make = make_val
    
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model_val):
        if isinstance(model_val, str):
            self._model = model_val
            
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year_val):
        if isinstance(year_val, int):
            self._year = year_val
    
    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, mileage_val):
        if isinstance(mileage_val, int):
            self._mileage = mileage_val
            
    @property
    def services(self):
        return self._services

    @services.setter
    def services(self, services_val):
        if isinstance(services_val, str):
            self._services = services_val

    