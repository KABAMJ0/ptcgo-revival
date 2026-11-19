from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class AdaptiveEvolutionPassive(Passive):
    def may_evolve_early(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


card = PokemonCardDef(
    guid="f76e0377-50dc-5258-8d1e-dc0d7c16ce79",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    display_name="Caterpie",
    searchable_by=["Caterpie", "Basic", "Caterpie"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=10,
    abilities=[
        Ability(
            title="Adaptive Evolution",
            game_text="This Pok\u00e9mon can evolve during your first turn or the turn you play it.",
            passive=AdaptiveEvolutionPassive(),
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)