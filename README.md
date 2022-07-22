# KBA FastAPI

This connects the KBA map tool Angular frontend to the KBA API hosted at Cambridge.

## Build the docker image
Run `docker build -t myimage .`

## Submit to `Google Cloud Platform`
1. Submit a new build whose image is called `kbaimage`: 
```
gcloud builds submit --tag gcr.io/kba-map-342017/kbaimage
```
2. View the uploaded image: [https://console.cloud.google.com/gcr/images/kba-map-342017/global/kbaimage?project=kba-map-342017](https://console.cloud.google.com/gcr/images/kba-map-342017/global/kbaimage?project=kba-map-342017)
3. Deploy to [`Cloud Run`](https://console.cloud.google.com/run?project=kba-map-342017) using the GUI.
4. View the deployment at: [https://kbaimage-lxdyktsplq-uc.a.run.app](https://kbaimage-lxdyktsplq-uc.a.run.app)