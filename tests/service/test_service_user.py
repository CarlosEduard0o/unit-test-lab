from src.service.service_user import ServiceUser

class TestServiceUser:


###########  Usuario ja cadastrado  ###########

    def test_add_user_already_registered(self):
        name_add = 'Leonardo'
        job_add = 'TechLead'
        result_expect = 'Usuario ja cadastrado'
        service = ServiceUser()

        service.add_user(name=name_add, job=job_add)

        result = service.add_user(name=name_add, job=job_add)

        assert result == result_expect


###########  Usuário adicionado com sucesso  ###########

    def test_add_user_success(self):
        name_add = 'Leonardo'
        job_add = 'TechLead'
        result_expect = 'Usuario adicionado com sucesso'
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_add)

        assert result_expect == result


###########  Nome ou Profissão precisa ser um texto  ###########

    def test_add_user_invalid_name_or_job(self):
        result_expect = 'Nome ou Profissão precisa ser um texto'
        service = ServiceUser()
        
        invalid_name = 12345
        job = 'Analista de Sistemas'
        result = service.add_user(name=invalid_name, job=job)
        assert result == result_expect


###########  Usuario nao adicionado  ###########

    def test_validate_null_job(self):
        name_null = 'Matheus'
        job_null = None
        result_expect = 'Usuario nao adicionado'
        service = ServiceUser()

        result = service.add_user(name=name_null, job=job_null)

        assert result_expect == result


###########  Profissão atualizada com sucesso  ###########

    def test_update_user_success(self):
        name_update = "Leonardo"
        job_update = "Test Analyst"
        result_expect = "Profissão atualizada com sucesso"
        service = ServiceUser()

        service.add_user(name=name_update, job='TechLead')
        
        result = service.update_user(name=name_update, new_job=job_update)

        assert result_expect == result


###########  Selecionar User  ###########

    def test_search_user_success(self):
        name_to_search = "Leonardo"
        result_expect = "Profissão: " + "TechLead"
        service = ServiceUser()

        service.add_user(name=name_to_search, job='TechLead')

        result = service.select_user(name=name_to_search)

        assert result_expect == result


###########  Deletar usuário  ###########

    def test_delete_user_success(self):
        name_to_delete = "Leonardo"
        result_expect = "Usuario removido"
        service = ServiceUser()

        service.add_user(name=name_to_delete, job='TechLead')

        result = service.del_user(name=name_to_delete)

        assert result_expect == result


###########  Usuário não encontrado  ###########

    def test_user_not_found(self):
        name_not_found = 'teste-teste'
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()

        result = service.del_user(name=name_not_found)

        assert result == result_expect
