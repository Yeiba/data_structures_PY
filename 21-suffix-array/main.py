class SuffixArrayFast:
    DEFAULT_ALPHABET_SIZE = 256

    def __init__(self, text, alphabet_size=DEFAULT_ALPHABET_SIZE):
        self.T = self.to_int_array(text) if isinstance(text, str) else text
        self.N = len(self.T)
        self.alphabet_size = alphabet_size
        self.construct()

    # Converts a string to an integer array
    def to_int_array(self, text):
        return [ord(char) for char in text]

    # Construct the suffix array
    def construct(self):
        self.sa = [0] * self.N
        self.sa2 = [0] * self.N
        self.rank = [0] * self.N
        self.c = [0] * max(self.alphabet_size, self.N)

        # Step 1: Initialize rank and counting sort
        for i in range(self.N):
            self.rank[i] = self.T[i]
            self.c[self.rank[i]] += 1
        for i in range(1, self.alphabet_size):
            self.c[i] += self.c[i - 1]
        for i in range(self.N - 1, -1, -1):
            self.c[self.T[i]] -= 1
            self.sa[self.c[self.T[i]]] = i

        # Step 2: Update ranks and sort suffixes by doubling step size
        p = 1
        while True:
            # Step 2a: Initialize `sa2`
            r = 0
            for i in range(self.N - p, self.N):
                self.sa2[r] = i
                r += 1
            for i in range(self.N):
                if self.sa[i] >= p:
                    self.sa2[r] = self.sa[i] - p
                    r += 1

            # Step 2b: Counting sort on ranks
            self.c = [0] * max(self.alphabet_size, self.N)
            for i in range(self.N):
                self.c[self.rank[i]] += 1
            for i in range(1, self.alphabet_size):
                self.c[i] += self.c[i - 1]
            for i in range(self.N - 1, -1, -1):
                self.c[self.rank[self.sa2[i]]] -= 1
                self.sa[self.c[self.rank[self.sa2[i]]]] = self.sa2[i]

            # Step 2c: Update ranks
            self.sa2[self.sa[0]] = r = 0
            for i in range(1, self.N):
                prev = self.sa[i - 1]
                curr = self.sa[i]
                next_prev = (self.sa[i - 1] + p) % self.N
                next_curr = (self.sa[i] + p) % self.N
                if (self.rank[prev] != self.rank[curr] or
                        self.rank[next_prev] != self.rank[next_curr]):
                    r += 1
                self.sa2[self.sa[i]] = r
            self.rank, self.sa2 = self.sa2, self.rank
            if r == self.N - 1:
                break
            self.alphabet_size = r + 1

    def __str__(self):
        return f"Suffix Array: [{', '.join(map(str, self.sa))}]"


# Example Usage
if __name__ == "__main__":
    text = "banana"
    suffix_array = SuffixArrayFast(text)
    print(suffix_array)  # Should print the suffix array for the text "banana"
