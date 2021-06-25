# magic_mirror_face_recognition

This is a module for the [MagicMirror²](https://github.com/MichMich/MagicMirror/).

## Installation
1.Install Magic Mirror by running this command:
    ```bash -c  "$(curl -sL https://raw.githubusercontent.com/sdetweil/MagicMirror_scripts/master/raspberry.sh)"```

2.Navigate to the "modules" folder and pull **this** repo

3.Run npm install in this folder

4.To test on a computer, run ````node ServerOnly```` in the "MagicMirror" root directory

5.To view the Mirror navigate to http://localhost:8080/ in your webbrowser.

## Connect to local Magic Mirror via SSH
1. run this command in shell: ````ssh pi@raspberrypi.local```` and input credentials
2. The raspi is configured with VNC viewer. Connect using the above address and credentials


## Installation
1. Install all the dependencies from the PIPFILE
2. ````pip install pipenv````
3. ````pipenv sync````



## Using the module

To use this module, add the following configuration block to the modules array in the `config/config.js` file:
```js
var config = {
    modules: [
        {
            module: 'magic_mirror_face_recognition',
            config: {
                // See below for configurable options
            }
        }
    ]
}
```

## Configuration options

| Option           | Description
|----------------- |-----------
| `option1`        | *Required* DESCRIPTION HERE
| `option2`        | *Optional* DESCRIPTION HERE TOO <br><br>**Type:** `int`(milliseconds) <br>Default 60000 milliseconds (1 minute)
