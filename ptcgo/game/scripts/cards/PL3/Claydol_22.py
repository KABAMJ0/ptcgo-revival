from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e940aff6-a7ad-536b-9d39-d5872407b441",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Antique Magic",
            game_text="Put 3 damage counters on any Pok\u00e9mon (both yours and your opponent's) in any way you like.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Synchro Attack",
            game_text="If the Defending Pok\u00e9mon has the same remaining HP as Claydol, this attack's base damage is 90 instead of 30.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)