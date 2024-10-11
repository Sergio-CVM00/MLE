load_file_in_context("script.py")

try:
  face_image_reshaped
  
  if not face_image_reshaped.shape == (side_length, side_length):
    fail_tests(f"Expected `face_image_reshaped` shape to be ({side_length}, {side_length}).")
  
except NameError:
  fail_tests("Expected `face_image_reshaped` to be defined.")

pass_tests()
