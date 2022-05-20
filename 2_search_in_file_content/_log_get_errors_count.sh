#!/bin/bash

if [[ "$1" ]]; then
	filepath=$1
	echo  ----------------------
	echo 	$filepath
	echo  ----------------------
	
	fieldList=("source title doi license description publish_time authors journal keywords url type")
	
	total=$(grep -c "" $filepath)
	echo "Total: $total"
	
	dataerror=$(grep -c DataError $filepath)
	echo "DataError: $dataerror"

	attributeerror=$(grep -c AttributeError $filepath)
	echo "AttributeError: $attributeerror"

	integrityerror=$(grep -c IntegrityError $filepath)
	echo "IntegrityError: $integrityerror"
	
	validationerror=$(grep -c ValidationError $filepath)
	echo "ValidationError: $validationerror"
	
	for field in $fieldList
	do
	fielderror=$(grep -c $field $filepath)
	echo "   $field: $fielderror"
	done
	
	nonfielderror=$(grep -c non_field_errors $filepath)
	echo "   non_field_errors: $nonfielderror"
else
	echo set log file
fi
