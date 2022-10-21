- This project was created using [Google Colab](https://colab.research.google.com/).
- You can also view this project in Colab [here](https://colab.research.google.com/drive/17ACUSj_MVoD7IyVRn5MfSDnsCsU0fkke?usp=sharing).
## **Averaging filter :**
> This method appears to make my image more smooth by reducing the amount color variation in the pixels between neighbouring pixels; including itself.
## **Sobel filter :**
> - For the vertical implementation, if you look at the blurred light fixtures in the background, there appears to be a horizontal white streak on the right side of each illuminated light.
> - For the horizontal implementation, if you look at the blurred light fixtures in the background, there appears to be a vertical white streak on the bottom of each illuminated light.
> - For the gradient edge implementation, if you look at the blurred light fixtures in the background, the lights appear to have a full white circle around each illuminated light, along with much more clean edges than the previous 2.
## **Laplacian filter :**
> This method appears to be very similar to the gradient edge implementaion above but appears to have more dark areas in comparison.
## **Median filter :**
> This method does not create new unrealistic pixel values when on the filters edges, while also filtering noise. For this reason, the median filter is much better at preserving sharp edges compared to the average (mean) filter for this image.
## **Gaussian filter :**
> This filter is used with the 2-D filter operator to blur the image and remove detail and noise as well as the average and median filters. This iamge does appear to be closer in appearance to the average filter.
