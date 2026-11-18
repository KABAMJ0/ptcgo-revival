from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="18a68364-e1cf-5ccf-ab0b-941adb38da0f",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Ability(
            title="Psychic Trace",
            game_text="Once during your turn (before your attack), if Claydol is your Active Pok\u00e9mon, you may shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand. This power can't be used if Claydol is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Ancient Mantra",
            game_text="If Claydol has any Psychic Energy attached to it, the Defending Pok\u00e9mon is now Confused. If Claydol has any Fighting Energy attached to it, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)