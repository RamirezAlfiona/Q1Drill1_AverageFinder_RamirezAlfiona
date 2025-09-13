from pyscript import document, display



def average_finder(e): #we put e for event handling
    num1= float(document.getElementById("input1").value)
    num2= float(document.getElementById("input2").value)

    average = (num1 + num2) / divisor
    message = "✅YAY!! You Passed!!" if average >= 75 else "❌Aww.. You failed" #displays the passed and failed message
    display(f"Average: {average:.2f} - {message}", target="output")


divisor = 2 #divisor for getting the average of the two scores
