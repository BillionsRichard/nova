# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from oslo_config import cfg

quota_group = cfg.OptGroup(
    name='quota',
    title='Quota Options',
    help="""
Quota options allow to manage quotas in openstack deployment.
""")

quota_opts = [
    cfg.IntOpt('instances',
        min=-1,
        default=10,
        deprecated_group='DEFAULT',
        deprecated_name='quota_instances',
        help="""
The number of instances allowed per project.

Possible Values

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('cores',
        min=-1,
        default=20,
        deprecated_group='DEFAULT',
        deprecated_name='quota_cores',
        help="""
The number of instance cores or vCPUs allowed per project.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('ram',
        min=-1,
        default=50 * 1024,
        deprecated_group='DEFAULT',
        deprecated_name='quota_ram',
        help="""
The number of megabytes of instance RAM allowed per project.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('floating_ips',
        min=-1,
        default=10,
        deprecated_group='DEFAULT',
        deprecated_name='quota_floating_ips',
        deprecated_for_removal=True,
        deprecated_since='15.0.0',
        deprecated_reason="""
nova-network is deprecated, as are any related configuration options.
""",
        help="""
The number of floating IPs allowed per project.

Floating IPs are not allocated to instances by default. Users need to select
them from the pool configured by the OpenStack administrator to attach to their
instances.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('fixed_ips',
        min=-1,
        default=-1,
        deprecated_group='DEFAULT',
        deprecated_name='quota_fixed_ips',
        deprecated_for_removal=True,
        deprecated_since='15.0.0',
        deprecated_reason="""
nova-network is deprecated, as are any related configuration options.
""",
        help="""
The number of fixed IPs allowed per project.

Unlike floating IPs, fixed IPs are allocated dynamically by the network
component when instances boot up.  This quota value should be at least the
number of instances allowed

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('metadata_items',
        min=-1,
        default=128,
        deprecated_group='DEFAULT',
        deprecated_name='quota_metadata_items',
        help="""
The number of metadata items allowed per instance.

Users can associate metadata with an instance during instance creation. This
metadata takes the form of key-value pairs.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('injected_files',
        min=-1,
        default=5,
        deprecated_group='DEFAULT',
        deprecated_name='quota_injected_files',
        help="""
The number of injected files allowed.

File injection allows users to customize the personality of an instance by
injecting data into it upon boot. Only text file injection is permitted: binary
or ZIP files are not accepted. During file injection, any existing files that
match specified files are renamed to include ``.bak`` extension appended with a
timestamp.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('injected_file_content_bytes',
        min=-1,
        default=10 * 1024,
        deprecated_group='DEFAULT',
        deprecated_name='quota_injected_file_content_bytes',
        help="""
The number of bytes allowed per injected file.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('injected_file_path_length',
        min=-1,
        default=255,
        deprecated_group='DEFAULT',
        deprecated_name='quota_injected_file_path_length',
        help="""
The maximum allowed injected file path length.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('security_groups',
        min=-1,
        default=10,
        deprecated_group='DEFAULT',
        deprecated_name='quota_security_groups',
        deprecated_for_removal=True,
        deprecated_since='15.0.0',
        deprecated_reason="""
nova-network is deprecated, as are any related configuration options.
""",
        help="""
The number of security groups per project.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('security_group_rules',
        min=-1,
        default=20,
        deprecated_group='DEFAULT',
        deprecated_name='quota_security_group_rules',
        deprecated_for_removal=True,
        deprecated_since='15.0.0',
        deprecated_reason="""
nova-network is deprecated, as are any related configuration options.
""",
        help="""
The number of security rules per security group.

The associated rules in each security group control the traffic to instances in
the group.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('key_pairs',
        min=-1,
        default=100,
        deprecated_group='DEFAULT',
        deprecated_name='quota_key_pairs',
        help="""
The maximum number of key pairs allowed per user.

Users can create at least one key pair for each project and use the key pair
for multiple instances that belong to that project.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('server_groups',
        min=-1,
        default=10,
        deprecated_group='DEFAULT',
        deprecated_name='quota_server_groups',
        help="""
The maxiumum number of server groups per project.

Server groups are used to control the affinity and anti-affinity scheduling
policy for a group of servers or instances. Reducing the quota will not affect
any existing group, but new servers will not be allowed into groups that have
become over quota.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    cfg.IntOpt('server_group_members',
        min=-1,
        default=10,
        deprecated_group='DEFAULT',
        deprecated_name='quota_server_group_members',
        help="""
The maximum number of servers per server group.

Possible values:

* A positive integer or 0.
* -1 to disable the quota.
"""),
    # TODO(stephenfin): This should have a min parameter
    cfg.IntOpt('reservation_expire',
        default=86400,
        deprecated_group='DEFAULT',
        help="""
The number of seconds until a reservation expires.

This quota represents the time period for invalidating quota reservations.
"""),
    cfg.IntOpt('until_refresh',
        min=0,
        default=0,
        deprecated_group='DEFAULT',
        help="""
The count of reservations until usage is refreshed.

This defaults to 0 (off) to avoid additional load but it is useful to turn on
to help keep quota usage up-to-date and reduce the impact of out of sync usage
issues.
"""),
    cfg.IntOpt('max_age',
        min=0,
        default=0,
        deprecated_group='DEFAULT',
        help="""
The number of seconds between subsequent usage refreshes.

This defaults to 0 (off) to avoid additional load but it is useful to turn on
to help keep quota usage up-to-date and reduce the impact of out of sync usage
issues. Note that quotas are not updated on a periodic task, they will update
on a new reservation if max_age has passed since the last reservation.
"""),
# TODO(pumaranikar): Add a new config to select between the db_driver and
# the no_op driver using stevedore.
    cfg.StrOpt('driver',
        default='nova.quota.DbQuotaDriver',
        deprecated_for_removal=True,
        deprecated_since='14.0.0',
        deprecated_group='DEFAULT',
        deprecated_name='quota_driver',
        help="""
The quota enforcer driver.

Provides abstraction for quota checks. Users can configure a specific
driver to use for quota checks.

Possible values:

* nova.quota.DbQuotaDriver (default) or any string representing fully
  qualified class name.
"""),
    cfg.BoolOpt('recheck_quota',
        default=True,
        help="""
Recheck quota after resource creation to prevent allowing quota to be exceeded.

This defaults to True (recheck quota after resource creation) but can be set to
False to avoid additional load if allowing quota to be exceeded because of
racing requests is considered acceptable. For example, when set to False, if a
user makes highly parallel REST API requests to create servers, it will be
possible for them to create more servers than their allowed quota during the
race. If their quota is 10 servers, they might be able to create 50 during the
burst. After the burst, they will not be able to create any more servers but
they will be able to keep their 50 servers until they delete them.

The initial quota check is done before resources are created, so if multiple
parallel requests arrive at the same time, all could pass the quota check and
create resources, potentially exceeding quota. When recheck_quota is True,
quota will be checked a second time after resources have been created and if
the resource is over quota, it will be deleted and OverQuota will be raised,
usually resulting in a 403 response to the REST API user. This makes it
impossible for a user to exceed their quota with the caveat that it will,
however, be possible for a REST API user to be rejected with a 403 response in
the event of a collision close to reaching their quota limit, even if the user
has enough quota available when they made the request.
"""),
]


def register_opts(conf):
    conf.register_group(quota_group)
    conf.register_opts(quota_opts, group=quota_group)


def list_opts():
    return {quota_group: quota_opts}
