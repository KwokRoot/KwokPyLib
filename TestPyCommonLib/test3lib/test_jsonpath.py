import jsonpath


# 模拟数据：来源 Elasticsearch 聚合结果。
json_data = {
  "aggregations": {
    "bucket1": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets":
      [
        {
          "key": "JD1",
          "doc_count": 100,
          "bucket2": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets":
            [
              {
                "key": "10.10.86.101",
                "doc_count": 30,
                "bucket3": {
                  "doc_count_error_upper_bound": 0,
                  "sum_other_doc_count": 0,
                  "buckets":
                  [
                    {
                      "key": "SH",
                      "doc_count": 30
                    }
                  ]
                }
              },
              {
                "key": "10.10.86.103",
                "doc_count": 40,
                "bucket3": {
                  "doc_count_error_upper_bound": 0,
                  "sum_other_doc_count": 0,
                  "buckets":
                  [
                    {
                      "key": "SZ1",
                      "doc_count": 10
                    },
                    {
                      "key": "SZ2",
                      "doc_count": 30
                    }
                  ]
                }
              },
              {
                "key": "10.10.86.106",
                "doc_count": 30,
                "bucket3": {
                  "doc_count_error_upper_bound": 0,
                  "sum_other_doc_count": 0,
                  "buckets":
                  [
                    {
                      "key": "BJ",
                      "doc_count": 30
                    }
                  ]
                }
              }
            ]
          }
        }
      ]
    }
  }
}

# jsonpath 常用于解析层级较深的多层嵌套 json 数据。
print(jsonpath.jsonpath(json_data, "$..bucket3.buckets[*].key"))

