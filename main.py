
print("=== Fiverr Gig Workflow System ===")
print("Select a gig to process:")
print("1. Code Explanation")
print("2. Python to EXE Conversion")
print("3. Debugging & Fixing")
choice = input("Enter number: ")

if choice == "1":
    from gigs import gig1
    gig1.run()
elif choice == "2":
    from gigs import gig2
    gig2.run()
elif choice == "3":
    from gigs import gig3
    gig3.run()
else:
    print("Invalid choice.")
