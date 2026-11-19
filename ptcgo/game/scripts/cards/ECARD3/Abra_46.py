from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import typed_energy_free_retreat_passive


card = PokemonCardDef(
    guid="4c489076-6601-5535-806a-2a30f7b9a287",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    display_name="Abra",
    searchable_by=["Abra", "Basic", "Abra"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=63,
    abilities=[
        Ability(
            title="Psychoflow",
            game_text="As long as there is a Psychic Energy card attached to Abra, its Retreat Cost is 0.",
            passive=typed_energy_free_retreat_passive(PokemonTypes.PSYCHIC.value),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)