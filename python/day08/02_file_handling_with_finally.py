try:
    f = open("output.txt", "w")
    f.write("Hello, this will be saved in the file!")
    # Simulate error
    raise Exception("Something went wrong while writing!")
except Exception as e:
    print("Caught error:", e)
finally:
    f.close()
    print("File closed (even if error occurred).")
