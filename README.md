# arobot
Program that displays ARO logo on CyberPi's (mBot2) 128x128 LCD display


## How to use it?
*Just run it...*

If you're unable to import PIL or numpy on your CyberPi, do this:

1)  Run the `ARO_logo.py` and copy that loooooooooooong Array of Arrays of Nubmers:
   
    ```shell
    [xxx@yyy]$ python ARO_logo.py 
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9090524, 7120085, 7054549, 7054549, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7181768, 1797817, 1863353, 1863353,...], [...], ...]
   
    final length: 32

    Process finished with exit code 0
    ```
    
2)  Open the `main.py` and edit these lines:
    ```python
    import event, time, cyberpi
    from ARO_logo import generate_tiles
    
    # initialize variables
    
    tiles = generate_tiles()  # if PIL or Numpy not installed, replace this with pre-generated list sent in discord
    sprites = []
    ```
    
    Place the copied array in place of the `generat_tiles()` and comment `from ARO_logo import generate_tiles`:
    
    ```python
    import event, time, cyberpi
    # from ARO_logo import generate_tiles
    
    # initialize variables
    
    tiles = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9090524, 7120085, 7054549, 7054549, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7181768, 1797817, 1863353, 1863353,...], [...], ...]
    sprites = []
    ```

3)  Now just run the `main.py` :)

> Note: if you want to use your own image with different dimensions, you have to change the `filepath` in `ARO_logo.py` and also change the numbers in `main.py` in these brackets, which defines, where the tiles are going to render:
> ```python
>     for j in (40, 56, 72, 88):  # positioning the sprites
>         for k in (8, 24, 40, 56, 72, 88, 104, 120):
> ```
   
