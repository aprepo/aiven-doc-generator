Service type: cassandra
-----------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``cassandra``
    - object
    - cassandra configuration values 
  * - ``migrate_sstableloader``
    - boolean
    - Migration mode for the sstableloader utility Sets the service into migration mode enabling the sstableloader utility to be used to upload Cassandra data files. Available only on service create.
  * - ``cassandra_version``
    - ['string', 'null']
    - Cassandra major version 
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``service_to_fork_from``
    - ['string', 'null']
    - Name of another service to fork from. This has effect only when a new service is being created. 
  * - ``project_to_fork_from``
    - ['string', 'null']
    - Name of another project to fork a service from. This has effect only when a new service is being created. 

Service type: elasticsearch
---------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``elasticsearch_version``
    - ['string', 'null']
    - Elasticsearch major version 
  * - ``opensearch_version``
    - ['string', 'null']
    - OpenSearch major version 
  * - ``disable_replication_factor_adjustment``
    - ['boolean', 'null']
    - Disable replication factor adjustment DEPRECATED: Disable automatic replication factor adjustment for multi-node services. By default, Aiven ensures all indexes are replicated at least to two nodes. Note: Due to potential data loss in case of losing a service node, this setting can no longer be activated.
  * - ``custom_domain``
    - ['string', 'null']
    - Custom domain Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``index_patterns``
    - array
    - Index patterns 
  * - ``max_index_count``
    - integer
    - Maximum index count Maximum number of indexes to keep before deleting the oldest one
  * - ``keep_index_refresh_interval``
    - boolean
    - Don't reset index.refresh_interval to the default value Aiven automation resets index.refresh_interval to default value for every index to be sure that indices are always visible to search. If it doesn't fit your case, you can disable this by setting up this flag to true.
  * - ``kibana``
    - object
    - Kibana settings 
  * - ``elasticsearch``
    - object
    - Elasticsearch settings 
  * - ``index_template``
    - object
    - Template settings for all new indexes 
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``privatelink_access``
    - object
    - Allow access to selected service components through Privatelink 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``recovery_basebackup_name``
    - string
    - Name of the basebackup to restore in forked service 
  * - ``service_to_fork_from``
    - ['string', 'null']
    - Name of another service to fork from. This has effect only when a new service is being created. 
  * - ``project_to_fork_from``
    - ['string', 'null']
    - Name of another project to fork a service from. This has effect only when a new service is being created. 

Service type: grafana
---------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``custom_domain``
    - ['string', 'null']
    - Custom domain Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``external_image_storage``
    - object
    - External image store settings 
  * - ``smtp_server``
    - object
    - SMTP server settings 
  * - ``auth_basic_enabled``
    - boolean
    - Enable or disable basic authentication form, used by Grafana built-in login 
  * - ``auth_generic_oauth``
    - object
    - Generic OAuth integration 
  * - ``auth_google``
    - object
    - Google Auth integration 
  * - ``auth_github``
    - object
    - Github Auth integration 
  * - ``auth_gitlab``
    - object
    - GitLab Auth integration 
  * - ``auth_azuread``
    - object
    - Azure AD OAuth integration 
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``privatelink_access``
    - object
    - Allow access to selected service components through Privatelink 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``recovery_basebackup_name``
    - string
    - Name of the basebackup to restore in forked service 
  * - ``service_to_fork_from``
    - ['string', 'null']
    - Name of another service to fork from. This has effect only when a new service is being created. 
  * - ``project_to_fork_from``
    - ['string', 'null']
    - Name of another project to fork a service from. This has effect only when a new service is being created. 
  * - ``user_auto_assign_org``
    - boolean
    - Auto-assign new users on signup to main organization. Defaults to false 
  * - ``user_auto_assign_org_role``
    - string
    - Set role for new signups. Defaults to Viewer 
  * - ``google_analytics_ua_id``
    - string
    - Google Analytics ID 
  * - ``metrics_enabled``
    - boolean
    - Enable Grafana /metrics endpoint 
  * - ``cookie_samesite``
    - string
    - Cookie SameSite attribute: 'strict' prevents sending cookie for cross-site requests, effectively disabling direct linking from other sites to Grafana. 'lax' is the default value. 
  * - ``alerting_error_or_timeout``
    - string
    - Default error or timeout setting for new alerting rules 
  * - ``alerting_nodata_or_nullvalues``
    - string
    - Default value for 'no data or null values' for new alerting rules 
  * - ``alerting_enabled``
    - boolean
    - Enable or disable Grafana alerting functionality 
  * - ``alerting_max_annotations_to_keep``
    - integer
    - Max number of alert annotations that Grafana stores. 0 (default) keeps all alert annotations. 
  * - ``dashboards_min_refresh_interval``
    - string
    - Minimum refresh interval Signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s, 1h
  * - ``dashboards_versions_to_keep``
    - integer
    - Dashboard versions to keep per dashboard 
  * - ``dataproxy_timeout``
    - integer
    - Timeout for data proxy requests in seconds 
  * - ``dataproxy_send_user_header``
    - boolean
    - Send 'X-Grafana-User' header to data source 
  * - ``viewers_can_edit``
    - boolean
    - Users with view-only permission can edit but not save dashboards 
  * - ``editors_can_admin``
    - boolean
    - Editors can manage folders, teams and dashboards created by them 
  * - ``disable_gravatar``
    - boolean
    - Set to true to disable gravatar. Defaults to false (gravatar is enabled) 
  * - ``allow_embedding``
    - boolean
    - Allow embedding Grafana dashboards with iframe/frame/object/embed tags. Disabled by default to limit impact of clickjacking 
  * - ``date_formats``
    - object
    - Grafana date format specifications 

Service type: influxdb
----------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``custom_domain``
    - ['string', 'null']
    - Custom domain Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``privatelink_access``
    - object
    - Allow access to selected service components through Privatelink 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``recovery_basebackup_name``
    - string
    - Name of the basebackup to restore in forked service 
  * - ``influxdb``
    - object
    - influxdb.conf configuration values 
  * - ``service_to_fork_from``
    - ['string', 'null']
    - Name of another service to fork from. This has effect only when a new service is being created. 
  * - ``project_to_fork_from``
    - ['string', 'null']
    - Name of another project to fork a service from. This has effect only when a new service is being created. 

Service type: kafka
-------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``custom_domain``
    - ['string', 'null']
    - Custom domain Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``privatelink_access``
    - object
    - Allow access to selected service components through Privatelink 
  * - ``kafka``
    - object
    - Kafka broker configuration values 
  * - ``kafka_authentication_methods``
    - object
    - Kafka authentication methods 
  * - ``kafka_connect``
    - boolean
    - Enable Kafka Connect service 
  * - ``kafka_connect_config``
    - object
    - Kafka Connect configuration values 
  * - ``kafka_rest``
    - boolean
    - Enable Kafka-REST service 
  * - ``kafka_version``
    - ['string', 'null']
    - Kafka major version 
  * - ``schema_registry``
    - boolean
    - Enable Schema-Registry service 
  * - ``kafka_rest_config``
    - object
    - Kafka REST configuration 
  * - ``schema_registry_config``
    - object
    - Schema Registry configuration 

Service type: kafka_connect
---------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``kafka_connect``
    - object
    - Kafka Connect configuration values 
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``privatelink_access``
    - object
    - Allow access to selected service components through Privatelink 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 

Service type: kafka_mirrormaker
-------------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``kafka_mirrormaker``
    - object
    - Kafka MirrorMaker configuration values 

Service type: m3db
------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``custom_domain``
    - ['string', 'null']
    - Custom domain Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``limits``
    - object
    - M3 limits 
  * - ``m3coordinator_enable_graphite_carbon_ingest``
    - boolean
    - Enable Graphite ingestion using Carbon plaintext protocol Enables access to Graphite Carbon plaintext metrics ingestion. It can be enabled only for services inside VPCs. The metrics are written to aggregated namespaces only.
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``m3_version``
    - ['string', 'null']
    - M3 major version (deprecated, use m3db_version) 
  * - ``m3db_version``
    - ['string', 'null']
    - M3 major version (the minimum compatible version) 
  * - ``namespaces``
    - array
    - List of M3 namespaces 
  * - ``rules``
    - object
    - M3 rules 
  * - ``service_to_fork_from``
    - ['string', 'null']
    - Name of another service to fork from. This has effect only when a new service is being created. 
  * - ``project_to_fork_from``
    - ['string', 'null']
    - Name of another project to fork a service from. This has effect only when a new service is being created. 

Service type: m3aggregator
--------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``custom_domain``
    - ['string', 'null']
    - Custom domain Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``m3_version``
    - ['string', 'null']
    - M3 major version (deprecated, use m3aggregator_version) 
  * - ``m3aggregator_version``
    - ['string', 'null']
    - M3 major version (the minimum compatible version) 

Service type: mysql
-------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``admin_username``
    - ['string', 'null']
    - Custom username for admin user. This must be set only when a new service is being created. 
  * - ``admin_password``
    - ['string', 'null']
    - Custom password for admin user. Defaults to random string. This must be set only when a new service is being created. 
  * - ``backup_hour``
    - ['integer', 'null']
    - The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed. 
  * - ``backup_minute``
    - ['integer', 'null']
    - The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed. 
  * - ``migration``
    - ['object', 'null']
    - Migrate data from existing server 
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``privatelink_access``
    - object
    - Allow access to selected service components through Privatelink 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``service_to_fork_from``
    - ['string', 'null']
    - Name of another service to fork from. This has effect only when a new service is being created. 
  * - ``project_to_fork_from``
    - ['string', 'null']
    - Name of another project to fork a service from. This has effect only when a new service is being created. 
  * - ``mysql_version``
    - ['string', 'null']
    - MySQL major version 
  * - ``recovery_target_time``
    - ['string', 'null']
    - Recovery target time when forking a service. This has effect only when a new service is being created. 
  * - ``binlog_retention_period``
    - integer
    - The minimum amount of time in seconds to keep binlog entries before deletion. This may be extended for services that require binlog entries for longer than the default for example if using the MySQL Debezium Kafka connector. 
  * - ``mysql``
    - object
    - mysql.conf configuration values 

Service type: opensearch
------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``opensearch_version``
    - ['string', 'null']
    - OpenSearch major version 
  * - ``disable_replication_factor_adjustment``
    - ['boolean', 'null']
    - Disable replication factor adjustment DEPRECATED: Disable automatic replication factor adjustment for multi-node services. By default, Aiven ensures all indexes are replicated at least to two nodes. Note: Due to potential data loss in case of losing a service node, this setting can no longer be activated.
  * - ``custom_domain``
    - ['string', 'null']
    - Custom domain Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``index_patterns``
    - array
    - Index patterns 
  * - ``max_index_count``
    - integer
    - Maximum index count Maximum number of indexes to keep before deleting the oldest one
  * - ``keep_index_refresh_interval``
    - boolean
    - Don't reset index.refresh_interval to the default value Aiven automation resets index.refresh_interval to default value for every index to be sure that indices are always visible to search. If it doesn't fit your case, you can disable this by setting up this flag to true.
  * - ``opensearch_dashboards``
    - object
    - OpenSearch Dashboards settings 
  * - ``opensearch``
    - object
    - OpenSearch settings 
  * - ``index_template``
    - object
    - Template settings for all new indexes 
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``privatelink_access``
    - object
    - Allow access to selected service components through Privatelink 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``recovery_basebackup_name``
    - string
    - Name of the basebackup to restore in forked service 
  * - ``service_to_fork_from``
    - ['string', 'null']
    - Name of another service to fork from. This has effect only when a new service is being created. 
  * - ``project_to_fork_from``
    - ['string', 'null']
    - Name of another project to fork a service from. This has effect only when a new service is being created. 

Service type: pg
----------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``migration``
    - ['object', 'null']
    - Migrate data from existing server 
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``admin_username``
    - ['string', 'null']
    - Custom username for admin user. This must be set only when a new service is being created. 
  * - ``admin_password``
    - ['string', 'null']
    - Custom password for admin user. Defaults to random string. This must be set only when a new service is being created. 
  * - ``backup_hour``
    - ['integer', 'null']
    - The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed. 
  * - ``backup_minute``
    - ['integer', 'null']
    - The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed. 
  * - ``pglookout``
    - object
    - PGLookout settings 
  * - ``pg_service_to_fork_from``
    - ['string', 'null']
    - Name of the PG Service from which to fork (deprecated, use service_to_fork_from). This has effect only when a new service is being created. 
  * - ``service_to_fork_from``
    - ['string', 'null']
    - Name of another service to fork from. This has effect only when a new service is being created. 
  * - ``project_to_fork_from``
    - ['string', 'null']
    - Name of another project to fork a service from. This has effect only when a new service is being created. 
  * - ``synchronous_replication``
    - string
    - Synchronous replication type. Note that the service plan also needs to support synchronous replication. 
  * - ``pg_read_replica``
    - ['boolean', 'null']
    - Should the service which is being forked be a read replica This setting is deprecated. Use read-replica service integration instead.
  * - ``pg_version``
    - ['string', 'null']
    - PostgreSQL major version 
  * - ``pgbouncer``
    - object
    - PGBouncer connection pooling settings 
  * - ``recovery_target_time``
    - ['string', 'null']
    - Recovery target time when forking a service. This has effect only when a new service is being created. 
  * - ``variant``
    - ['string', 'null']
    - Variant of the PostgreSQL service, may affect the features that are exposed by default 
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``privatelink_access``
    - object
    - Allow access to selected service components through Privatelink 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``pg``
    - object
    - postgresql.conf configuration values 
  * - ``shared_buffers_percentage``
    - number
    - shared_buffers_percentage Percentage of total RAM that the database server uses for shared memory buffers. Valid range is 20-60 (float), which corresponds to 20% - 60%. This setting adjusts the shared_buffers configuration value.
  * - ``timescaledb``
    - object
    - TimescaleDB extension configuration values 
  * - ``work_mem``
    - integer
    - work_mem Sets the maximum amount of memory to be used by a query operation (such as a sort or hash table) before writing to temporary disk files, in MB. Default is 1MB + 0.075% of total RAM (up to 32MB).

Service type: redis
-------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``migration``
    - ['object', 'null']
    - Migrate data from existing server 
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``privatelink_access``
    - object
    - Allow access to selected service components through Privatelink 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``recovery_basebackup_name``
    - string
    - Name of the basebackup to restore in forked service 
  * - ``redis_maxmemory_policy``
    - ['string', 'null']
    - Redis maxmemory-policy 
  * - ``redis_pubsub_client_output_buffer_limit``
    - integer
    - Pub/sub client output buffer hard limit in MB Set output buffer limit for pub / sub clients in MB. The value is the hard limit, the soft limit is 1/4 of the hard limit. When setting the limit, be mindful of the available memory in the selected service plan.
  * - ``redis_number_of_databases``
    - integer
    - Number of redis databases Set number of redis databases. Changing this will cause a restart of redis service.
  * - ``redis_io_threads``
    - integer
    - Redis IO thread count 
  * - ``redis_lfu_log_factor``
    - integer
    - Counter logarithm factor for volatile-lfu and allkeys-lfu maxmemory-policies 
  * - ``redis_lfu_decay_time``
    - integer
    - LFU maxmemory-policy counter decay time in minutes 
  * - ``redis_ssl``
    - boolean
    - Require SSL to access Redis 
  * - ``redis_timeout``
    - integer
    - Redis idle connection timeout 
  * - ``redis_notify_keyspace_events``
    - string
    - Set notify-keyspace-events option 
  * - ``redis_persistence``
    - string
    - Redis persistence When persistence is 'rdb', Redis does RDB dumps each 10 minutes if any key is changed. Also RDB dumps are done according to backup schedule for backup purposes. When persistence is 'off', no RDB dumps and backups are done, so data can be lost at any moment if service is restarted for any reason, or if service is powered off. Also service can't be forked.
  * - ``redis_acl_channels_default``
    - string
    - Default ACL for pub/sub channels used when Redis user is created Determines default pub/sub channels' ACL for new users if ACL is not supplied. When this option is not defined, all_channels is assumed to keep backward compatibility. This option doesn't affect Redis configuration acl-pubsub-default.
  * - ``service_to_fork_from``
    - ['string', 'null']
    - Name of another service to fork from. This has effect only when a new service is being created. 
  * - ``project_to_fork_from``
    - ['string', 'null']
    - Name of another project to fork a service from. This has effect only when a new service is being created. 

