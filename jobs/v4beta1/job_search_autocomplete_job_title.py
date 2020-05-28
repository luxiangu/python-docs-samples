# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START job_search_autocomplete_job_title]

from google.cloud import talent_v4beta1
from google.cloud.talent import enums
import six


def complete_query(project_id, tenant_id, query):
    """Complete job title given partial text (autocomplete)"""

    client = talent_v4beta1.CompletionClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # query = '[partially typed job title]'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode("utf-8")
    if isinstance(tenant_id, six.binary_type):
        tenant_id = tenant_id.decode("utf-8")
    if isinstance(query, six.binary_type):
        query = query.decode("utf-8")

    parent = client.tenant_path(project_id, tenant_id)

    response = client.complete_query(
        parent,
        query,
        page_size=5,  # limit for number of results
        language_codes=["en-US"],  # language code
    )
    for result in response.completion_results:
        print("Suggested title: {}".format(result.suggestion))
        # Suggestion type is JOB_TITLE or COMPANY_TITLE
        print(
            "Suggestion type: {}".format(
                enums.CompleteQueryRequest.CompletionType(result.type).name
            )
        )


# [END job_search_autocomplete_job_title]
