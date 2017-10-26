// For django csrf key
function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		let cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			let cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
// Hide the result panel first
$('#result-panel').collapse('toggle');
$( document ).ready(function() {
	// If match completed, this signal will disable the start button.
	let matchComplete=false;

	// Reset the whole page
	$('#reset-page').click(function() {
		// Restore the start and valid button
		matchComplete=false;
		$('#LaunchSim').prop('disabled', false);
		$('#LaunchSim').button('reset');
		$('#valid').prop('disabled', false);
		$('#valid').button('reset');

		// $("#test").html("page reseted.")
		// reset the inputs
		$('#info-form').trigger('reset');
		$('#form-status').remove();
		$('#gender-text').removeClass();
		$('#exAppearenceBox').removeClass('has-error');
		$('#exPersonalityBox').removeClass('has-error');
		$('#exWealthBox').removeClass('has-error');
		$('#exAppearenceBox').removeClass('has-success');
		$('#exPersonalityBox').removeClass('has-success');
		$('#exWealthBox').removeClass('has-success');

		$('#appearenceBox').removeClass('has-success');
		$('#personalityBox').removeClass('has-success');
		$('#wealthBox').removeClass('has-success');
		$('#appearenceBox').removeClass('has-error');
		$('#personalityBox').removeClass('has-error');
		$('#wealthBox').removeClass('has-error');
		// Clear the result panel
		$('#logBox').empty();
		$('#result-panel').collapse('hide');
	});

	$('#exampleModal').on('show.bs.modal', function(event) {
		let button = $(event.relatedTarget); // Button that triggered the modal
		// Extract info from data-* attributes
		// var recipient = button.data('whatever') 
		// Check the input entries are all filled out
		$('#LaunchSim').click(function() {
			event.preventDefault();
			let isFormValid=true;
			// check the all blanks are filled
			$('input').each(function() {
				let temp=$.trim($(this).val());
				if (!temp||temp<0||temp>100) {
					$(this).parent().parent().addClass('has-error');
					isFormValid=false;
				} else {
					$(this).parent().parent().removeClass('has-error');
					// $(this).parent().addClass("has-success")
				}
			});
			if (!isFormValid) {
				alert('Numbers filled in should be in 1~100 and not blank.');
				return;
			};
			// Check gender radio button is checked
			let gender=$('input[name="inlineRadioOptions"]:checked', '#info-form').val();
			if (!gender) {
				alert('TELL ME YOUR GENDER');
				$('#gender-text').addClass('text-danger');
				return;
			} else {
				$('#gender-text').removeClass('text-danger');
				$('#gender-text').addClass('text-success');
			};
			// Retrieve the data
			let appear=$.trim($('#inputAppearence').val());
			let person=$.trim($('#inputPersonality').val());
			let wealth=$.trim($('#inputWealth').val());

			let exAppear=$.trim($('#inputExAppear').val());
			let exPerson=$.trim($('#inputExPerson').val());
			let exWealth=$.trim($('#inputExWealth').val());
			$('#appearenceBox').addClass('has-success');
			$('#personalityBox').addClass('has-success');
			$('#wealthBox').addClass('has-success');
			// Check add up to 100
			if (Number(exAppear)+Number(exPerson)+Number(exWealth)!==100) {
				$('#exAppearenceBox').addClass('has-error');
				$('#exPersonalityBox').addClass('has-error');
				$('#exWealthBox').addClass('has-error');
				isFormValid=false;
			} else {
				$('#exAppearenceBox').removeClass('has-error');
				$('#exPersonalityBox').removeClass('has-error');
				$('#exWealthBox').removeClass('has-error');
				$('#exAppearenceBox').addClass('has-success');
				$('#exPersonalityBox').addClass('has-success');
				$('#exWealthBox').addClass('has-success');

			};
			if (!isFormValid) {
				alert('The three expectation should add up to 100.');
				return;
			}

			// Start the ajax process:calling the server
			$('#LaunchSim').button('loading');
			$.ajaxSetup({
				headers: {
					'X-CSRFToken': getCookie('csrftoken'),
					"contentType": 'application/json',
				},
			});
			// Ajax request
			$.ajax({
				type: "POST",
				url: "/MMS/matching/",
				// url: form.attr("data-validate-url"),
				data: {
					'gender': gender,
					'appearence': appear,
					'personality': person,
					'wealth': wealth,
					'exAppear': exAppear,
					'exPerson': exPerson,
					'exWealth': exWealth,
				},
				dataType: 'json',
				success: function(ret) {
					console.log('ajax succeed');
					if (ret.Error) {
						$('#form-status').html(' Server Failed.');
						console.log('match failed');
						$('#logBox').empty();
						$('#ret-msg').text('There is error in the server side.');
						$('#result-panel').addClass('panel-danger');
						for (var i = 0; i <ret.result.length; i++) {
							$('#logBox').append('<li class="list-group-item text-center list-group-item-warning">'+ ret.result[i]+ '</li>');
						}
					} else {
						$('#logBox').empty();
						$('#ret-msg').text(ret.result[0]);
						$('#result-panel').addClass('panel-success');
						for (var i = 0; i <ret.result.length; i++) {
							if (i==1) {
								$('#logBox').append('<li class="list-group-item text-center list-group-item-info">'+ ret.result[i]+ '</li>');
							}
							else {
								$('#logBox').append('<li class="list-group-item text-center">'+ ret.result[i]+ '</li>');
							}
						}
					}
				},
			});
			// Update the result panel main anchor
			$('#LaunchSim').button('complete');
			$('#result-panel').collapse('show');
			// Process complete, disable the button
			matchComplete=true;
			$('#exampleModal').modal('hide');
		});

		// Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
		let modal = $(this);
		// Disable the start button from lauching another request
		if (matchComplete) {
			$('#LaunchSim').prop('disabled', true);
			modal.find('.modal-title').text('Click RESET Button for another round');
			modal.find('.modal-title').addClass('text-warning');
			// $('#form-status').html("You've found your match, click reset for another round")
		};

		// modal.find('.modal-body input').val(recipient)
	});
	// Validation Button 
	$('#valid').click(function() {
		event.preventDefault();
		$('#valid').button('loading');

		$.ajaxSetup({
			headers: {
				'X-CSRFToken': getCookie('csrftoken'),
				"contentType": 'application/json',
			},
		});
		// ajax request
		$.getJSON('/MMS/matching/', function(ret) {
			// check the result
			console.log('ajax success');
			if (ret.Error) {
				console.log('match failed');
				$('#logBox').empty();
				$('#ret-msg').text('Test Failed: Something Wrong with the Algorithm.');
				$('#result-panel').addClass('panel-danger');
			} else {
				console.log('match succeed');
				$('#logBox').empty();
				$('#ret-msg').text('Test Passed, Click to see detailed log (Specifically the first and last player)');
				$('#result-panel').addClass('panel-success');
			}
			// update the result panel
			for (let i = 0; i <ret.result.length; i++) {
				$('#logBox').append('<li class="list-group-item text-center">'+ ret.result[i]+ '</li>');
			}
			// Update the list result
			console.log(ret.ErrMsg);
			switch (ret.ErrMsg) {
				case '01':
					$('#logBox li:eq(0)').addClass('list-group-item-danger');
					$('#logBox li:eq(-4)').addClass('list-group-item-success');
					break;
				case '10':
					$('#logBox li:eq(0)').addClass('list-group-item-success');
					$('#logBox li:eq(-4)').addClass('list-group-item-danger');
					break;
				case '00':
					$('#logBox li:eq(0)').addClass('list-group-item-danger');
					$('#logBox li:eq(-4)').addClass('list-group-item-danger');
					break;
				default:
					$('#logBox li:eq(0)').addClass('list-group-item-success');
					$('#logBox li:eq(-4)').addClass('list-group-item-success');
			};
			$('#result-panel').collapse('show');
			$('#valid').button('complete');
		});
		$('#valid').prop('disabled', true);
		return false;
	});
	console.log('READY');
});
