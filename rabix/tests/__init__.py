
infinite_loop = {
    "tool": {
        "softwareDescription": {},
        "documentAuthor": "boysha",
        "requirements": {
            "environment": {
                "container": {
                    "type": "docker",
                    "uri": "docker:infinite_loop#latest",
                    "imageId": "e678dddee492"
                }
            },
            "resources": {},
            "platformFeatures": []
        },
        "inputs": {},
        "outputs": {},
        "adapter": {
            "baseCmd": [],
            "stdout": "output.sam",
            "args": []
        }
    }
}

mock_app_good_repo = {
    "tool": {
        "softwareDescription": {},
        "documentAuthor": "boysha",
        "requirements": {
            "environment": {
                "container": {
                    "type": "docker",
                    "uri": "docker:ubuntu#14.10",
                    "imageId": "f14704ad99b8"
                }
            },
            "resources": {},
            "platformFeatures": []
        },
        "inputs": {},
        "outputs": {},
        "adapter": {
            "baseCmd": [],
            "stdout": "output.sam",
            "args": []
        }
    }
}

mock_app_bad_repo = {
    "tool": {
        "softwareDescription": {},
        "documentAuthor": "boysha",
        "requirements": {
            "environment": {
                "container": {
                    "type": "docker",
                    "uri": "docker://wrongrepository#latest",
                    "imageId": "aaaaaaaaaaaa"
                }
            },
            "resources": {},
            "platformFeatures": []
        },
        "inputs": {},
        "outputs": {},
        "adapter": {
            "baseCmd": [],
            "stdout": "output.sam",
            "args": []
        }
    }
}
