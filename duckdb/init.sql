install uc_catalog from core_nightly;
load uc_catalog;
install delta;
load delta;

CREATE SECRET (
    TYPE UC,
    TOKEN 'not-used',
    ENDPOINT 'http://127.0.0.1:8080',
    AWS_REGION 'us-east-2'
);

ATTACH 'unity' AS unity (TYPE UC_CATALOG);

select * from unity.default.test;
