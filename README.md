# arobot
Program that displays ARO logo on CyberPi's (mBot2) 128x128 LCD display


## How to use it?
*Just run it...*

If you're unable to import PIL or numpy on your CyberPi, do this:

1)  Run the `image_processing.py` and copy that loooooooooooong Array of Arrays of Nubmers:
   
    ```shell
    [xxx@yyy]$ python image_processing.py 
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9090524, 7120085, 7054549, 7054549, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7181768, 1797817, 1863353, 1863353,...], [...], ...]
    final size: 128x64

    Process finished with exit code 0
    ```
    
2)  Open the `main.py` and edit these lines:
    ```python
    import event, time, cyberpi
    from image_processing import generate_tiles  # if PIL or Numpy not installed, comment this line
    
    # initialize variables
    
    im_array = generate_tiles()  # if PIL or Numpy not installed, replace this with pre-generated list from image_processing.py
    sprite = cyberpi.sprite()
    width = len(im_array[0])
    height = len(im_array)
    ...
    ```
    
    Place the copied array in place of the `generat_tiles()` and comment `from ARO_logo import generate_tiles`:
    
    ```python
    import event, time, cyberpi
    # from ARO_logo import generate_tiles
    
    # initialize variables
    
    tiles = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9090524, 7120085, 7054549, 7054549, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7181768, 1797817, 1863353, 1863353,...], [...], ...]
    sprites = []
    ...
    ```

3)  Now just run the `main.py` :)

> Note: if you want to use your own image with different dimensions, you have to change the `filepath` in `image_processing.py`:
> 
> ```python
> def generate_tiles():
>     filepath = "./ARO_logo-removebg-preview_1.png"  # downscaled and cropped image, so it has 128x64
>     test = "./test002.png"  # testing image ("./test001.png", "./test002.png")
>
>     imp = Image.open(filepath)
>     ...
> ```
> 
> Also make sure that the image is not larger than 128x128!
   
