#!/bin/sh -ex

# unit tests
phpunit
# integration tests
cd tests/ui
mvn -q -s settings.xml clean test
