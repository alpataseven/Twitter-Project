TR

# Twitter Auto-Like Bot 🤖❤️

## 📌 Proje Açıklaması

Bu Selenium tabanlı otomasyon projesi, Twitter'da belirlediğiniz bir arama terimi için sonuçları otomatik olarak beğenir ve yer işaretlerine ekler.

## ✨ Özellikler

- ✅ Twitter giriş otomasyonu

- 🔍 Özelleştirilebilir arama terimleri

- ♻️ Dinamik sayfa kaydırma

- ⏱️ Akıllı bekleme sistemleri

## 🛠️ Kurulum

### Gereksinimler

```bash
Python 3.8+
Google Chrome v115+
   ```

### Adım Adım Kurulum

1. Depoyu klonlayın:
  ```bash
    git clone https://github.com/alpataseven/Twitter-Project.git
    cd Twitter-Project
  ```
2. Sanal ortam oluşturun (önerilir):
  ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
  ```
3. Gerekli paketleri yükleyin:
  ```bash
    pip install -r requirements.txt
  ```
4. userInformation.py dosyasını düzenleyin:
     ```bash
      def UserName():
      return "twitter_kullanici_adiniz"
  
      def Password():
          return "twitter_sifreniz"
    ```
### 🚀 Kullanım

```bash
python autolike.py
```

### 🌟 Katkı

Hatalar ve öneriler için Issues bölümünü kullanın. PR'larınızı bekliyorum!

ENG

# Twitter Auto-Like Bot 🤖❤️

## 📌 Project Description

This is a Selenium-based automation project that automatically likes and bookmarks tweets on Twitter based on a specified search term.

## ✨ Features

- ✅ Automated Twitter login  
- 🔍 Customizable search terms  
- ♻️ Dynamic scrolling through results  
- ⏱️ Smart wait mechanisms to mimic human behavior  

## 🛠️ Setup

### Requirements

```bash
Python 3.8+
Google Chrome v115+
```

### 🔧 Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/alpataseven/Twitter-Project.git
   cd Twitter-Project
   ```
2. **(Optional) Create and activate a virtual environment**
   ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```
3. **Install the required packages**
   ```bash
    pip install -r requirements.txt
    ```
4. **Configure your Twitter credentials**
   Open the userInformation.py file and edit it as follows:
   ```bash
      def UserName():
      return "twitter_kullanici_adiniz"
  
      def Password():
          return "twitter_sifreniz"
   ```
## 🚀 Usage

```bash
python autolike.py
```

## 🌟 Contribution

Use the Issues section to report bugs and suggestions. I'm waiting for your PRs!
