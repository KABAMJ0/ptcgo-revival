from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d35aa26-bf7c-59f8-8478-0201c1ba010c",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    display_name="Hattrem",
    searchable_by=["Hattrem", "Stage 1", "Hattrem"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hatenna.Name",
    family_id=856,
    abilities=[
        Attack(
            title="Calm Mind",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Brutal Swing",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)