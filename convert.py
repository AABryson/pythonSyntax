def convert_temp(unit_in, unit_out, temp):
    if unit_in is "c" and unit_out is "f":
        return (temp - 32) * 5/9
    elif unit_in is "f" and unit_out is "c":
        return 5/9 * (temp - 32)
    elif (unit_in not in ["c" or "f"]) or  (unit_out not in ["c" or "f"]):
      return print(f"Invalid unit[{unit_in}]")
  
    elif unit_in is unit_out:
      return temp

  
print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

