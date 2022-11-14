arr = [1,2,3,4,5,6,2.3]
def f(arr):
  try:
   setarr = set(arr)
   if len(arr) == len(setarr):
    print("All elements are unical")
   else:
    print("Not Unical")
   if not type(arr) is int:
    raise  ValueError("The list must be int")
  except Exception as exec:
      return exec

  finally: "All value is checked"
print(f(arr))











