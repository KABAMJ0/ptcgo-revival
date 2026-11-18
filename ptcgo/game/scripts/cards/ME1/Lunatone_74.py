from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b07c40c6-f621-54ca-b3aa-52bb7402ec7c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=337,
    abilities=[
        Ability(
            title="Lunar Cycle",
            game_text="Once during your turn, if you have Solrock in play, you may discard a Basic Fighting Energy card from your hand in order to use this Ability. Draw 3 cards. You can't use more than 1 Lunar Cycle Ability each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
    ],
)