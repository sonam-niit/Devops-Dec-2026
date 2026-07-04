# Backups

- Disaster Recovery Backups are very important.
- many ways to do backups like EBS, S3 Backups, RDS backups

## EBS Snapshots

- EBS: Elastic Block Store - storage provided By EC2 
- By default when we create instance volume added to it but if you want to add extra volume to your instance that also we can manage using EBS.
- This volumes backup we can take using **SnapShots**

## Let's Create Instance to understand This.

- while creating instance we configure volume.

![Volume](images/volume.png)

- if you check volumes you can see 1 volume which is connected with this instanceID.

## Add Extra Space to this instance

- create new Volume.
- before create volume check your instance running in which zone and based on it create volume to that zone.
- create volume, give size of 16 GB 
- General Purpose Volume, then chose zone
- give tags: Name: Extra volume

- create. 

## Attach volume to instance

- select volume
- actions, attach volume to instance
- select device name like sdf (f drive)
- attach.

- once attach done check instance and see storage

![Storage Details](images/attach.png)