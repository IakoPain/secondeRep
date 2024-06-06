$('.powermail_form').parsley({
	errorsWrapper: '',
	errorTemplate: ''
});

window.Parsley.on('field:error', function() {
	this.$element.attr( 'aria-invalid', 'true' );
	this.$element.nextAll().remove();
	if(this.$element[0]['dataset']['parsleyErrorMessage']) {
		this.$element.after( '<p class="parsley-errors-list filled" id=parsley-id-"' + this.$element[0]['dataset']['parsleyId'] + '">' + this.$element[0]['dataset']['parsleyErrorMessage'] + '</p>' );
	} else {
		this.$element.after( '<p class="parsley-errors-list filled" id=parsley-id-"' + this.$element[0]['dataset']['parsleyId'] + '">' + this.$element[0]['dataset']['parsleyRequiredMessage'] + '</p>' );
	}
});

window.Parsley.on('field:success', function() {
	this.$element.removeAttr( 'aria-invalid' );
	this.$element.nextAll().remove();
});
