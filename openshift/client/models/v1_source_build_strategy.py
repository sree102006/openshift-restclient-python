# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1SourceBuildStrategy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, env=None, force_pull=None, _from=None, incremental=None, pull_secret=None, runtime_artifacts=None, runtime_image=None, scripts=None):
        """
        V1SourceBuildStrategy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'env': 'list[V1EnvVar]',
            'force_pull': 'bool',
            '_from': 'V1ObjectReference',
            'incremental': 'bool',
            'pull_secret': 'V1LocalObjectReference',
            'runtime_artifacts': 'list[V1ImageSourcePath]',
            'runtime_image': 'V1ObjectReference',
            'scripts': 'str'
        }

        self.attribute_map = {
            'env': 'env',
            'force_pull': 'forcePull',
            '_from': 'from',
            'incremental': 'incremental',
            'pull_secret': 'pullSecret',
            'runtime_artifacts': 'runtimeArtifacts',
            'runtime_image': 'runtimeImage',
            'scripts': 'scripts'
        }

        self._env = env
        self._force_pull = force_pull
        self.__from = _from
        self._incremental = incremental
        self._pull_secret = pull_secret
        self._runtime_artifacts = runtime_artifacts
        self._runtime_image = runtime_image
        self._scripts = scripts

    @property
    def env(self):
        """
        Gets the env of this V1SourceBuildStrategy.
        env contains additional environment variables you want to pass into a builder container.

        :return: The env of this V1SourceBuildStrategy.
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """
        Sets the env of this V1SourceBuildStrategy.
        env contains additional environment variables you want to pass into a builder container.

        :param env: The env of this V1SourceBuildStrategy.
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def force_pull(self):
        """
        Gets the force_pull of this V1SourceBuildStrategy.
        forcePull describes if the builder should pull the images from registry prior to building.

        :return: The force_pull of this V1SourceBuildStrategy.
        :rtype: bool
        """
        return self._force_pull

    @force_pull.setter
    def force_pull(self, force_pull):
        """
        Sets the force_pull of this V1SourceBuildStrategy.
        forcePull describes if the builder should pull the images from registry prior to building.

        :param force_pull: The force_pull of this V1SourceBuildStrategy.
        :type: bool
        """

        self._force_pull = force_pull

    @property
    def _from(self):
        """
        Gets the _from of this V1SourceBuildStrategy.
        from is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled

        :return: The _from of this V1SourceBuildStrategy.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1SourceBuildStrategy.
        from is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled

        :param _from: The _from of this V1SourceBuildStrategy.
        :type: V1ObjectReference
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")

        self.__from = _from

    @property
    def incremental(self):
        """
        Gets the incremental of this V1SourceBuildStrategy.
        incremental flag forces the Source build to do incremental builds if true.

        :return: The incremental of this V1SourceBuildStrategy.
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        """
        Sets the incremental of this V1SourceBuildStrategy.
        incremental flag forces the Source build to do incremental builds if true.

        :param incremental: The incremental of this V1SourceBuildStrategy.
        :type: bool
        """

        self._incremental = incremental

    @property
    def pull_secret(self):
        """
        Gets the pull_secret of this V1SourceBuildStrategy.
        pullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries

        :return: The pull_secret of this V1SourceBuildStrategy.
        :rtype: V1LocalObjectReference
        """
        return self._pull_secret

    @pull_secret.setter
    def pull_secret(self, pull_secret):
        """
        Sets the pull_secret of this V1SourceBuildStrategy.
        pullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries

        :param pull_secret: The pull_secret of this V1SourceBuildStrategy.
        :type: V1LocalObjectReference
        """

        self._pull_secret = pull_secret

    @property
    def runtime_artifacts(self):
        """
        Gets the runtime_artifacts of this V1SourceBuildStrategy.
        runtimeArtifacts specifies a list of source/destination pairs that will be copied from the builder to the runtime image. sourcePath can be a file or directory. destinationDir must be a directory. destinationDir can also be empty or equal to \".\", in this case it just refers to the root of WORKDIR. Deprecated: This feature will be removed in a future release. Use ImageSource to copy binary artifacts created from one build into a separate runtime image.

        :return: The runtime_artifacts of this V1SourceBuildStrategy.
        :rtype: list[V1ImageSourcePath]
        """
        return self._runtime_artifacts

    @runtime_artifacts.setter
    def runtime_artifacts(self, runtime_artifacts):
        """
        Sets the runtime_artifacts of this V1SourceBuildStrategy.
        runtimeArtifacts specifies a list of source/destination pairs that will be copied from the builder to the runtime image. sourcePath can be a file or directory. destinationDir must be a directory. destinationDir can also be empty or equal to \".\", in this case it just refers to the root of WORKDIR. Deprecated: This feature will be removed in a future release. Use ImageSource to copy binary artifacts created from one build into a separate runtime image.

        :param runtime_artifacts: The runtime_artifacts of this V1SourceBuildStrategy.
        :type: list[V1ImageSourcePath]
        """

        self._runtime_artifacts = runtime_artifacts

    @property
    def runtime_image(self):
        """
        Gets the runtime_image of this V1SourceBuildStrategy.
        runtimeImage is an optional image that is used to run an application without unneeded dependencies installed. The building of the application is still done in the builder image but, post build, you can copy the needed artifacts in the runtime image for use. Deprecated: This feature will be removed in a future release. Use ImageSource to copy binary artifacts created from one build into a separate runtime image.

        :return: The runtime_image of this V1SourceBuildStrategy.
        :rtype: V1ObjectReference
        """
        return self._runtime_image

    @runtime_image.setter
    def runtime_image(self, runtime_image):
        """
        Sets the runtime_image of this V1SourceBuildStrategy.
        runtimeImage is an optional image that is used to run an application without unneeded dependencies installed. The building of the application is still done in the builder image but, post build, you can copy the needed artifacts in the runtime image for use. Deprecated: This feature will be removed in a future release. Use ImageSource to copy binary artifacts created from one build into a separate runtime image.

        :param runtime_image: The runtime_image of this V1SourceBuildStrategy.
        :type: V1ObjectReference
        """

        self._runtime_image = runtime_image

    @property
    def scripts(self):
        """
        Gets the scripts of this V1SourceBuildStrategy.
        scripts is the location of Source scripts

        :return: The scripts of this V1SourceBuildStrategy.
        :rtype: str
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        """
        Sets the scripts of this V1SourceBuildStrategy.
        scripts is the location of Source scripts

        :param scripts: The scripts of this V1SourceBuildStrategy.
        :type: str
        """

        self._scripts = scripts

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1SourceBuildStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
