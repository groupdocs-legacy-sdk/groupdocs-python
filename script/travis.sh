#!/bin/sh -ex

# integration tests
cd tests/samples-ui-tests
mvn -q -s settings.xml clean test
