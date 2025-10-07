{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMTlefkx6ljgfuoJYVhowsr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AlisaUrikh/uni_repo/blob/main/task.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 40,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UlnD744IxPxH",
        "outputId": "a1c391a0-6547-4668-8b77-9b0b1ee6ba90"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Найденная песня: Sweet Child O' Mine\n",
            "Похожие песни: Hotel California, Billie Jean, Good Vibrations\n"
          ]
        }
      ],
      "source": [
        "import json\n",
        "\n",
        "class Dataset:\n",
        "    def __init__(self, filename='/content/api.json'):\n",
        "        self.filename = filename\n",
        "        self.data = self._read_json()\n",
        "\n",
        "    def _read_json(self):\n",
        "        \"\"\" Функция для чтения JSON-файла. \"\"\"\n",
        "        try:\n",
        "            with open (self.filename, 'r', encoding= 'utf-8') as file:\n",
        "                text = json.load(file)\n",
        "                return(text)\n",
        "        except FileNotFoundError:\n",
        "            print (f'Ошибка: файл \"{self.filename}\" не найден!')\n",
        "        except json.JSONDecodeError:\n",
        "            print(f\"Ошибка декодирования JSON\")\n",
        "\n",
        "    def get_song(self, id):\n",
        "        \"\"\" Функция для поиска песни по id. \"\"\"\n",
        "        if self.data is not None:\n",
        "            for i in self.data:\n",
        "                if i['id'] == id:\n",
        "                    return i['title']\n",
        "            return 'Нет записи с таким id'\n",
        "\n",
        "    def find_similar(self, id):\n",
        "        \"\"\"Функция для поиска похожих песен.\"\"\"\n",
        "        songs = []\n",
        "        if self.data is not None:\n",
        "            for i in self.data:\n",
        "                if i['id'] == id:\n",
        "                    songs = [self.data[y-1]['title'] for y in i['similar_ids']]\n",
        "            return songs\n",
        "        return 'Нет записи с таким id'\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    id = 4\n",
        "    dataset = Dataset()\n",
        "    result = dataset.get_song(id)\n",
        "    similar_songs = dataset.find_similar(id)\n",
        "    print(f'Найденная песня: {result}')\n",
        "    print(f'Похожие песни: {', '.join(similar_songs)}')"
      ]
    }
  ]
}