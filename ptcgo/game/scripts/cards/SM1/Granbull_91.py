from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3a41277-eae8-5eae-9759-41cec43457ed",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name",
    display_name="Granbull",
    searchable_by=["Granbull", "Stage 1", "Granbull"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    family_id=209,
    abilities=[
        Attack(
            title="Dark Clamp",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Fight Back",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)