document.addEventListener('DOMContentLoaded', function() {
  const countdownDate = new Date(2024, 0, 20, 0, 0, 0).getTime();

  const countdownElement = document.getElementById('countdown-fajar');
  const countdownInterval = setInterval(function() {
    const currentDate = new Date().getTime();
    const distance = countdownDate - currentDate;

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("fajar-days").innerHTML = days + " <small>Hari</small>";
	document.getElementById("fajar-hours").innerHTML = hours + " <small>Jam</small> ";
	document.getElementById("fajar-minutes").innerHTML = minutes + " <small>Menit</small> ";
	document.getElementById("fajar-seconds").innerHTML = seconds + " <small>Detik</small> ";


    if (distance < 0) {
      clearInterval(countdownInterval);
      countdownElement.innerHTML = '- - - -';
    }
  }, 1000);
});
