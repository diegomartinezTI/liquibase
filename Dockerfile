FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from your project folder.
COPY XX_AP_UPL_MERCHANT_DOCS_NPRD_.key  .
RUN gpg --import XX_AP_UPL_MERCHANT_DOCS_NPRD_.key
COPY requirements.txt  . 
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]