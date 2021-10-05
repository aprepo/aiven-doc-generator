Service type: cassandra
-----------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``cassandra configuration values``
    - object
    - 
  * - ``Migration mode for the sstableloader utility``
    - boolean
    - Sets the service into migration mode enabling the sstableloader utility to be used to upload Cassandra data files. Available only on service create.
  * - ``Cassandra major version``
    - ['string', 'null']
    - 
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 
  * - ``Name of another service to fork from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Name of another project to fork a service from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 

Service type: elasticsearch
---------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``Elasticsearch major version``
    - ['string', 'null']
    - 
  * - ``OpenSearch major version``
    - ['string', 'null']
    - 
  * - ``Disable replication factor adjustment``
    - ['boolean', 'null']
    - DEPRECATED: Disable automatic replication factor adjustment for multi-node services. By default, Aiven ensures all indexes are replicated at least to two nodes. Note: Due to potential data loss in case of losing a service node, this setting can no longer be activated.
  * - ``Custom domain``
    - ['string', 'null']
    - Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``Index patterns``
    - array
    - 
  * - ``Maximum index count``
    - integer
    - Maximum number of indexes to keep before deleting the oldest one
  * - ``Don't reset index.refresh_interval to the default value``
    - boolean
    - Aiven automation resets index.refresh_interval to default value for every index to be sure that indices are always visible to search. If it doesn't fit your case, you can disable this by setting up this flag to true.
  * - ``Kibana settings``
    - object
    - 
  * - ``Elasticsearch settings``
    - object
    - 
  * - ``Template settings for all new indexes``
    - object
    - 
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service components through Privatelink``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 
  * - ``Name of the basebackup to restore in forked service``
    - string
    - 
  * - ``Name of another service to fork from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Name of another project to fork a service from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 

Service type: grafana
---------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``Custom domain``
    - ['string', 'null']
    - Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``External image store settings``
    - object
    - 
  * - ``SMTP server settings``
    - object
    - 
  * - ``Enable or disable basic authentication form, used by Grafana built-in login``
    - boolean
    - 
  * - ``Generic OAuth integration``
    - object
    - 
  * - ``Google Auth integration``
    - object
    - 
  * - ``Github Auth integration``
    - object
    - 
  * - ``GitLab Auth integration``
    - object
    - 
  * - ``Azure AD OAuth integration``
    - object
    - 
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service components through Privatelink``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 
  * - ``Name of the basebackup to restore in forked service``
    - string
    - 
  * - ``Name of another service to fork from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Name of another project to fork a service from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Auto-assign new users on signup to main organization. Defaults to false``
    - boolean
    - 
  * - ``Set role for new signups. Defaults to Viewer``
    - string
    - 
  * - ``Google Analytics ID``
    - string
    - 
  * - ``Enable Grafana /metrics endpoint``
    - boolean
    - 
  * - ``Cookie SameSite attribute: 'strict' prevents sending cookie for cross-site requests, effectively disabling direct linking from other sites to Grafana. 'lax' is the default value.``
    - string
    - 
  * - ``Default error or timeout setting for new alerting rules``
    - string
    - 
  * - ``Default value for 'no data or null values' for new alerting rules``
    - string
    - 
  * - ``Enable or disable Grafana alerting functionality``
    - boolean
    - 
  * - ``Max number of alert annotations that Grafana stores. 0 (default) keeps all alert annotations.``
    - integer
    - 
  * - ``Minimum refresh interval``
    - string
    - Signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s, 1h
  * - ``Dashboard versions to keep per dashboard``
    - integer
    - 
  * - ``Timeout for data proxy requests in seconds``
    - integer
    - 
  * - ``Send 'X-Grafana-User' header to data source``
    - boolean
    - 
  * - ``Users with view-only permission can edit but not save dashboards``
    - boolean
    - 
  * - ``Editors can manage folders, teams and dashboards created by them``
    - boolean
    - 
  * - ``Set to true to disable gravatar. Defaults to false (gravatar is enabled)``
    - boolean
    - 
  * - ``Allow embedding Grafana dashboards with iframe/frame/object/embed tags. Disabled by default to limit impact of clickjacking``
    - boolean
    - 
  * - ``Grafana date format specifications``
    - object
    - 

Service type: influxdb
----------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``Custom domain``
    - ['string', 'null']
    - Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service components through Privatelink``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 
  * - ``Name of the basebackup to restore in forked service``
    - string
    - 
  * - ``influxdb.conf configuration values``
    - object
    - 
  * - ``Name of another service to fork from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Name of another project to fork a service from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 

Service type: kafka
-------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``Custom domain``
    - ['string', 'null']
    - Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 
  * - ``Allow access to selected service components through Privatelink``
    - object
    - 
  * - ``Kafka broker configuration values``
    - object
    - 
  * - ``Kafka authentication methods``
    - object
    - 
  * - ``Enable Kafka Connect service``
    - boolean
    - 
  * - ``Kafka Connect configuration values``
    - object
    - 
  * - ``Enable Kafka-REST service``
    - boolean
    - 
  * - ``Kafka major version``
    - ['string', 'null']
    - 
  * - ``Enable Schema-Registry service``
    - boolean
    - 
  * - ``Kafka REST configuration``
    - object
    - 
  * - ``Schema Registry configuration``
    - object
    - 

Service type: kafka_connect
---------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``Kafka Connect configuration values``
    - object
    - 
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service components through Privatelink``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 

Service type: kafka_mirrormaker
-------------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``Kafka MirrorMaker configuration values``
    - object
    - 

Service type: m3db
------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``Custom domain``
    - ['string', 'null']
    - Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``M3 limits``
    - object
    - 
  * - ``Enable Graphite ingestion using Carbon plaintext protocol``
    - boolean
    - Enables access to Graphite Carbon plaintext metrics ingestion. It can be enabled only for services inside VPCs. The metrics are written to aggregated namespaces only.
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 
  * - ``M3 major version (deprecated, use m3db_version)``
    - ['string', 'null']
    - 
  * - ``M3 major version (the minimum compatible version)``
    - ['string', 'null']
    - 
  * - ``List of M3 namespaces``
    - array
    - 
  * - ``M3 rules``
    - object
    - 
  * - ``Name of another service to fork from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Name of another project to fork a service from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 

Service type: m3aggregator
--------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``Custom domain``
    - ['string', 'null']
    - Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``M3 major version (deprecated, use m3aggregator_version)``
    - ['string', 'null']
    - 
  * - ``M3 major version (the minimum compatible version)``
    - ['string', 'null']
    - 

Service type: mysql
-------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``Custom username for admin user. This must be set only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Custom password for admin user. Defaults to random string. This must be set only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed.``
    - ['integer', 'null']
    - 
  * - ``The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed.``
    - ['integer', 'null']
    - 
  * - ``Migrate data from existing server``
    - ['object', 'null']
    - 
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service components through Privatelink``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 
  * - ``Name of another service to fork from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Name of another project to fork a service from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``MySQL major version``
    - ['string', 'null']
    - 
  * - ``Recovery target time when forking a service. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``The minimum amount of time in seconds to keep binlog entries before deletion. This may be extended for services that require binlog entries for longer than the default for example if using the MySQL Debezium Kafka connector.``
    - integer
    - 
  * - ``mysql.conf configuration values``
    - object
    - 

Service type: opensearch
------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``OpenSearch major version``
    - ['string', 'null']
    - 
  * - ``Disable replication factor adjustment``
    - ['boolean', 'null']
    - DEPRECATED: Disable automatic replication factor adjustment for multi-node services. By default, Aiven ensures all indexes are replicated at least to two nodes. Note: Due to potential data loss in case of losing a service node, this setting can no longer be activated.
  * - ``Custom domain``
    - ['string', 'null']
    - Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``Index patterns``
    - array
    - 
  * - ``Maximum index count``
    - integer
    - Maximum number of indexes to keep before deleting the oldest one
  * - ``Don't reset index.refresh_interval to the default value``
    - boolean
    - Aiven automation resets index.refresh_interval to default value for every index to be sure that indices are always visible to search. If it doesn't fit your case, you can disable this by setting up this flag to true.
  * - ``OpenSearch Dashboards settings``
    - object
    - 
  * - ``OpenSearch settings``
    - object
    - 
  * - ``Template settings for all new indexes``
    - object
    - 
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service components through Privatelink``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 
  * - ``Name of the basebackup to restore in forked service``
    - string
    - 
  * - ``Name of another service to fork from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Name of another project to fork a service from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 

Service type: pg
----------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``Migrate data from existing server``
    - ['object', 'null']
    - 
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``Custom username for admin user. This must be set only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Custom password for admin user. Defaults to random string. This must be set only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed.``
    - ['integer', 'null']
    - 
  * - ``The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed.``
    - ['integer', 'null']
    - 
  * - ``PGLookout settings``
    - object
    - 
  * - ``Name of the PG Service from which to fork (deprecated, use service_to_fork_from). This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Name of another service to fork from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Name of another project to fork a service from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Synchronous replication type. Note that the service plan also needs to support synchronous replication.``
    - string
    - 
  * - ``Should the service which is being forked be a read replica``
    - ['boolean', 'null']
    - This setting is deprecated. Use read-replica service integration instead.
  * - ``PostgreSQL major version``
    - ['string', 'null']
    - 
  * - ``PGBouncer connection pooling settings``
    - object
    - 
  * - ``Recovery target time when forking a service. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Variant of the PostgreSQL service, may affect the features that are exposed by default``
    - ['string', 'null']
    - 
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service components through Privatelink``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 
  * - ``postgresql.conf configuration values``
    - object
    - 
  * - ``shared_buffers_percentage``
    - number
    - Percentage of total RAM that the database server uses for shared memory buffers. Valid range is 20-60 (float), which corresponds to 20% - 60%. This setting adjusts the shared_buffers configuration value.
  * - ``TimescaleDB extension configuration values``
    - object
    - 
  * - ``work_mem``
    - integer
    - Sets the maximum amount of memory to be used by a query operation (such as a sort or hash table) before writing to temporary disk files, in MB. Default is 1MB + 0.075% of total RAM (up to 32MB).

Service type: redis
-------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``IP filter``
    - array
    - Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``Static IP addresses``
    - boolean
    - Use static public IP addresses
  * - ``Migrate data from existing server``
    - ['object', 'null']
    - 
  * - ``Allow access to selected service ports from private networks``
    - object
    - 
  * - ``Allow access to selected service components through Privatelink``
    - object
    - 
  * - ``Allow access to selected service ports from the public Internet``
    - object
    - 
  * - ``Name of the basebackup to restore in forked service``
    - string
    - 
  * - ``Redis maxmemory-policy``
    - ['string', 'null']
    - 
  * - ``Pub/sub client output buffer hard limit in MB``
    - integer
    - Set output buffer limit for pub / sub clients in MB. The value is the hard limit, the soft limit is 1/4 of the hard limit. When setting the limit, be mindful of the available memory in the selected service plan.
  * - ``Number of redis databases``
    - integer
    - Set number of redis databases. Changing this will cause a restart of redis service.
  * - ``Redis IO thread count``
    - integer
    - 
  * - ``Counter logarithm factor for volatile-lfu and allkeys-lfu maxmemory-policies``
    - integer
    - 
  * - ``LFU maxmemory-policy counter decay time in minutes``
    - integer
    - 
  * - ``Require SSL to access Redis``
    - boolean
    - 
  * - ``Redis idle connection timeout``
    - integer
    - 
  * - ``Set notify-keyspace-events option``
    - string
    - 
  * - ``Redis persistence``
    - string
    - When persistence is 'rdb', Redis does RDB dumps each 10 minutes if any key is changed. Also RDB dumps are done according to backup schedule for backup purposes. When persistence is 'off', no RDB dumps and backups are done, so data can be lost at any moment if service is restarted for any reason, or if service is powered off. Also service can't be forked.
  * - ``Default ACL for pub/sub channels used when Redis user is created``
    - string
    - Determines default pub/sub channels' ACL for new users if ACL is not supplied. When this option is not defined, all_channels is assumed to keep backward compatibility. This option doesn't affect Redis configuration acl-pubsub-default.
  * - ``Name of another service to fork from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 
  * - ``Name of another project to fork a service from. This has effect only when a new service is being created.``
    - ['string', 'null']
    - 

