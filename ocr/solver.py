from mlpm.solver import Solver
import easyocr

class ocrSolver(Solver):
    def __init__(self, toml_file=None):
        super().__init__(toml_file)
        # Do you Init Work here
        self.reader = easyocr.Reader(['de', 'en'], model_storage_directory="./pretrained")
        self.ready()
    def infer(self, data):
        # if you need to get file uploaded, get the path from input_file_path in data
        # image = load_image(data['input_file_path'])
        result = self.reader.readtext(data['input_file_path'])
        # encode result
        for each_res in result:
            for each_coord in each_res[0]:
                each_coord[0] = each_coord[0].item()
                each_coord[1] = each_coord[1].item()
        return result