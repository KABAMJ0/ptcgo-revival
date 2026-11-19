from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class AdaptiveEvolutionPassive(Passive):
    def may_evolve_early(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


card = PokemonCardDef(
    guid="2328ab69-4e02-57b9-a9df-e2bb5e9d96bb",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    display_name="Spewpa",
    searchable_by=["Spewpa", "Stage 1", "Spewpa"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    family_id=664,
    abilities=[
        Ability(
            title="Adaptive Evolution",
            game_text="This Pok\u00e9mon can evolve during your first turn or the turn you play it.",
            passive=AdaptiveEvolutionPassive(),
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)