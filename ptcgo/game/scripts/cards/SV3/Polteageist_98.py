from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0b392cdd-2d0b-5b08-ad78-75883aca77fa",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Polteageist.Name",
    display_name="Polteageist",
    searchable_by=["Polteageist", "Stage 1", "Polteageist"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name",
    family_id=854,
    abilities=[
        Attack(
            title="Antique Collecting",
            game_text="Put up to 2 in any combination of Item cards and Pok\u00e9mon Tool cards from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Pour Tea",
            game_text="Put 5 damage counters on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)