def main():
    input_strings = ['1', '5', '28', '131', '3']
    # filter out nums bigger than 3
    output_intergers = [int(num) for num in input_strings if len(num) < 3]
    print(output_intergers)

if __name__ == "__main__":
    main()