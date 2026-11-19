from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26bc30fd-37e6-5a91-84a8-23cf7677aab4",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=226,
    abilities=[
        Ability(
            title="Ripples",
            game_text="Once during your turn (before your attack), you may remove 1 damage counter from 1 of your Pok\u00e9mon (excluding Mantine). This power can't be used if Mantine is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Slash",
            game_text="Mantine can't attack during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)