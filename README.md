## Setup

export PROJECT_ID='marks-firestore-app'
export TOKEN=$(gcloud auth print-access-token)

pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib google-cloud-firestore

## Run

python3 firestore_latency_test.py | column -t -s,