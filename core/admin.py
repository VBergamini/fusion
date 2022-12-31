from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Feature, Planos


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado', 'ativo')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'icone')


@admin.register(Planos)
class PlanosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'descricao', 'preco', 'icone')
