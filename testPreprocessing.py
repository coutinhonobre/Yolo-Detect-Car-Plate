from preprocessing import file_paths
root_dir = "datasets/car-number-plate/"
valid_formats = [".jpg", ".jpeg", ".png", ".txt"]
image_paths = file_paths(root_dir + "images", valid_formats[:3])
print(image_paths)

label_paths = file_paths(root_dir + "labels", valid_formats[-1])
print(label_paths)
