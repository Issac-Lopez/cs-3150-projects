## This project was created using [https://colab.research.google.com/](Google Colab).
## You can use view my project in Colab [https://colab.research.google.com/drive/1I-fsfalshe-hYstXF4KT7LjA2EXckWPG?usp=sharing](here).
## 1. **Read Image**
#### 1.1. Mount Drive
> Use `cp -r` following the file path in drive to portrait image location then saving the image in to a **mydata** directory created in colab.
#### 1.2. Imports
> Import appropriate libararies to display image and manipulate it.
#### 1.3. Python Explained
> Reading and displaying image in grayscale.
> - Read image from file location using `cv2.imread()`
> - To see matrices of image using `print()`
> - Convert image into grayscale using `cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)` to work in colab.
## 2. **Removing Irrelevant Background**
#### 2.1. How For loops Work 
> - The first `for` loop needed for the rows in the image using the `length` in `range()`.
> - The nested `for` loop needed for the columns in the image using the `width` in `range()`.
> -  `If` statement used to correctly size foreground image to the background with `mth.sqrt`. Which then displays white background.
## 3. **BONUS**
### 3.1. What Can Use Some More Work...
> - Making the colors on the background and foreground different.
> - Repositioning my portrait to be more centered to my face withitn the radius of the circle.
> - Creating a more unique background using `cmap='prism'`, for example.
### 3.2. Image Enhancements Approaches
> Enhanced my image incorporating the Gamma/power law to make the image more visible with the grayscale. 
