# Proposed updates to Cinema Specification

The current Cinema database specification was designed for simplicity, so that metadata and artifacts could be recorded in the simplest way possible.

There are very few restrictions on the database, and this means that it is up to applications to record any other information about the database (variable names, expected ranges, etc.) in an explicit specification for that application. And example of this is in the [Cinema:Bandit](https://github.com/cinemascience/cinema_bandit) application, which describes expected restrictions in the application documentation.

The Cinema community has expressed a need for a minimal set of metadata that could be included in the specification. This document is a proposal for that minimum set of information.

## Proposal

We propose to optionally include a `cinema.json` file in a Cinema database. The file includes a minimal set of useful information, and optional extensions. Thus, a proposed Cinema database would be organized in the following way:


```
    mydatabase.cdb/
        data.csv
        cinema.json
```

## The `cinema.json` file

The `cinema.json` file is a `json` file that optionally includes the following data. The file:

- must be valid `json`.
- may be empty
- may include **cinema optional fields**
- may include any other valid `json`

```
{
    "title" : "cinema database metadata specification",
    "description" : "additional data describing the cinema database",
    "type" : "object",
    "properties" : {
        "version" : {
            "type" : "string"
            "description" : "the version number of the database specification defining this database"
        },
        "data" : {
            "type" : "object",
            "description" : "information about the data contained in the database",
            "properties" : {
                "license" : {
                    "type" : "string",
                    "description" : "a string noting the type of license for the data"
                },
                "created" : {
                    "type" : "object",
                    "description" : "data associated with creation of the database",
                    "properties" : {
                        "date" : {
                            "type" : "string",
                            "format" : "date-time"
                        },
                        "created-by" : {
                            "type" : "object",
                            "description" : "the person who created the database"
                            "properties" : {
                                "name" : {
                                    "type" : "string",
                                    "description" : "name of person who created this database"
                                },
                                "email" : {
                                    "type" : "string",
                                    "description" : "the email address for the named person",
                                    "format" : "email"
                                }
                            }
                        },
                        "application" : {
                            "type" : "object",
                            "description" : "the application which created the database"
                            "properties" : {
                                "name" : {
                                    "type" : "string",
                                    "description" : "name of person who created this database"
                                },
                                "version" : {
                                    "type" : "string",
                                    "description" : "the version of the application"
                                }
                            }
                        },
                    }
                },
                "description" : {
                	"type" : "string",
                    "description" : "a description of the database creation"
                }
            }
        }
    }
}
```

```
{
    "version" : "2.1",
    "data" : {
        "license" : "not sure what these would be",
        "description" : "data created during a science run",
        "created" : {
            "date" : "2019-11-01T12:00:00+00:00",
            "created-by" : {
                "name" : "David H. Rogers",
                "email" : "dhr@lanl.gov"
            },
            "application: " : {
                "name" : "foo",
                "version" : "1.0.62"
            }
        }
    }
}
```
 



