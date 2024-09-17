SECRET_NAME="noftsite"
ROOT_DIR="$(git rev-parse --show-toplevel)"

SECRETS = $(aws secretsmanager get-secret-value --secret-id $SECRET_NAME --query SecretString --output text)
touch $ENV_DIR
echo $SECRETS | jq -r 'to_entries | map("\(.key)=\(.value|tostring)") | .[]' > $ENV_DIR
echo "Secrets written to $ENV_DIR"