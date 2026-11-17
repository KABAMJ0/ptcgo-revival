from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d42d31e2-9ffb-5846-8f94-addad768bc36",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaSkarmoryex.Name",
    display_name="Mega Skarmory ex",
    searchable_by=["Mega Skarmory ex", "Basic", "MEGA", "ex", "MegaSkarmoryex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=55,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=227,
    abilities=[
        Attack(
            title="Sonic Ripper",
            game_text="Shuffle all Energy attached to this Pok\u00e9mon into your deck, and this attack does 220 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)