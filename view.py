################################################################################################
#Busca de erro
################################################################################################
@n1_web_tools.route('/buscador-de-erros/', methods=['GET', 'POST'])
def erros():
    form = SearchForm(request.form)

    if request.method == 'POST' and form.validate():
        try:
            '''
                Aqui vai a lógica quando é realizado um POST na página
            '''
            return render_template('index.html', form=form)
        except Exception as error:
            trace = traceback.format_exc()
            print(trace)
            print(str(error))
            error = 'Ops, ocorreu um erro: '+str(error)
            return render_template('index.html', form=form, error=error)
    else:
        return render_template('index.html', form=form)
    return render_template('index.html')

################################################################################################
#Busca de erro API
################################################################################################
@n1_web_tools.route('/api/', methods=['GET', 'POST'])
def errosAPI():
    gerenciamento_conn = None
    try:
        '''
            Aqui vai a lógica da API
        '''
        return jsonify({'data': 'true'})
    except Exception as e:
        trace = traceback.format_exc()
        print(trace)
        print(e)
        return jsonify({'erro': str(e), 'stack':str(trace)})
