for row in $(echo "${values}" | jq -r '.[]'); do
    -jq() {
        echo ${row} | jq -r ${1}
    }
    echo $(_jq '.samplekey')
done