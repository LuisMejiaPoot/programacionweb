<?php
class Login extends CI_Controller
{


	function index()
	{
		if (!isset($_POST['matricula'])) {
			$data = [];
			$this->load->view('login', $data);
		} else {

			$this->load->model('Alumno_model');
			$this->form_validation->set_rules('matricula', 'Matrícula', 'required');
			if (($this->form_validation->run() == FALSE)) {
				$this->load->view('login');
			} else {
				$alumno = $this->Alumno_model->getAlumno($_POST['matricula']);
				if ($alumno) {
					$alumno = $alumno->row();
					$passwordDB = $alumno->password;
					$options = array('cost' => 11);
					if (password_needs_rehash($passwordDB, PASSWORD_DEFAULT, $options)) 
					{
						$passwordDB = password_hash($passwordDB, PASSWORD_DEFAULT, $options);
					}

					//$Existe=$this->Alumno_model->ValidarUsuario($_POST['matricula'],$_POST['password']);
					if (password_verify($_POST['password'], $passwordDB)) {
						if ($alumno->status == 1) {
							$_SESSION['matricula'] = $alumno->matricula;
							$_SESSION['usuario'] = $alumno->nom_alumno;
							$_SESSION['generacion'] = $alumno->anioregistro;
							$_SESSION['foto'] = $alumno->foto;
							$_SESSION['tipo'] = 0;
							header("Location:" . base_url() . 'inicio');
						} else {
							$data['error'] = "Te encuentras dado de baja, contacta a tu coordinador";
							$this->load->view('login', $data);
						}
					}
					//ccxc
					$Existe2 = $this->Alumno_model->ValidarModerador($_POST['matricula'], $_POST['password']);
					if ($Existe2) {
						$_SESSION['matricula'] = $Existe2->id_instructor;
						$_SESSION['usuario'] = $Existe2->nom_instructor;
						$_SESSION['tipo'] = 3;
						header("Location:" . base_url() . 'inicio');
					} else {
						$data['error'] = "Credenciales incorrectas, por favor vuelva a intentaR";
							$this->load->view('login', $data);   //   Lo regresamos a la pantalla de login y pasamos como parámetro el mensaje de error a presentar en pantalla
						}
					}
					else
					{
						$Existe = $this->Alumno_model->ValidarAdmin($_POST['matricula'], $_POST['password']);
						if ($Existe) {
							$_SESSION['matricula'] = $Existe->clave;
							$_SESSION['usuario'] = $Existe->nom_admin;
							if ($Existe->tipo == 2) {
								$_SESSION['tipo'] = 2;
							} else {
								$_SESSION['tipo'] = 1;
							}
							header("Location:" . base_url() . 'inicio');
						}
						else
						{
							$data['error'] = "Para poder ingresar necesitas registrarte primero";
							$this->load->view('login', $data); 
						}
					}
				}
			}
		}

		function registro()
		{
			$this->load->view('register');
		}

		public function getAlumno()
		{
			if ($this->input->is_ajax_request()) {
				$matricula = $this->input->post('matricula');
				$this->load->model('Alumno_model');
				$datos = $this->Alumno_model->getAlumno2($matricula);
				echo json_encode($datos);
			}
		}

		public function guardar()
		{
			$matricula = $this->input->post('matricula');
			$this->load->model('alumno_model');
			$this->load->model('carrera_model');
			$data['alumno'] = $this->alumno_model->getAlumno($matricula);
			if (empty($data['alumno'])) {
				$semestre = $this->input->post('semestre');
				$car = $this->input->post('carrera_id_car');
				switch ($semestre) {
					case 1:
					$generacion = 2022;
					break;
					case 3:
					$generacion = 2021;
					break;
					case 5:
					$generacion = 2020;
					break;
					default:
					$generacion = 0;
					break;
				}

				$fecha = date('Y-m-d');
				if($car=='AXX')
				{
					$data = array(
						'matricula' => $this->input->post('matricula'),
						'nom_alumno' => $this->input->post('nom_alumno'),
						'apaterno_alumno' => $this->input->post('apaterno_alumno'),
						'amaterno_alumno' => $this->input->post('amaterno_alumno'),
						'carrera_id_car' => $this->input->post('carrera_id_car'),
						'mail_alumno' => $this->input->post('mail_alumno'),
						'fecharegistro' => $fecha,
						'anioregistro' => $generacion,
						'revalida' => $generacion - 2,
						'password' => strtoupper($this->input->post('apaterno_alumno'))
					);
				}
				else
				{
					if($car=='BDS')
					{
						$data = array(
							'matricula' => $this->input->post('matricula'),
							'nom_alumno' => $this->input->post('nom_alumno'),
							'apaterno_alumno' => $this->input->post('apaterno_alumno'),
							'amaterno_alumno' => $this->input->post('amaterno_alumno'),
							'carrera_id_car' => $this->input->post('carrera_id_car'),
							'mail_alumno' => $this->input->post('mail_alumno'),
							'fecharegistro' => $fecha,
							'anioregistro' => $generacion,
							'revalida' => $generacion - 1,
							'password' => strtoupper($this->input->post('apaterno_alumno'))
						);
					}
					else
					{
						$data = array(
							'matricula' => $this->input->post('matricula'),
							'nom_alumno' => $this->input->post('nom_alumno'),
							'apaterno_alumno' => $this->input->post('apaterno_alumno'),
							'amaterno_alumno' => $this->input->post('amaterno_alumno'),
							'carrera_id_car' => $this->input->post('carrera_id_car'),
							'mail_alumno' => $this->input->post('mail_alumno'),
							'fecharegistro' => $fecha,
							'anioregistro' => $generacion,
							'password' => strtoupper($this->input->post('apaterno_alumno'))
						);
					}
				}
				$this->alumno_model->registrarAlumno($data);
				//Preguntar si es de primer semestre para registrarlo a la inducción
				if($generacion==2022)
				{
					$carrera=$this->carrera_model->getCarrera($car);
					$escuela=$carrera->result()[0]->escuela;
					if($escuela=='salud' || $escuela=='humanidades' || $escuela=='negocios' || $escuela=='derecho')
					{
					$data2 = array(
								'alumno_matricula' => $this->input->post('matricula'),
								'id_grupo' => 754,
								'calif' => 1
							);
					}
					else
					{
						$data2 = array(
								'alumno_matricula' => $this->input->post('matricula'),
								'id_grupo' => 755,
								'calif' => 1
							);
					}
					$this->alumno_model->insertarAlumnoAGrupo($data2);
				}

				//$url =  base_url();
				//$redirec =  $this->config->item('base_url') . "login";
				echo "<script>
				alert('Registro exitoso a la plataforma de eduvida');
				window.location.href = 'https://servicios.unimodelo.edu.mx/merida/eduvida/login';
				</script>";
			} else {
				echo "<script>
				alert('El alumno ya estaba registrado en el sistema');
				window.location.href = 'https://servicios.unimodelo.edu.mx/merida/eduvida/login';
				</script>";
			}
		}

		function salir()
		{
			$_SESSION = array();
		//Destruir Sesión
			session_destroy();
		//Redireccionar a login.php
			header("Location:" . base_url() . 'login');
		}
	}
