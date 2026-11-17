from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4983962f-7cf7-5f1a-9773-bda644ad9507",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squawkabillyex.Name",
    display_name="Squawkabilly ex",
    searchable_by=["Squawkabilly ex", "Basic", "ex", "Squawkabillyex"],
    subtypes=["Basic", "ex"],
    collector_number=160,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=931,
    abilities=[
        Ability(
            title="Squawk and Seize",
            game_text="Once during your first turn, you may discard your hand and draw 6 cards. You can't use more than 1 Squawk and Seize Ability during your turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Motivate",
            game_text="Attach up to 2 Basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)