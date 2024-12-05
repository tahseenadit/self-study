# Orchestration

When we say a **pipeline orchestrates an ML workflow**, it means that the pipeline manages the sequence of steps required to build, train, validate, deploy, and monitor a machine learning (ML) model. The pipeline ensures these steps are executed in the correct order, with the right data, and under specified conditions.

### **Breaking Down the Key Concepts**

---

### **1. What is an ML Workflow?**
An **ML workflow** consists of a series of tasks required to develop and operationalize a machine learning model. These tasks often include:
- **Data Preprocessing**:
  - Cleaning and transforming raw data into a usable format.
  - Splitting data into training, validation, and test sets.
- **Feature Engineering**:
  - Creating features from raw data to improve model performance.
- **Model Training**:
  - Using training data to fit a machine learning algorithm.
- **Model Validation**:
  - Evaluating the model’s performance on validation data to fine-tune hyperparameters.
- **Model Deployment**:
  - Putting the trained model into production for real-world use.
- **Monitoring and Maintenance**:
  - Continuously tracking the model's performance and retraining it as necessary.

---

### **2. What is a Pipeline?**
A **pipeline** is an automated process that links these individual tasks in a structured sequence. It ensures:
- Each task receives the correct inputs.
- Tasks are executed in the right order.
- Results from one step are passed to the next step seamlessly.

Think of it as an **assembly line** for ML workflows:
- Data preprocessing is the "input stage."
- Feature engineering is the "processing stage."
- Model training is the "assembly stage."
- Model deployment is the "output stage."

---

### **3. What Does "Orchestrate" Mean?**
**Orchestration** in this context refers to the management and coordination of tasks within the pipeline. It involves:
- **Resource Allocation**:
  - Assigning the necessary compute resources (e.g., GPUs, CPUs) for each step.
- **Error Handling**:
  - Managing failures (e.g., retrying a failed task or alerting when something breaks).
- **Task Scheduling**:
  - Ensuring tasks are run in the correct order (e.g., you can’t train a model before preparing the data).
- **Dependency Management**:
  - Handling dependencies between tasks (e.g., the output of data preprocessing is used as input for training).

---

### **4. Benefits of Orchestrating ML Workflows with Pipelines**
- **Automation**:
  - Reduces manual effort by automating repetitive tasks.
- **Consistency**:
  - Ensures all steps are executed in the same way each time, reducing errors.
- **Scalability**:
  - Pipelines can scale to handle large datasets and complex workflows.
- **Reproducibility**:
  - Makes it easier to replicate workflows for debugging or auditing.
- **Monitoring**:
  - Allows for tracking progress and performance metrics throughout the workflow.

---

### **5. Example of an ML Pipeline**
Imagine a pipeline for building a model to predict house prices:
1. **Step 1: Data Collection**:
   - Load raw data from a database or CSV files.
2. **Step 2: Data Preprocessing**:
   - Clean missing values, normalize features, and split data into training and test sets.
3. **Step 3: Feature Engineering**:
   - Create new features (e.g., square footage per room) to improve model performance.
4. **Step 4: Model Training**:
   - Train a regression model using the preprocessed data.
5. **Step 5: Model Evaluation**:
   - Validate the model on a test set and tune hyperparameters if needed.
6. **Step 6: Model Deployment**:
   - Deploy the trained model to a production server.
7. **Step 7: Monitoring**:
   - Continuously monitor the model’s performance in production and trigger retraining if necessary.

---

### **6. Tools for Pipeline Orchestration**
Popular tools and platforms for orchestrating ML workflows include:
- **Kubeflow Pipelines**:
  - Designed for Kubernetes, it enables seamless orchestration of containerized ML tasks.
- **Apache Airflow**:
  - General-purpose workflow orchestration that’s widely used in ML workflows.
- **MLflow**:
  - Tracks the full lifecycle of an ML project, from experimentation to deployment.
- **TensorFlow Extended (TFX)**:
  - A library for deploying production-ready ML pipelines.
- **Vertex AI Pipelines**:
  - Google Cloud’s tool for orchestrating end-to-end ML workflows.


## Vertex AI Pipelines: Pipeline orchestrates ML workflow
- Serverless
- Portable
- Scaleable
- based on containers and Google Cloud services

You can use two SDKs **(** an SDK serves as a complete toolkit for developers to build and enhance applications, streamlining integration with specific platforms or services (Core Libraries, APIs, Compilers, Debuggers, Documentation, Templates, Dependency management tools (e.g., Maven, Gradle), Build scripts or frameworks (e.g., CMake for C/C++ projects), Runtime Environment (i.e Java Virtual Machine in the JDK), Testing tools etc)**)** to create a ML pipeline in vertex AI. They are:

- Kubeflow Pipelines SDK v1.8 or later (v2 is recommended)
  - build custom components or reuse prebuilt components 
- TensorFlow Extended v0.30.0 or later
  - TensorFlow in an ML workflow that processes terabytes of structured data or text data. TFX pipeline is not recommended since it is a very specific solution for very-high load tensorflow use-cases and it incurs a high penalty due to the complexity and poor integration with Vertex AI.
 
Suppose I have the following workflow:

```
    ds_op = ImageDatasetCreateOp(
        project=project_id,
        display_name="flowers",
        gcs_source="gs://cloud-samples-data/vision/automl_classification/flowers/all_data_v2.csv",
        import_schema_uri=aiplatform.schema.dataset.ioformat.image.single_label_classification,
    )

    # The second step is a model training component. It takes the dataset
    # outputted from the first step, supplies it as an input argument to the
    # component (see `dataset=ds_op.outputs["dataset"]`), and will put its
    # outputs into `training_job_run_op`.
    training_job_run_op = AutoMLImageTrainingJobRunOp(
        project=project_id,
        display_name="train-iris-automl-mbsdk-1",
        prediction_type="classification",
        model_type="CLOUD",
        dataset=ds_op.outputs["dataset"],
        model_display_name="iris-classification-model-mbsdk",
        training_fraction_split=0.6,
        validation_fraction_split=0.2,
        test_fraction_split=0.2,
        budget_milli_node_hours=8000,
    )

    # The third and fourth step are for deploying the model.
    create_endpoint_op = EndpointCreateOp(
        project=project_id,
        display_name = "create-endpoint",
    )

    model_deploy_op = ModelDeployOp(
        model=training_job_run_op.outputs["model"],
        endpoint=create_endpoint_op.outputs['endpoint'],
        automatic_resources_min_replica_count=1,
        automatic_resources_max_replica_count=1,
    )
```

In the above workflow, workflow components are:

- ds_op
- training_job_run_op
- create_endpoint_op
- model_deploy_op

Now These components are google_cloud_pipeline_components, means these components are defined in the google_cloud_pipeline_components. Therefore, I need to import them:

```
from google_cloud_pipeline_components.v1.dataset import ImageDatasetCreateOp
from google_cloud_pipeline_components.v1.automl.training_job import AutoMLImageTrainingJobRunOp
from google_cloud_pipeline_components.v1.endpoint import EndpointCreateOp, ModelDeployOp
```

But then how do I define this workflow as a kubeflow pipeline. Like below:

```
import kfp
from google.cloud import aiplatform
from google_cloud_pipeline_components.v1.dataset import ImageDatasetCreateOp
from google_cloud_pipeline_components.v1.automl.training_job import AutoMLImageTrainingJobRunOp
from google_cloud_pipeline_components.v1.endpoint import EndpointCreateOp, ModelDeployOp

project_id = PROJECT_ID
pipeline_root_path = PIPELINE_ROOT

# Define the workflow of the pipeline.
@kfp.dsl.pipeline(
    name="automl-image-training-v2",
    pipeline_root=pipeline_root_path)
def pipeline(project_id: str):
    # The first step of your workflow is a dataset generator.
    # This step takes a Google Cloud Pipeline Component, providing the necessary
    # input arguments, and uses the Python variable `ds_op` to define its
    # output. Note that here the `ds_op` only stores the definition of the
    # output but not the actual returned object from the execution. The value
    # of the object is not accessible at the dsl.pipeline level, and can only be
    # retrieved by providing it as the input to a downstream component.
    ds_op = ImageDatasetCreateOp(
        project=project_id,
        display_name="flowers",
        gcs_source="gs://cloud-samples-data/vision/automl_classification/flowers/all_data_v2.csv",
        import_schema_uri=aiplatform.schema.dataset.ioformat.image.single_label_classification,
    )

    # The second step is a model training component. It takes the dataset
    # outputted from the first step, supplies it as an input argument to the
    # component (see `dataset=ds_op.outputs["dataset"]`), and will put its
    # outputs into `training_job_run_op`.
    training_job_run_op = AutoMLImageTrainingJobRunOp(
        project=project_id,
        display_name="train-iris-automl-mbsdk-1",
        prediction_type="classification",
        model_type="CLOUD",
        dataset=ds_op.outputs["dataset"],
        model_display_name="iris-classification-model-mbsdk",
        training_fraction_split=0.6,
        validation_fraction_split=0.2,
        test_fraction_split=0.2,
        budget_milli_node_hours=8000,
    )

    # The third and fourth step are for deploying the model.
    create_endpoint_op = EndpointCreateOp(
        project=project_id,
        display_name = "create-endpoint",
    )

    model_deploy_op = ModelDeployOp(
        model=training_job_run_op.outputs["model"],
        endpoint=create_endpoint_op.outputs['endpoint'],
        automatic_resources_min_replica_count=1,
        automatic_resources_max_replica_count=1,
    )
```

We can save this as a .yaml file. This yaml file is our pipeline file. As you can see, kubeflow supports google_cloud_pipeline_components.
 
You need to install these SDKs before you begin to create the pipeline. They are not preinstalled in Vertex AI.  
