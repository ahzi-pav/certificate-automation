import cv2

list_of_names = []

data_file_name = "data.txt"

certificate_template_file_name = "certificate_template.png"

generated_destination = "generated/"

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2
fontColor = (0, 0, 0)
fontThickness = 5
offsetY = -50

def clean_data():
    with open(data_file_name) as file:
        for line in file:  
            list_of_names.append(line.strip())

def generate_certificate():
    for name in list_of_names:
        template = cv2.imread(certificate_template_file_name)
        text_size = cv2.getTextSize(name, font, fontScale, fontThickness)[0]
        textX = (template.shape[1] - text_size[0]) // 2
        textY = (template.shape[0] + text_size[1]) // 2
        cv2.putText(template, name, (textX, textY - offsetY), font, fontScale, fontColor, fontThickness, cv2.LINE_AA)
        cv2.imwrite(f'{generated_destination} Certificate - {name}.png', template)

clean_data()
print(list_of_names)
generate_certificate()


