# Start with loading all necessary libraries
from wordcloud import WordCloud

import matplotlib.pyplot as plt

class WordCloudEngine:
    def __init__(self, data_path: str, removeable_words: list):
        self.data_path = data_path
        self.removeable_words = removeable_words
        self.image_filename: str = self.data_path.replace(".txt", "") + "_result_image.png"
        self.string_total_lenth = -1
        print('word cloud initialized')

    def open_file(self):
        with open(self.data_path, 'r', encoding='utf8') as txt_file:
            data = ""
            print("file open successfully")
            for line in txt_file.readlines():
                certain_line = line
                for removeable_word in self.removeable_words:
                    #print("before: ", certain_line)
                    certain_line = certain_line.replace(removeable_word, '')
                    #print("after: ", certain_line)
                data += certain_line
            self.string_total_lenth = len(data)
            print(f"process complete. Length: {self.string_total_lenth}.\n Head: {data[:100]}")
        return data

    def generate_word_cloud(self, data):
        print(f"processing file, estimate time for the process: {round(self.string_total_lenth/2000000, 2)} seconds")
        wordcloud = WordCloud(max_words=100, max_font_size=300 ,background_color="white", width=1600, height=800).generate(data)
        plt.figure(figsize=(20,10), facecolor='k')
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.savefig(self.image_filename)
        print(f'process complete, please check {self.image_filename} in your directory')


if __name__ == "__main__":
    # if you miss any package. please try pip install -r requirements.txt 
    # make sure file is in your project directory and you also switch to it
    #data_paths = ["review_chicago.txt", "reviews_hawaii.txt"]
    data_paths = ["reviews_hawaii.txt"]
    removeable_words = ['<br/>', 'Chicago', 'place', 'stay', 'ã', 'å', 'ä', 'á', '€', 'ž', 'œ', 'play', 'stay', 'ì', 'ë']
    for data_path in data_paths:
        word_cloud_engine = WordCloudEngine(data_path, removeable_words)
        data = word_cloud_engine.open_file()
        word_cloud_engine.generate_word_cloud(data)

