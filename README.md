# magic_mirror_face_recognition

This is a module for the [MagicMirror²](https://github.com/MichMich/MagicMirror/).

This repo is where our facial recognition module for magic mirror lives. 
## Local testing
To utilize local testing for this module you need to first create a local instance of MagicMirror as by running this script: 
```bash -c  "$(curl -sL https://raw.githubusercontent.com/sdetweil/MagicMirror_scripts/master/raspberry.sh)"```
[Credits](https://github.com/sdetweil/MagicMirror_scripts) 

Once Magicmirror is installed run ```node ServerOnly```

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
