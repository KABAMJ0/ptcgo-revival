from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="24e284e8-28b5-5cdd-8973-88c17fc0d486",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansHoOhex.Name",
    display_name="Ethan's Ho-Oh ex",
    searchable_by=["Ethan's Ho-Oh ex", "Basic", "ex", "EthansHoOhex"],
    subtypes=["Basic", "ex"],
    collector_number=239,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Ability(
            title="Golden Flame",
            game_text="Once during your turn, you may attach up to 2 Basic Fire Energy cards from your hand to 1 of your Benched Ethan's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Shining Feathers",
            game_text="Heal 50 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 4},
            damage=160,
            effect=unimplemented,
        ),
    ],
)