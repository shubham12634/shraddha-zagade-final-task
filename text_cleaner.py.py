class text_cleaner:
    """
    A simple text cleaning utility class.

    This class provides methods to:
    - Remove spaces from text
    - Remove special characters
    - Convert text to lowercase

    Each method prints the cleaned text.
    """

    def remove_extra_space(self, s):
        """
        Remove all spaces from the given text.

        Parameters
        ----------
        s : str
            Input string from which spaces will be removed.

        Example
        -------
        Input:  "Hello World"
        Output: "HelloWorld"
        """
        character = " "
        new_s = ""
        for i in s:
            if i != character:
                new_s += i
        print(new_s)

    def remove_special_characters(self, s):
        """
        Remove all special characters from the given text.

        Only letters and numbers are kept.  
        The cleaned text is stored globally for further processing.

        Parameters
        ----------
        s : str
            Input string containing special characters.

        Example
        -------
        Input:  "#Hello!!!123"
        Output: "Hello123"
        """
        global new_s1
        new_s1 = ""
        for i in s:
            if i.isalnum():
                new_s1 += i
        print(new_s1)

    def normalize_case(self, s):
        """
        Convert the previously cleaned text to lowercase.

        This method converts the text produced by
        `remove_special_characters` into lowercase.

        Example
        -------
        Input:  "HELLO"
        Output: "hello"
        """
        print(new_s1.lower())
