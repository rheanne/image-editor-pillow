import os
from PIL import Image, ImageFilter
print("""Welcome to Rheanne's POKEMON Image Editor!

Here is a list of commands you are able to type in order to make changes to the photo of your choice: 

· User can save jpeg images to png. All new png files created will be moved to png folder 
· User can view all current jpeg and png images in their directories
· User should decide what size thumbnails (200, 400, or 600) they want 
· User should be given an option of rotating an image to a given length (users choice)
· User should be given an option to turn image to black and white. Save these pictures in a “Black & White” folder
· User should be able to blur an image. User should also be able to input a value of how much they want to blur the image.
· User the ability to add text! 
""")

i = 0
x = int(input("How many photos do you wish to edit? "))

for i in range(x):
    choice = str(input("Pick the image(s) you wish to make changes to by typing the corresponding number (eg: 1): "))
    
    if choice == '1':
        image1 = Image.open('poke1.jpg')
        image1.show()

#PNG
        png = input('Time to edit! Do you wish to save it as a png? Y/N: ')
        if png == 'Y':
            for f in os.listdir('.'):
                if f.endswith('poke1.jpg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))

        else: 
            pass
        
#THUMBNAIL SIZING
        size_200 = (200,200)
        size_400 = (400,400)
        size_600 = (600,600)

        thumbnail = input("Change thumbnail size? If yes then to which size: 200, 400, or 600 (just type the number as the response). If no just type N: ")
        if thumbnail == '200':

            for f in os.listdir('.'):
                    if f.endswith('poke1.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_200)
                        i.save('200/{}._200{}'.format(fn, fext))


        elif thumbnail == '400':
            for f in os.listdir('.'):
                    if f.endswith('poke1.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_400)
                        i.save('400/{}._400{}'.format(fn, fext))

        elif thumbnail == '600':
            for f in os.listdir('.'):
                    if f.endswith('poke1.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_600)
                        i.save('600/{}._600{}'.format(fn, fext))

        else:
             pass

#ROTATION OF IMAGE(S)

        rotate = input("Rotate image? If yes, how many degrees: 90 or 180. Please respond with the amount (e.g: 180). If no then type N: ")
        if rotate == '90':
             image1.rotate(90).save('poke1_rotate90.jpg')
        elif rotate == '180':
             image1.rotate(180).save('poke1_rotate180.jpg')

        else:
             pass

#BLACK/WHITE COLOR CHANGE

        bw = input("Change the image to black and white? (Y/N): ")
        if bw == "Y":
             image1.convert(mode='L').save('poke1_bw.jpg')

        else: 
             pass
        
#BLUR IMAGE

        blur = input("Blur image? (Y/N): ")
        if blur == 'Y':
             blurAmount = int(input("By how much do you want to blur the image: "))
             image1.filter(ImageFilter.GaussianBlur(blurAmount)).save('poke1_blur.jpg')
        
        else:
             pass
        
#CROP IMAGE
        
        crop = input("Want to crop image? (Y/N): ")

        if crop == "Y":
             width, height = image1.size
             left = 5
             top = height / 4
             right = 164
             bottom = 3 * height / 4

             image1Crop = image1.crop((left, top, right, bottom))
             image1Crop.save("poke1_crop.jpg")

        else:
             pass


    elif choice == '2':
        image2 = Image.open('poke2.jpg')
        image2.show()

    #PNG
        png = input('Time to edit! Do you wish to save it as a png? Y/N: ')
        if png == 'Y':
            for f in os.listdir('.'):
                if f.endswith('poke2.jpg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))

        else: 
            pass
        
#THUMBNAIL SIZING
        size_200 = (200,200)
        size_400 = (400,400)
        size_600 = (600,600)

        thumbnail = input("Change thumbnail size? If yes then to which size: 200, 400, or 600 (just type the number as the response). If no just type N: ")
        if thumbnail == '200':

            for f in os.listdir('.'):
                    if f.endswith('poke2.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_200)
                        i.save('200/{}._200{}'.format(fn, fext))


        elif thumbnail == '400':
            for f in os.listdir('.'):
                    if f.endswith('poke2.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_400)
                        i.save('400/{}._400{}'.format(fn, fext))

        elif thumbnail == '600':
            for f in os.listdir('.'):
                    if f.endswith('poke2.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_600)
                        i.save('600/{}._600{}'.format(fn, fext))

        else:
             pass

#ROTATION OF IMAGE(S)

        rotate = input("Rotate image? If yes, how many degrees: 90 or 180. Please respond with the amount (e.g: 180). If no then type N: ")
        if rotate == '90':
             image2.rotate(90).save('poke2_rotate90.jpg')
        elif rotate == '180':
             image2.rotate(180).save('poke2_rotate180.jpg')

        else:
             pass

#BLACK/WHITE COLOR CHANGE

        bw = input("Change the image to black and white? (Y/N): ")
        if bw == "Y":
             image2.convert(mode='L').save('poke2_bw.jpg')

        else: 
             pass
        
#BLUR IMAGE

        blur = input("Blur image? (Y/N): ")
        if blur == 'Y':
             blurAmount = int(input("By how much do you want to blur the image: "))
             image2.filter(ImageFilter.GaussianBlur(blurAmount)).save('poke2_blur.jpg')
        
        else:
             pass
        
#CROP IMAGE
        
        crop = input("Want to crop image? (Y/N): ")

        if crop == "Y":
             width, height = image2.size
             left = 5
             top = height / 4
             right = 164
             bottom = 3 * height / 4

             image2Crop = image2.crop((left, top, right, bottom))
             image2Crop.save("poke2_crop.jpg")

        else:
             pass

    elif choice == '3':
        image3 = Image.open('poke3.jpg')
        image3.show()

    #PNG
        png = input('Time to edit! Do you wish to save it as a png? Y/N: ')
        if png == 'Y':
            for f in os.listdir('.'):
                if f.endswith('poke3.jpg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))

        else: 
            pass
        
#THUMBNAIL SIZING
        size_200 = (200,200)
        size_400 = (400,400)
        size_600 = (600,600)

        thumbnail = input("Change thumbnail size? If yes then to which size: 200, 400, or 600 (just type the number as the response). If no just type N: ")
        if thumbnail == '200':

            for f in os.listdir('.'):
                    if f.endswith('poke3.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_200)
                        i.save('200/{}._200{}'.format(fn, fext))


        elif thumbnail == '400':
            for f in os.listdir('.'):
                    if f.endswith('poke3.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_400)
                        i.save('400/{}._400{}'.format(fn, fext))

        elif thumbnail == '600':
            for f in os.listdir('.'):
                    if f.endswith('poke3.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_600)
                        i.save('600/{}._600{}'.format(fn, fext))

        else:
             pass

#ROTATION OF IMAGE(S)

        rotate = input("Rotate image? If yes, how many degrees: 90 or 180. Please respond with the amount (e.g: 180). If no then type N: ")
        if rotate == '90':
             image3.rotate(90).save('poke3_rotate90.jpg')
        elif rotate == '180':
             image3.rotate(180).save('poke3_rotate180.jpg')

        else:
             pass

#BLACK/WHITE COLOR CHANGE

        bw = input("Change the image to black and white? (Y/N): ")
        if bw == "Y":
             image3.convert(mode='L').save('poke3_bw.jpg')

        else: 
             pass
        
#BLUR IMAGE

        blur = input("Blur image? (Y/N): ")
        if blur == 'Y':
             blurAmount = int(input("By how much do you want to blur the image: "))
             image3.filter(ImageFilter.GaussianBlur(blurAmount)).save('poke3_blur.jpg')
        
        else:
             pass
        
#CROP IMAGE
        
        crop = input("Want to crop image? (Y/N): ")

        if crop == "Y":
             width, height = image3.size
             left = 5
             top = height / 4
             right = 164
             bottom = 3 * height / 4

             image3Crop = image3.crop((left, top, right, bottom))
             image3Crop.save("poke3_crop.jpg")

        else:
             pass

    elif choice == '4':
        image4 = Image.open('poke4.jpg')
        image4.show()

    #PNG
        png = input('Time to edit! Do you wish to save it as a png? Y/N: ')
        if png == 'Y':
            for f in os.listdir('.'):
                if f.endswith('poke4.jpg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))

        else: 
            pass
        
#THUMBNAIL SIZING
        size_200 = (200,200)
        size_400 = (400,400)
        size_600 = (600,600)

        thumbnail = input("Change thumbnail size? If yes then to which size: 200, 400, or 600 (just type the number as the response). If no just type N: ")
        if thumbnail == '200':

            for f in os.listdir('.'):
                    if f.endswith('poke4.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_200)
                        i.save('200/{}._200{}'.format(fn, fext))


        elif thumbnail == '400':
            for f in os.listdir('.'):
                    if f.endswith('poke4.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_400)
                        i.save('400/{}._400{}'.format(fn, fext))

        elif thumbnail == '600':
            for f in os.listdir('.'):
                    if f.endswith('poke4.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_600)
                        i.save('600/{}._600{}'.format(fn, fext))

        else:
             pass

#ROTATION OF IMAGE(S)

        rotate = input("Rotate image? If yes, how many degrees: 90 or 180. Please respond with the amount (e.g: 180). If no then type N: ")
        if rotate == '90':
             image4.rotate(90).save('poke4_rotate90.jpg')
        elif rotate == '180':
             image4.rotate(180).save('poke4_rotate180.jpg')

        else:
             pass

#BLACK/WHITE COLOR CHANGE

        bw = input("Change the image to black and white? (Y/N): ")
        if bw == "Y":
             image4.convert(mode='L').save('poke4_bw.jpg')

        else: 
             pass
        
#BLUR IMAGE

        blur = input("Blur image? (Y/N): ")
        if blur == 'Y':
             blurAmount = int(input("By how much do you want to blur the image: "))
             image4.filter(ImageFilter.GaussianBlur(blurAmount)).save('poke4_blur.jpg')
        
        else:
             pass
        
#CROP IMAGE
        
        crop = input("Want to crop image? (Y/N): ")

        if crop == "Y":
             width, height = image4.size
             left = 5
             top = height / 4
             right = 164
             bottom = 3 * height / 4

             image4Crop = image4.crop((left, top, right, bottom))
             image4Crop.save("poke4_crop.jpg")

        else:
             pass

    elif choice == '5':
        image5 = Image.open('poke5.jpg')
        image5.show()

    #PNG
        png = input('Time to edit! Do you wish to save it as a png? Y/N: ')
        if png == 'Y':
            for f in os.listdir('.'):
                if f.endswith('poke5.jpg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))

        else: 
            pass
        
#THUMBNAIL SIZING
        size_200 = (200,200)
        size_400 = (400,400)
        size_600 = (600,600)

        thumbnail = input("Change thumbnail size? If yes then to which size: 200, 400, or 600 (just type the number as the response). If no just type N: ")
        if thumbnail == '200':

            for f in os.listdir('.'):
                    if f.endswith('poke5.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_200)
                        i.save('200/{}._200{}'.format(fn, fext))


        elif thumbnail == '400':
            for f in os.listdir('.'):
                    if f.endswith('poke5.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_400)
                        i.save('400/{}._400{}'.format(fn, fext))

        elif thumbnail == '600':
            for f in os.listdir('.'):
                    if f.endswith('poke5.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_600)
                        i.save('600/{}._600{}'.format(fn, fext))

        else:
             pass

#ROTATION OF IMAGE(S)

        rotate = input("Rotate image? If yes, how many degrees: 90 or 180. Please respond with the amount (e.g: 180). If no then type N: ")
        if rotate == '90':
             image5.rotate(90).save('poke5_rotate90.jpg')
        elif rotate == '180':
             image5.rotate(180).save('poke5_rotate180.jpg')

        else:
             pass

#BLACK/WHITE COLOR CHANGE

        bw = input("Change the image to black and white? (Y/N): ")
        if bw == "Y":
             image5.convert(mode='L').save('poke5_bw.jpg')

        else: 
             pass
        
#BLUR IMAGE

        blur = input("Blur image? (Y/N): ")
        if blur == 'Y':
             blurAmount = int(input("By how much do you want to blur the image: "))
             image5.filter(ImageFilter.GaussianBlur(blurAmount)).save('poke5_blur.jpg')
        
        else:
             pass
        
#CROP IMAGE
        
        crop = input("Want to crop image? (Y/N): ")

        if crop == "Y":
             width, height = image5.size
             left = 5
             top = height / 4
             right = 164
             bottom = 3 * height / 4

             image5Crop = image5.crop((left, top, right, bottom))
             image5Crop.save("poke5_crop.jpg")

        else:
             pass

    elif choice == '6':
        image6 = Image.open('poke6.jpg')
        image6.show()

    #PNG
        png = input('Time to edit! Do you wish to save it as a png? Y/N: ')
        if png == 'Y':
            for f in os.listdir('.'):
                if f.endswith('poke6.jpg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))

        else: 
            pass
        
#THUMBNAIL SIZING
        size_200 = (200,200)
        size_400 = (400,400)
        size_600 = (600,600)

        thumbnail = input("Change thumbnail size? If yes then to which size: 200, 400, or 600 (just type the number as the response). If no just type N: ")
        if thumbnail == '200':

            for f in os.listdir('.'):
                    if f.endswith('poke6.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_200)
                        i.save('200/{}._200{}'.format(fn, fext))


        elif thumbnail == '400':
            for f in os.listdir('.'):
                    if f.endswith('poke6.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_400)
                        i.save('400/{}._400{}'.format(fn, fext))

        elif thumbnail == '600':
            for f in os.listdir('.'):
                    if f.endswith('poke6.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_600)
                        i.save('600/{}._600{}'.format(fn, fext))

        else:
             pass

#ROTATION OF IMAGE(S)

        rotate = input("Rotate image? If yes, how many degrees: 90 or 180. Please respond with the amount (e.g: 180). If no then type N: ")
        if rotate == '90':
             image6.rotate(90).save('poke6_rotate90.jpg')
        elif rotate == '180':
             image6.rotate(180).save('poke6_rotate180.jpg')

        else:
             pass

#BLACK/WHITE COLOR CHANGE

        bw = input("Change the image to black and white? (Y/N): ")
        if bw == "Y":
             image6.convert(mode='L').save('poke6_bw.jpg')

        else: 
             pass
        
#BLUR IMAGE

        blur = input("Blur image? (Y/N): ")
        if blur == 'Y':
             blurAmount = int(input("By how much do you want to blur the image: "))
             image6.filter(ImageFilter.GaussianBlur(blurAmount)).save('poke6_blur.jpg')
        
        else:
             pass
        
#CROP IMAGE
        
        crop = input("Want to crop image? (Y/N): ")

        if crop == "Y":
             width, height = image6.size
             left = 5
             top = height / 4
             right = 164
             bottom = 3 * height / 4

             image6Crop = image6.crop((left, top, right, bottom))
             image6Crop.save("poke6_crop.jpg")

        else:
             pass

    elif choice == '7':
        image7 = Image.open('poke7.jpg')
        image7.show()

    #PNG
        png = input('Time to edit! Do you wish to save it as a png? Y/N: ')
        if png == 'Y':
            for f in os.listdir('.'):
                if f.endswith('poke7.jpg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))

        else: 
            pass
        
#THUMBNAIL SIZING
        size_200 = (200,200)
        size_400 = (400,400)
        size_600 = (600,600)

        thumbnail = input("Change thumbnail size? If yes then to which size: 200, 400, or 600 (just type the number as the response). If no just type N: ")
        if thumbnail == '200':

            for f in os.listdir('.'):
                    if f.endswith('poke7.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_200)
                        i.save('200/{}._200{}'.format(fn, fext))


        elif thumbnail == '400':
            for f in os.listdir('.'):
                    if f.endswith('poke7.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_400)
                        i.save('400/{}._400{}'.format(fn, fext))

        elif thumbnail == '600':
            for f in os.listdir('.'):
                    if f.endswith('poke7.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_600)
                        i.save('600/{}._600{}'.format(fn, fext))

        else:
             pass

#ROTATION OF IMAGE(S)

        rotate = input("Rotate image? If yes, how many degrees: 90 or 180. Please respond with the amount (e.g: 180). If no then type N: ")
        if rotate == '90':
             image7.rotate(90).save('poke7_rotate90.jpg')
        elif rotate == '180':
             image7.rotate(180).save('poke7_rotate180.jpg')

        else:
             pass

#BLACK/WHITE COLOR CHANGE

        bw = input("Change the image to black and white? (Y/N): ")
        if bw == "Y":
             image7.convert(mode='L').save('poke7_bw.jpg')

        else: 
             pass
        
#BLUR IMAGE

        blur = input("Blur image? (Y/N): ")
        if blur == 'Y':
             blurAmount = int(input("By how much do you want to blur the image: "))
             image7.filter(ImageFilter.GaussianBlur(blurAmount)).save('poke7_blur.jpg')
        
        else:
             pass
        
#CROP IMAGE
        
        crop = input("Want to crop image? (Y/N): ")

        if crop == "Y":
             width, height = image7.size
             left = 5
             top = height / 4
             right = 164
             bottom = 3 * height / 4

             image7Crop = image7.crop((left, top, right, bottom))
             image7Crop.save("poke7_crop.jpg")

        else:
             pass


    elif choice == '8':
        image8 = Image.open('poke8.jpg')
        image8.show()

#PNG
        png = input('Time to edit! Do you wish to save it as a png? Y/N: ')
        if png == 'Y':
            for f in os.listdir('.'):
                if f.endswith('poke8.jpg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))

        else: 
            pass
        
#THUMBNAIL SIZING
        size_200 = (200,200)
        size_400 = (400,400)
        size_600 = (600,600)

        thumbnail = input("Change thumbnail size? If yes then to which size: 200, 400, or 600 (just type the number as the response). If no just type N: ")
        if thumbnail == '200':

            for f in os.listdir('.'):
                    if f.endswith('poke8.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_200)
                        i.save('200/{}._200{}'.format(fn, fext))


        elif thumbnail == '400':
            for f in os.listdir('.'):
                    if f.endswith('poke8.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_400)
                        i.save('400/{}._400{}'.format(fn, fext))

        elif thumbnail == '600':
            for f in os.listdir('.'):
                    if f.endswith('poke8.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_600)
                        i.save('600/{}._600{}'.format(fn, fext))

        else:
             pass

#ROTATION OF IMAGE(S)

        rotate = input("Rotate image? If yes, how many degrees: 90 or 180. Please respond with the amount (e.g: 180). If no then type N: ")
        if rotate == '90':
             image8.rotate(90).save('poke8_rotate90.jpg')
        elif rotate == '180':
             image8.rotate(180).save('poke8_rotate180.jpg')

        else:
             pass

#BLACK/WHITE COLOR CHANGE

        bw = input("Change the image to black and white? (Y/N): ")
        if bw == "Y":
             image8.convert(mode='L').save('poke8_bw.jpg')

        else: 
             pass
        
#BLUR IMAGE

        blur = input("Blur image? (Y/N): ")
        if blur == 'Y':
             blurAmount = int(input("By how much do you want to blur the image: "))
             image8.filter(ImageFilter.GaussianBlur(blurAmount)).save('poke8_blur.jpg')
        
        else:
             pass
        
#CROP IMAGE
        
        crop = input("Want to crop image? (Y/N): ")

        if crop == "Y":
             width, height = image8.size
             left = 5
             top = height / 4
             right = 164
             bottom = 3 * height / 4

             image8Crop = image8.crop((left, top, right, bottom))
             image8Crop.save("poke8_crop.jpg")

        else:
             pass

    elif choice == '9':
        image9 = Image.open('poke9.jpg')
        image9.show()

    #PNG
        png = input('Time to edit! Do you wish to save it as a png? Y/N: ')
        if png == 'Y':
            for f in os.listdir('.'):
                if f.endswith('poke9.jpg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))

        else: 
            pass
        
#THUMBNAIL SIZING
        size_200 = (200,200)
        size_400 = (400,400)
        size_600 = (600,600)

        thumbnail = input("Change thumbnail size? If yes then to which size: 200, 400, or 600 (just type the number as the response). If no just type N: ")
        if thumbnail == '200':

            for f in os.listdir('.'):
                    if f.endswith('poke9.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_200)
                        i.save('200/{}._200{}'.format(fn, fext))


        elif thumbnail == '400':
            for f in os.listdir('.'):
                    if f.endswith('poke9.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_400)
                        i.save('400/{}._400{}'.format(fn, fext))

        elif thumbnail == '600':
            for f in os.listdir('.'):
                    if f.endswith('poke9.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_600)
                        i.save('600/{}._600{}'.format(fn, fext))

        else:
             pass

#ROTATION OF IMAGE(S)

        rotate = input("Rotate image? If yes, how many degrees: 90 or 180. Please respond with the amount (e.g: 180). If no then type N: ")
        if rotate == '90':
             image1.rotate(90).save('poke9_rotate90.jpg')
        elif rotate == '180':
             image1.rotate(180).save('poke9_rotate180.jpg')

        else:
             pass

#BLACK/WHITE COLOR CHANGE

        bw = input("Change the image to black and white? (Y/N): ")
        if bw == "Y":
             image9.convert(mode='L').save('poke9_bw.jpg')

        else: 
             pass
        
#BLUR IMAGE

        blur = input("Blur image? (Y/N): ")
        if blur == 'Y':
             blurAmount = int(input("By how much do you want to blur the image: "))
             image9.filter(ImageFilter.GaussianBlur(blurAmount)).save('poke9_blur.jpg')
        
        else:
             pass
        
#CROP IMAGE
        
        crop = input("Want to crop image? (Y/N): ")

        if crop == "Y":
             width, height = image9.size
             left = 5
             top = height / 4
             right = 164
             bottom = 3 * height / 4

             image9Crop = image9.crop((left, top, right, bottom))
             image9Crop.save("poke9_crop.jpg")

        else:
             pass

    elif choice == '10':
        image10 = Image.open('poke10.jpg')
        image10.show()

    #PNG
        png = input('Time to edit! Do you wish to save it as a png? Y/N: ')
        if png == 'Y':
            for f in os.listdir('.'):
                if f.endswith('poke10.jpg'):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)
                    i.save('pngs/{}.png'.format(fn))

        else: 
            pass
        
#THUMBNAIL SIZING
        size_200 = (200,200)
        size_400 = (400,400)
        size_600 = (600,600)

        thumbnail = input("Change thumbnail size? If yes then to which size: 200, 400, or 600 (just type the number as the response). If no just type N: ")
        if thumbnail == '200':

            for f in os.listdir('.'):
                    if f.endswith('poke10.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_200)
                        i.save('200/{}._200{}'.format(fn, fext))


        elif thumbnail == '400':
            for f in os.listdir('.'):
                    if f.endswith('poke10.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_400)
                        i.save('400/{}._400{}'.format(fn, fext))

        elif thumbnail == '600':
            for f in os.listdir('.'):
                    if f.endswith('poke10.jpg'):
                        i = Image.open(f)
                        fn, fext = os.path.splitext(f)

                        i.thumbnail(size_600)
                        i.save('600/{}._600{}'.format(fn, fext))

        else:
             pass

#ROTATION OF IMAGE(S)

        rotate = input("Rotate image? If yes, how many degrees: 90 or 180. Please respond with the amount (e.g: 180). If no then type N: ")
        if rotate == '90':
             image10.rotate(90).save('poke10_rotate90.jpg')
        elif rotate == '180':
             image10.rotate(180).save('poke10_rotate180.jpg')

        else:
             pass

#BLACK/WHITE COLOR CHANGE

        bw = input("Change the image to black and white? (Y/N): ")
        if bw == "Y":
             image10.convert(mode='L').save('poke10_bw.jpg')

        else: 
             pass
        
#BLUR IMAGE

        blur = input("Blur image? (Y/N): ")
        if blur == 'Y':
             blurAmount = int(input("By how much do you want to blur the image: "))
             image10.filter(ImageFilter.GaussianBlur(blurAmount)).save('poke10_blur.jpg')
        
        else:
             pass
        
#CROP IMAGE
        
        crop = input("Want to crop image? (Y/N): ")

        if crop == "Y":
             width, height = image10.size
             left = 5
             top = height / 4
             right = 164
             bottom = 3 * height / 4

             image10Crop = image10.crop((left, top, right, bottom))
             image10Crop.save("poke10_crop.jpg")

        else:
             pass


